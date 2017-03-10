# Token types
# EOF is used for end of file (duh).
EOF, INTEGER = 'EOF', 'INTEGER'
# Mathematical operators
PLUS, MINUS = 'PLUS', 'MINUS'
TIMES, DIVIDE = 'TIMES', 'DIVIDE'
# Stack prefix. To select a stack and slot, you use the format: 
# $<stack number<stack slot
STACK_PREFIX = '$'
# < is used whenever you are selecting something.
# Ususally a stack and a slot on the stack.
SELECT_PREFIX = '<'

class Token(object):
    def __init__(self, type, value):
        # Token type: one of the ones defined at the start
        self.type = type
        # Token value: 0-9, +, -, *. /, or $
        self.value = value
    
    def __str__(self):
        '''
        A string representation of the token.
        eg:
        Token(INTEGER, 1), or
        Token(STACK_PREFIX, 2)
        '''
        return 'Token({type}, {value})'.format(
            type = self.type
            value = self.value
        )
        
    def __repr__(self):
        return self.__str__()
        

class Tokenizer(object):
    def __init__(self, text):
        # String input
        self.text = text
        # An index onto self.text
        self.pos = 0
        # Current token instance
        self.currentToken = None
        # List of errors
        self.errors = {1: 'Error: Expected token does not match current token.'}
        
    def error(errorId):
        raise Exception(self.errors[errorId])
        
    def getNextToken(self):
        '''
        Tokenizer, lexer, scanner, whatever you want to call it, this is the function 
        responsible for splitting the input up into tokens, one at a time.
        
        This is NOT the part responsible for handling the tokens. That part is 
        in a file called driver.py.
        '''
        
        text = self.text
        
        # If the position is greater than the length of the input, return an EOF
        # token.
        if self.pos > len(text):
            return Token(EOF, None)
            
        # The current character, used for determining what token to return.
        currentChar = text[self.pos]
        
        if currentChar.isDigit():
            token = Token(INTEGER, int(currentChar))
            self.pos += 1
            return token
            
        if currentChar == '+':
            token = Token(PLUS, currentChar)
            self.pos += 1
            return token
            
        if currentChar == '-':
            token = Token(MINUS, currentChar)
            self.pos += 1
            return token
            
        if currentChar == '*':
            token = Token(TIMES, currentChar)
            self.pos += 1
            return token
            
        if currentChar == '/':
            token = Token(DIVIDE, currentChar)
            self.pos += 1
            return token
            
        if currentChar == '$':
            token = Token(STACK_PREFIX, currentChar)
            self.pos += 1
            return token
            
        if currentChar == '<':
            token = Token(SELECT_PREFIX, currentChar)
            self.pos += 1
            return token
            
    def eat(self, tokenType):
        if self.currentToken.type == tokenType:
            self.token = self.getNextToken()
            return 1
        else:
            return 0
