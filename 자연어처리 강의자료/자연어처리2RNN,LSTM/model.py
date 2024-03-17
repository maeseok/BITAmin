import torch
import torch.nn as nn
import numpy as np
from torch.autograd import Variable




class LSTM_net(nn.Module):
    def __init__(self, num_output, input_size, hidden_size, linear_size, num_layers, seq_length, device):
        super(LSTM_net, self).__init__()
        self.device = device
        self.num_output = num_output
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.seq_length = seq_length
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size = input_size, hidden_size = hidden_size,
                            num_layers = num_layers, dropout = 0.3, bidirectional = True)
        self.fclayer = nn.Linear(hidden_size, linear_size)
        self.outlayer = nn.Linear(linear_size, num_output)

    def forward(self, x):
        scaler = 2 if self.lstm.bidirectional == True else 1
        h_state = Variable(torch.zeros(self.num_layers*scaler, x.size(0),
                                       self.hidden_size, requires_grad = True)).to(self.device)
        c_state = Variable(torch.zeros(self.num_layers*scaler, x.size(0),
                                       self.hidden_size, requires_grad = True)).to(self.device)

        lstm_out, (h, c) = self.lstm(x.transpose(1,0), (h_state, c_state))
        h = h[-1]
        h = self.fclayer(h).relu()
        predict = self.outlayer(h)
        return predict


class CNN_1D(nn.Module):
    def __init__(self, num_output, input_size, hidden_size, linear_size, kernel_size, seq_length, device):
        super(CNN_1D, self).__init__()
        self.device = device
        self.conv1 = nn.Conv1d(in_channels = input_size, out_channels = hidden_size, kernel_size = kernel_size)
        self.fclayer = nn.Linear(hidden_size * (seq_length - kernel_size + 1), linear_size)
        self.outlayer = nn.Linear(linear_size, num_output)

    def forward(self, x):
        x = self.conv1(x.transpose(1,2)).flatten(1)
        x = self.fclayer(x).relu()
        predict = self.outlayer(x)
        return predict

class seq2seq(nn.Module):
    def __init__(self, enc_size, dec_size, hidden_size, num_layers, seq_length_enc, seq_length_dec, device, emb_size = 16):
        super(seq2seq, self).__init__()
        self.device = device
        self.hidden_size = hidden_size
        self.seq_length_enc = seq_length_enc
        self.seq_length_dec = seq_length_dec
        self.num_layers = num_layers
        self.lstm_enc = nn.LSTM(input_size = emb_size, hidden_size = hidden_size,
                            num_layers = num_layers, dropout = 0.3, bidirectional = True)
        self.lstm_dec = nn.LSTM(input_size = emb_size, hidden_size = hidden_size,
                                num_layers = num_layers * (2 if self.lstm_enc.bidirectional == True else 1),
                                dropout = 0.3, bidirectional = False)
        self.fclayer1 = nn.Linear(hidden_size, hidden_size)
        self.fclayer2 = nn.Linear(hidden_size, dec_size)
        self.embed_Enc = nn.Embedding(enc_size, emb_size)
        self.embed_Dec = nn.Embedding(dec_size, emb_size)

    def forward(self, x, y, test = False):
        scaler = 2 if self.lstm_enc.bidirectional == True else 1
        h_state = Variable(torch.zeros(self.num_layers*scaler, x.size(0),
                                       self.hidden_size, requires_grad = True)).to(self.device)
        c_state = Variable(torch.zeros(self.num_layers*scaler, x.size(0),
                                       self.hidden_size, requires_grad = True)).to(self.device)
        embedded = self.embed_Enc(x.argmax(2).transpose(1,0))
        _, (h, c) = self.lstm_enc(embedded, (h_state, c_state))

        predict = torch.zeros(y.size(1), y.size(0), y.size(2)).to(self.device)

        if test:
            pred_in = torch.zeros(1, y.size(0), y.size(2)).to(self.device)
            pred_in[0, :, :] = y[:, 0, :]
            for i in range(y.size(1)-1):
                pred, _, = self.lstm_dec(self.embed_Dec(pred_in.argmax(2)), (h, c))
                pred = self.fclayer2(self.fclayer1(pred.relu()))
                pred_in[0,:,:] = pred
                predict[i,:,:] = pred
        else:
            pred_in = torch.zeros(1, y.size(0), y.size(2)).to(self.device)
            pred_in[0, :, :] = y[:, 0, :]
            for i in range(y.size(1) - 1):
                if torch.rand(1) <= 0.75:
                    pred, _, = self.lstm_dec(self.embed_Dec(pred_in.argmax(2)), (h, c))
                else:
                    pred, _, = self.lstm_dec(self.embed_Dec(y[:,i,:].unsqueeze(0).argmax(2)), (h, c))
                pred = self.fclayer2(self.fclayer1(pred.relu()))
                pred_in[0, :, :] = pred
                predict[i, :, :] = pred
        return predict
