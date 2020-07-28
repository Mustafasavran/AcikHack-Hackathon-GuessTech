class Vocabulary:
  def __init__(self,data):
    self.create_vocab(data)
    self.create_inv_vocab()
    
  
  def create_vocab(self,data):
    """
    params:
    sentences:string
    return: dict:vocabulary dictionary

    create vocabulary dictionary"""
    vocab_file = open("turkish_vocab.txt","w")
    self.vocab = {}
    splited_words = [] 
    i=1
    for text in data:
      
      words = " ".join(text.split()).lower().split()
      splited_words.append(words)
      for word in words:
        if word not in self.vocab:
          vocab_file.write(word+"\n")
          self.vocab[word] = i
          i+=1
    return self.vocab
  def create_inv_vocab(self):

    self.inv_vocab= {v: k for k, v in self.vocab.items()}
    return self.inv_vocab
  def get_inds_vector(self,words):
    return [self.vocab[word.lower()] for word in words]

    

