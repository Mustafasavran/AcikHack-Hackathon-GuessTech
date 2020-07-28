from Preprocessor import Preprocessor
from Vocabulary import Vocabulary
class DataHandler:
  def __init__(self):
    self.preprocessor = Preprocessor()
    
  
  def text_to_inds(self,data,k = 4):
    """
    params:
    data:list --> list of list of words
    k: int --> split k words
    return: list,list:  splitted and indeksed words and labels

    split words into k words and add some padding"""
    
    features_ = []
    label = []
    data = [sentence.split() for sentence in data]
    
    for words in data:
      if len(words)>k:
        for inds in range(0,len(words)):
          if inds + k>= len(words):
            break
          if inds + k< len(words):

            word_vector =self.vocab.get_inds_vector(words[inds:inds+k])
            features_.append(word_vector)
            label.append(self.vocab.vocab[words[inds+k].lower()])
            copy_list = word_vector.copy()
            for i in range(2):
              copy_list = copy_list.copy()
              copy_list[i] = 0
              
              features_.append(copy_list)
              label.append(self.vocab.vocab[words[inds+k].lower()])
          elif len(words)>2:

            temp = []
            temp.extend(self.vocab.get_inds_vector(words))
            

            while len(temp) !=k+1:
              temp.insert(0,0)
            features_.append(temp[:k])
          
            label.append(temp[k])
    print(label)
    return features_,label

  def prepare_data(self,data):
    
    preprocessed_data = self.preprocessor.preprocess(data)
    self.vocab = Vocabulary(preprocessed_data)
    return self.text_to_inds(preprocessed_data)

