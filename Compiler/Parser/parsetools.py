import tokens
import grabbertools

def parseVarDec(text):
    # Parses a valid variable declaration into a block
    # Assumes that the inputted text is a valid variable declaration
    # Meant to be used in tandem with grabbertools.getNextVarDec()
    tokenList = []
    pos = 0
    
    num = None
    
    # Make the first element of the token list the variable type
    # As defined in the language specifications
    tokenList.append(grabbertools.getNextWord(text).title())
    pos += len(grabbertools.getNextWord(text)) + 1
    
    tokenList.append(tokens.Token(tokens.VAR_NAME, grabbertools.getNextWord(text[pos:])))
    print(grabbertools.getNextWord(text[pos:]))
    pos += len(grabbertools.getNextWord(text[pos:]))
    
    print (len(text), pos)
    print(text[pos:])
    
    print(grabbertools.getNextVarInit(text[pos:]))
    
    if grabbertools.getNextVarInit(text[pos:]) is not None:
        varinit = grabbertools.getNextVarInit(text[pos:])
        print('varinit ', varinit)
        if (tokenList[0] == 'Char'):
            
            if (grabbertools.getNextWord(varinit) is not None):
                
                if len(grabbertools.getNextWord(varinit)) > 1:
                    
                    print('Invalid value for char variable.')
                    return 0
                    
                tokenList.append(tokens.Token(tokens.CHAR, grabbertools.getNextWord(varinit)))
            
            else:
                
                print('Invalid value for char variable.')
                return 0
                
        elif (tokenList[0] == 'Str'):
            
            if (grabbertools.getNextWord(varinit) is not None):
                
                tokenList.append(tokens.Token(tokens.STR, grabbertools.getNextWord(varinit)))
                
            else:
                
                print('Invalid value for str variable.')
                return 0
                
        elif (tokenList[0] == 'Short' or 'Int' or 'Long'):
            
            if grabbertools.getNextNum(varinit) is not None:
                tokenList.append(tokens.Token(tokens.NUM, 
                                grabbertools.getNextNum(varinit)))
            
            else:
                
                print('Invalid value for', tokenList[0], 'variable.')
                return 0
            
        else:
            
            print('Invalid type.')
            return 0
    
    return (tokenList)
