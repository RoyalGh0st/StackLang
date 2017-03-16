from ExprHandlers import MathHandler
import Stacks
import Tokens

class Token(object):
    '''
    The token class. The list that the tokenizer creates from a text file is made up of these.
    '''
    def __init__(self, type, value):
        self.type = type
        self.value = value
        
    def __str__(self):
        # Returns a string representation of the token.
        # For example: 
        # T(INTEGER, 1), or
        # T(PLUS, +)
        return 'T({type}, {value})'.format (
            type = self.type,
            value = repr(self.value)
        )
        
    def __repr__(self):
        return self.__str__()
        
class Tokenizer(object):
    '''
    The tokenizer. This is what 'compiles' or translates the text into a list of tokens.
    '''
    def __init__(self, text):
        self.text = text
        # Index onto text
        self.pos = 0
        # Current token
        self.currentToken = None
        # Token list
        # We start it with the begin token
        self.tokenList = [[[None] for x in (Driver.Stacks)] for y in Driver.Slots]
        
    def compileToList(self):
        '''
        This is what handles the actual 'compiling'. Rather, this function
        creates the list of tokens that is executed by the driver.
        '''
        text = self.text
        pos = self.pos
        
        
        
        
    
    def checkToken(self, tokenType):
        if (self.currentToken.type == tokenType):
            return 1
        else:
            return 0
