from keras.utils import Sequence
import keras
from keras import Sequential,optimizers
from keras.layers import Embedding,LSTM,Dense,Dropout
from keras.callbacks import ModelCheckpoint
import numpy as np
import argparse
from DataHandler import DataHandler
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--data", type=str,
	              help="eğitmek için veri seti yolu")
ap.add_argument("-m", "--model_adi", type=str, default="model.h5",
	help="modelin kaydedilecek yeri")
args = vars(ap.parse_args())
data = open(args["data"],"r",encoding = "windows-1254")
read_data = data.read()
data_handler = DataHandler()
data,label = data_handler.prepare_data(read_data)
class MY_Generator(Sequence):

    def __init__(self, words, labels, batch_size):
        self.words, self.labels = words, labels
        self.batch_size = batch_size

    def __len__(self):
        return int(np.ceil(len(self.words) // float(self.batch_size)))

    def __getitem__(self, idx):
        batch_x = self.words[idx * self.batch_size:(idx + 1) * self.batch_size]
        batch_y = self.labels[idx * self.batch_size:(idx + 1) * self.batch_size]

        return np.array(batch_x), keras.utils.to_categorical(batch_y,num_classes = len(data_handler.vocab.vocab))
def create_model(vocabulary_size, seq_len,l_r = 0.0001):
  model = Sequential()
  model.add(Embedding(vocabulary_size, seq_len,input_length=seq_len))
  model.add(LSTM(64,return_sequences=True))
  model.add(LSTM(64))
  model.add(Dense(64,activation='relu'))
  model.add(Dense(vocabulary_size,activation='softmax'))
  opt_adam = optimizers.adam(lr=l_r)
  model.compile(loss='categorical_crossentropy',optimizer=opt_adam,metrics=['accuracy'])
  model.summary()
  return model





my_training_batch_generator = MY_Generator(data,label, 64)
model = create_model(len(data_handler.vocab.vocab),4)
path = args["model_adi"]
checkpoint = ModelCheckpoint(path, monitor='loss', verbose=1, save_best_only=True, mode='min')
history = model.fit_generator(generator=my_training_batch_generator,
                                          steps_per_epoch=(len(data)//4),
                                          epochs=120,
                                          verbose=1,
                                          callbacks=[checkpoint])