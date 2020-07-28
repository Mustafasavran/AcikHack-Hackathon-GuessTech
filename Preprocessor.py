import re
import string
class Preprocessor:
  def remove_newline(self,sentences,newline = "\n"):
    """
    params:
    sentences:list of strings
    newline: newline character

    return: list of strings 

    remove all new line character from all strings in the list"""
    return [sentence.replace(newline,"") for sentence in sentences]
  def remove_urls(self,sentences):
    """
    params:
    sentences:list of strings

    return: list of strings 

    remove all urls character from all strings in the list"""

    return [re.sub(r'http\S+', '', sentence) for sentence in sentences]
  def remove_digits(self,sentences):
    """
    params:
    sentences:list of strings

    return: list of strings 

    remove all digits character from all strings in the list"""

    return [sentence.translate(str.maketrans('', '', string.digits)).strip() for sentence in sentences]
  
  def remove_punctuations(self,sentences):
    """
    params:
    sentences:list of strings

    return: list of strings 

    remove all punctuations character from all strings in the list"""

    return [sentence.translate(str.maketrans("{}\\“”’".format(string.punctuation), ' '*len("{}\\“”’".format(string.punctuation)), )).strip() for sentence in sentences]
  def remove_extreme(self,sentences,n = 2):
    """
    params:
    sentences:list of strings
    n: character number
    return: list of strings 

    remove all strings that have less than n character"""
    return [sentence  for sentence in sentences if len(sentence)>2]
  def preprocess(self,sentences):
    """
    params:
    sentences:string
    return: list of strings 

    preprocess the emails"""

    sentences = sentences.replace("?",".").replace("!",".").split(".") # tokenize string
    
    sentences = self.remove_newline(sentences)
    sentences = self.remove_urls(sentences)
    sentences = self.remove_digits(sentences)
    sentences = self.remove_punctuations(sentences)
    sentences = self.remove_extreme(sentences)
    
    sentences = [" ".join(sentence.split()) for sentence in sentences]

    return sentences


