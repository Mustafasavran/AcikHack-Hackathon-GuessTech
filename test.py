from keras.models import load_model
import argparse
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", type=str,
	              help="modelin yolu")

args = vars(ap.parse_args())
model = load_model(args["model"])
vocab_file = open("turkish_vocab.txt","r")
i = 1
vocab = {}
for kelime in vocab_file:
  kelime.replace("\n","")
  vocab[ kelime.replace("\n","")] = i
  i+=1
inv_vocab= {v: k for k, v in vocab.items()}
kelime = None
while kelime != "q":
    kelime = input("Cümle giriniz(çıkmak için q): ")
    if kelime.lower() == "q":
      break
    if kelime.isdigit():
      print("Geçersiz kelime")
      continue
    splited = kelime.split(" ")
    indexed = []
    for word in splited[-4:]:
      
      if word in vocab:
        indexed.append(vocab[word.lower()])
      else:
        indexed.append(0)

    while len(indexed)<4:
      indexed.insert(0,0)
    print("cümle: "+kelime)
    print("tahmin:"+inv_vocab[model.predict_classes(np.array(indexed).reshape(1,4))[0]])
    print("------------------------------------------------------\n")
  
