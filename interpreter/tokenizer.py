from ExprHandlers import MathHandler
import Driver

''' Constants '''
# END is obviously the end of the compiled list
# And BEGIN is obviously the start of the compiled list
BEGIN, END = 'BEGIN', 'END'
# INTEGER is just the symbol for a number
INTEGER = 'INTEGER'
# Here we have the mathematics constants
PLUS, MINUS = 'PLUS', 'MINUS'
MULTIPLY, DIVIDE = 'MULTIPLY', 'DIVIDE'
# The prefixes
# So selecting a stack and its slot looks like this:
# $1~1 for stack 1, slot 1, or
# $3~4 for stack 3, slot 4
STACK_PREFIX = 'STACK PREFIX'
SLOT_PREFIX = 'SLOT PREFIX'
# Assignment operator
ASSIGN = 'ASSIGN'
# Layout character
LAYOUT = 'LAYOUT'
# End of statement
EOS = 'EOS'

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
