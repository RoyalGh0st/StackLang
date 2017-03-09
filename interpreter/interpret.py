# Token types
# EOF is used for end of file (duh).
EOF, INTEGER = 'EOF', 'INTEGER'
# Mathematical operators
PLUS, MINUS = 'PLUS', 'MINUS'
TIMES, DIVIDE = 'TIMES', 'DIVIDE'
# Stack prefix. To select a stack, you use the format: $(stack number)
STACK_PREFIX = '$'

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
        

class Interpreter(object):
    def __init__(self, text):
        # String input
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.currentToken = None
        # registers for math
        self.mathLeftRegister = [0] * 2
        self.mathRightRegister = [0] * 2
        
        
    def error(self):
        raise Exception('Error parsing input.')
        
    def getNextToken(self):
        '''
        Lexical analyzer/tokenizer/scanner, whatever you want to call it.
        
        This is the part responsible for splitting up the input into tokens.
        '''
        text = self.text
        
        # if self.pos is past the end of self.text, return EOF
        if self.pos > len(text):
            return Token(EOF, None)
            
        currentChar = text[self.pos]
            
        # if the character is a digit, convert it to an integer token.
        if currentChar.isDigit():
            token = Token(INTEGER, currentChar)
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
            
    def eat(self, tokenType):
        # Check to see if current token matches passed token.
        # If so, "eat" the current token and assign the current token to the 
        # next token.
        # If they do not match, raise an exception.
        if self.currentToken.type == tokenType:
            self.currentToken = self.getNextToken()
        else:
            self.error()
            
    def exprAdd(self):
        '''exprAdd = INTEGER PLUS INTEGER'''
        # Set current token to be the first from the input
        self.currentToken = self.getNextToken()
        
        # We expect the left to be a two-digit integer
        mathLeftRegister[0] = self.currentToken.value
        self.eat(INTEGER)
        mathLeftRegister[1] = self.currentToken.value
        self.eat(INTEGER)
        
        # We expect the middle token to be a plus
        # You know, because this is the addition expression
        op = self.currentToken
        self.eat(PLUS)
        
        # And now, we fill up the right register
        mathRightRegister[0] = self.currentToken.value
        self.eat(INTEGER)
        mathRightRegister[1] = self.currentToken.value
        self.eat(INTEGER)
        
        left = mathLeftRegister[0] + mathLeftRegister[1]
        right = mathRightRegister[0] + mathRightRegister[1]
        
        result = left + right
        
        return result
        
            
