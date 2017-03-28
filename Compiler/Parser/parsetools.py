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
    
    # Now get the variable name
    tokenList.append(tokens.Token(tokens.VAR_NAME, grabbertools.getNextWord(text[pos:])))
    
    print('Remaining text: ', text[pos:])
    print('getVarInit: ', grabbertools.getNextVarInit(text[pos:]))
    
    pos += len(grabbertools.getNextWord(text[pos:]))
    
    if grabbertools.getNextVarInit(text[pos:]) is not None:
        
        varinit = grabbertools.getNextVarInit(text[pos:])
        
        if (tokenList[0] == 'Char'):
            
            if (grabbertools.getNextChar(varinit) != None):
                tokenList.append(tokens.Token(tokens.CHAR, 
                                              grabbertools.getNextChar(varinit)))
                
                print('parseVarDec->Char->getNextChar(varinit): ', grabbertools.getNextChar(varinit)[1:-1])
            else:
                print("Invalid value for char variable.")
                return 0
                
        elif (tokenList[0] == 'Short' or 'Int' or 'Long'):
            
            print(grabbertools.getNextNum(varinit))
            
            if (grabbertools.getNextNum(varinit) is not None):
                
                tokenList.append(tokens.Token(tokens.Var[tokenList[0]], 
                                                grabbertools.getNextNum(varinit)))
            else:
                
                print('Invalid value for ', tokenList[0], ' variable.')
        else:
            
            print('Invalid type.')
            return 0
    else:
        print("parseVarDec: Can't find varinit")
    
    return (tokenList)
