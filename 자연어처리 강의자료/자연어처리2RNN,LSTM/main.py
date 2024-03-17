import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import argparse
from torch.utils.data import DataLoader, TensorDataset
from torch import LongTensor as LT
from torch import FloatTensor as FT
from model import LSTM_net, CNN_1D
from tqdm import tqdm
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument('--lr', type = float, default = 1e-3)
parser.add_argument('--nepoch', type = int, default = 20)
parser.add_argument('--seqlen', type = int, default = 5)
args = parser.parse_args()


class Generate_Dataset(torch.utils.data.Dataset):
    def __init__(self, device, data, seq_length):
        self.x_data = np.zeros((data.shape[0]-seq_length - 1, seq_length, data.shape[1])) # seq_length = 10, input_size = 7
        self.y_data = np.zeros((data.shape[0]-seq_length - 1, 1)) # output = 1
        for i in range(data.shape[0] - seq_length - 1):
            for j in range(seq_length):
                self.x_data[i,j,:] = data[i+j,:].ravel()
            self.y_data[i,:] = data[i+seq_length,0].ravel()
        self.device = device
    def __len__(self):
        return len(self.x_data)
    def __getitem__(self, idx):
        x = FT(self.x_data[idx]).to(self.device)
        y = FT(self.y_data[idx]).to(self.device)
        return x, y

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
lstm_net = LSTM_net(num_output = 1, input_size = 7, hidden_size = 128, linear_size = 128,
                    num_layers = 3, seq_length = args.seqlen, device = device).to(device)
#lstm_net = CNN_1D(num_output = 1, input_size = 7, hidden_size = 128, linear_size = 128,
#                  kernel_size = 5, seq_length = args.seqlen, device = device).to(device)


data = pd.read_csv('household_power_consumption.txt', sep = ';',
                   parse_dates = {'dt': ['Date', 'Time']},
                   infer_datetime_format = True, na_values = ['nan', '?'], index_col = 'dt')
for i in range(7):
    data.iloc[:,i] = data.iloc[:,i].fillna(data.iloc[:,i].mean())
print(data.isnull().sum())
data_resample = data.resample('h').mean()
scale = MinMaxScaler(feature_range = (0, 1))
data_scaled = scale.fit_transform(data_resample)
data_train = data_scaled[:10000, :]
data_test = data_scaled[10000:10200, :]


dataset = Generate_Dataset(device, data_train, seq_length = args.seqlen)
dataset_test = Generate_Dataset(device, data_test, seq_length = args.seqlen)
train_loader = DataLoader(dataset, batch_size = 256, shuffle = True)
test_loader = DataLoader(dataset_test, shuffle = False)
optimizer = torch.optim.Adam(lstm_net.parameters(), lr = args.lr)


for epoch in range(args.nepoch):
    with tqdm(train_loader, unit = 'batch') as tepoch:
        for x, y in tepoch:
            predict = lstm_net(x)
            loss = torch.nn.functional.mse_loss(predict, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            tepoch.set_description(f"Epoch {epoch}")
            tepoch.set_postfix(loss = loss.item())

print('Testing')
ypred = np.zeros(len(dataset_test))
ytruth = np.zeros(len(dataset_test))
with tqdm(test_loader) as tepoch:
    for i, (x, y) in enumerate(tepoch):
        yhat = lstm_net(x)
        ypred[i] = yhat.cpu().detach().numpy()
        ytruth[i] = y
        loss = torch.nn.functional.mse_loss(yhat, y)
        tepoch.set_postfix(loss=loss.item())
plt.plot(ytruth, marker = '.', label = 'Truth')
plt.plot(ypred, 'r', label = 'Prediction')
plt.show()

