import importlib.util

spec = importlib.util.spec_from_file_location("Tokens.py", "../Tokens.py")
Tokenizer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Tokens)

spec = importlib.util.spec_from_file_location("Stacks.py", "../Stacks.py")
Stacks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(Stacks)

class MathHandler(object):
    '''
    This handler handles all number related things.
    Math, conversion of tokens to integers, anything involving numbers,
    this handler takes care of it.
    '''
    def __init__(self):
        # The registers
        self.RegisterSet1 = [0, 0]
        self.RegisterSet2 = [0, 0]
        # Coordinate registers
        self.CoordRegisters = [[0, 0], [0, 0]]
        
    def convertTokensToInt(self, tokenList):
        ''' This function converts INTEGER tokens to a number.
        It should probably be called convertTokensToNum, but whatever.
        '''
        total = 0
        pos = 0
        
        # This function assumes that the first token provided is an integer.
        # If not, it will error out.
        if (tokenList[pos].type != Tokenizer.INTEGER):
            raise Exception("Error converting tokens to integer: first token provided is not an integer token.")
            
        while (tokenList[pos].type == Tokenizer.INTEGER):
            total += tokenList[pos].value
            pos += 1
        
        return total
    
    def add(self, tokenList):
        ''' This function performs addition on two stack slots.
        It is called when the "add" instruction is found in the instruction stack.
        '''
        
        pos = 1
        
        # First, we check to see that the arguments are correct.
        # It is assumed that we start on the opening parenthese after the add function
        # is called. If not, error out.
        if (tokenList[0].type != Tokens.PAREN or tokenList[0].value != '('):
            raise Exception("Syntax error: Missing opening paren on addition function.")
        
        # If our program is correct with the first paren, we check for the second paren.
        # Because add is called like: "ADD((1, 1), (1, 2))"
        if (tokenList[1].type != Tokens.PAREN or tokenList[1].value != '('):
            raise Exception("Syntax error: Missing opening paren for first argument of addition function.")
        
        pos += 1
        
        if (tokenList[pos].type != Tokens.INTEGER):
            raise Exception("Syntax error: Invalid location.")
        
        # Set the first coordinate register
        self.CoordRegisters[0][0] = self.convertTokensToInt(tokenList[pos::])
        
        pos += 1
        
        # At this point, the next character should be a comma.
        if (tokenList[pos].type != Tokens.COMMA):
            raise Exception("Syntax error: Incorrect format for specifying stack location.")
            
        pos += 1
        
        # Whitespace is okay
        while (tokenList[pos].type == Tokens.WHITESPACE):
            pos += 1
            
        pos += 1
        
        # Now, we check for the second number
        if (tokenList[pos].type != Tokens.INTEGER):
            raise Exception("Syntax error: Invalid location.")
            
        self.CoordRegisters[0][1] = self.convertTokensToInt(tokenList[pos::])
        
        # Now, the first register is set to the specified stack slot's value.
        self.RegisterSet1[0] = Stacks.Stacks[self.CoordRegisters[0][0], self.CoordRegisters[0][1]]
        
        # Finally, we check to see that the parens close up
        pos += 1
        
        if (tokenList[pos].type != Tokens.PAREN or tokenList[pos].value != ')'):
            raise Exception("Missing closing parenthese.")
        
        # Then, we do ALL THIS CRAP AGAIN
        pos += 1
        
        if (tokenList[pos].type != Tokens.INTEGER):
            raise Exception("Syntax error: Invalid location.")
        
        self.CoordRegisters[1][0] = self.convertTokensToInt(tokenList[pos::])
        
        pos += 1
        
        if (tokenList[pos].type != Tokens.COMMA):
            raise Exception("Syntax error: Incorrect format for specifying stack location.")
            
        pos += 1
        
        while (tokenList[pos].type == Tokens.WHITESPACE):
            pos += 1
            
        pos += 1
        if (tokenList[pos].type != Tokens.INTEGER):
            raise Exception("Syntax error: Invalid location.")
            
        self.CoordRegisters[1][1] = self.convertTokensToInt(tokenList[pos::])
        
        self.RegisterSet1[1] = Stacks.Stacks[self.CoordRegisters[1][0], self.CoordRegisters[1][1]]
        
        # Check that the parentheses close up
        pos += 1
        if (tokenList[pos].type != Tokens.PAREN or tokenList[pos].value != ')'):
            raise Exception("Missing closing parenthese.")
            
        pos += 1
        if (tokenList[pos].type != Tokens.PAREN or tokenList[pos].value != ')'):
            raise Exception("Missing closing parenthese.")
            
        # Add the two registers together
        total = self.RegisterSet1[0] + self.RegisterSet1[1]
        
        return total
    
    def subtract(self, tokenList):
        ''' If you want an explanation of what this does, look at the add function. It's basically the same,
        but with subtraction at the end.
        '''
        
        pos = 1
        
