import tokens
import grabbertools
import Global

def parseVarDec(text):
    # Parses a valid variable declaration into a block
    # Assumes that the inputted text is a valid variable declaration
    # Meant to be used in tandem with grabbertools.getNextVarDec()
    # Note: not called if no variable declaration is found
    
    tokenList = []
    pos = 0
    
    # Make the first element of the token list the variable type
    # As defined in the language specifications
    tokenList.append(grabbertools.getNextWord(text).title())
    pos += len(grabbertools.getNextWord(text)) + 1
    
    # Now get the variable name
    tokenList.append(tokens.Token(tokens.VAR_NAME, grabbertools.getNextWord(text[pos:])))
    
    pos += len(grabbertools.getNextWord(text[pos:]))
    
    if grabbertools.getNextVarInit(text[pos:]) is not None:
        
        varinit = grabbertools.getNextVarInit(text[pos:])
        
        if (tokenList[0] == 'Char'):
            
            if (grabbertools.getNextChar(varinit) != None):
                tokenList.append(tokens.Token(tokens.CHAR, 
                                              grabbertools.getNextChar(varinit)))
            else:
                Global.ErrorsGenerated.append('Invalid value for char variable')
                return None
                
        elif (tokenList[0] == 'Str'):
            
            if (grabbertools.getNextStr(varinit) != None):
                tokenList.append(tokens.Token(tokens.STR,
                                              grabbertools.getNextStr(varinit)))
                                              
            else:
                Global.ErrorsGenerated.append('Invalid variable for string variable')
                return None
                
        elif (tokenList[0] == 'Short' or 'Int' or 'Long'):
            
            if (grabbertools.getNextNum(varinit) is not None):
                
                tokenList.append(tokens.Token(tokens.Var[tokenList[0]], 
                                                grabbertools.getNextNum(varinit)))
            else:
                
                Global.ErrorsGenerated.append('Invalid value for ', tokenList[0], ' variable.')
        else:
            
            Global.ErrorsGenerated.append('Invalid type')
            return 0
    
    return (tokenList)
    
def parseSimpleState(text):
    # Parses a simple statement into a token list
    # Assumes that the inputted text is a valid statement.
    
    # But we check anyway
    if text == None:
        return None
        
    tokenList = []
    
    tokenlistpos = 0
    
    pos = 0
    
    # This loop handles most of the things
    while(pos < len(text)):
        cc = text[pos] # cc = current char
        
        if cc.isalnum() == True:
            # Just avoiding errors with the if statement below
            if pos > 0:
                if text[pos - 1].isalnum == True:
                    tokenList[tokenlistpos].value += cc
                else:
                    tokenList.append(tokens.Token(tokens.OD_NAME, cc))
            else:
                tokenList.append(tokens.Token(tokens.OD_NAME, cc))
                
            tokenlistpos = len(tokenList)
                
        elif cc == '+' or cc == '-' or cc == '*' or cc == '-' or cc == '=':
            tokenList.append(tokens.Token(tokens.OP, cc))
            tokenlistpos = len(tokenList)
        
        else:
            tokenlistpos = len(tokenList)
            
        pos += 1
            
    return tokenList
    
    
