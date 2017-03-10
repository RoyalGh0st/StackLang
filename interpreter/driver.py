import tokenizer
from tokenizer import Tokenizer

class Driver(object):
    def __init__(self, text):
        self.text = text
        # These are for math expressions.
        self.mathLRegister = 0
        self.mathRRegister = 0
        self.tokenizer = Tokenizer()
        
    def ConvertTokensToInt(self, Token):
        
