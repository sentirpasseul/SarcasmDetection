from nltk import sent_tokenize

class Algorithm():
    def __init__(self, text: str):
        self.text = text



    def get_tokens(self):
        sentence_tokens = sent_tokenize(self.text)




test1 = Algorithm("Привет! Меня зовут Макс!").get_tokens()
