import tensorflow as tf
from tensorflow.python.client import device_lib
# tensorflow version 확인 후 GPU 확인
import tensorflow as tf

print(f'tf.__version__: {tf.__version__}')

gpus = tf.config.experimental.list_physical_devices('GPU')
tf.config.list_physical_devices('GPU') #이 코드도 가능
for gpu in gpus:
    print(gpu)
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
#device_lib.list_local_devices()
#print(tf.__version__) # 텐서플로우 버전 확인

#tf.test.is_built_with_cuda() # cuda 잘 작동되는지

#tf.test.is_built_with_gpu_support() # gpu support 되는지 확인

#tf.test.gpu_device_name() # gpu 장치 이름들

#cuda 11.8
#cudnn 8.6