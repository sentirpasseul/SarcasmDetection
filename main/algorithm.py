import nltk
from nltk import sent_tokenize, word_tokenize
import pandas as pd
import numpy as np

class Algorithm():
    def __init__(self, text: str):
        self.text = text


    def get_tokens(self):
        #Функция для получения предложений текста

        sentence_tokens = np.array([sentence for sentence in sent_tokenize(self.text, language='russian')])
        #list_words = np.array([word_tokenize(sentence) for sentence in sentence_tokens])
        print(sentence_tokens)
        #print(list_words)
        #word_tokens = [word_tokenize(sentence) for sentence in sentence_tokens]
        #word_tokens = np.array(word_tokens)
        #print(sentence_tokens)
        #print(word_tokens)

        return sentence_tokens
        #word_tokens

    def get_df(self):
        #Функция для получения датафрейма текста

        sentences = self.get_tokens()
        print(sentences)

    def get_tonality(self):
        ...





c = Algorithm("Привет! Меня зовут Макс!").get_tokens()
