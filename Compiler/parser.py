# Contains token class and constants
import Tokens

# Contains tools used during parsing
import parseTools

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class Parser(object):
    def __init__(self, text):
        self.text = text
        # Index onto text
        self.index = 0
        # The token list that is returned
        self.tokenList = [None]
        # Position on tokenList
        self.tokenListPos = 0
        
    def getBlock(self, text):
        
        ''' This function finds the next block from text input. '''
        recordBlock = False
        # This is so a block can contain other blocks.
        currentBlockCount = 0
        # Index onto the text
        index = 0
        
        block = ""
        
        while (True):
            if (text[index] == '{'):
                if (currentBlockCount == 0):
                    recordBlock = True
                currentBlockCount += 1
                
            if (recordBlock == True):
                block = block + text[index]
                
            if (text[index] == '}'):
                currentBlockCount -= 1
                if (currentBlockCount == 0):
                    recordBlock = False
                    break
                
            index += 1
        
        block += '}'
        
        return(block)
    
    def skipWhitespace(self, text):
        """ This function actually returns the amount of whitespace, not the text
            without whitespace. Counterintuitive, but it needs to be this way, because of the way
            other functions are designed."""
        counter = 0
        pos = 0
        while (text[pos] == ' ' or text[pos] == '\n' or text[pos] == '\t'):
            counter += 1
            pos += 1
            
        return counter
        
        
    def Parse(self, text, *args):
        ''' Actual parser that constructs an AST made of lists. '''
        tokenList = []
        # Block for recursive parsing
        block = ''
        # Index onto text
        pos = 0
        # Second index, for iterating without affecting parse position
        pos2 = 0
        # This is for parsing words in
        word = ""
        
        while (pos < len(text)):
            currentChar = text[pos]
            
            #print(pos, ',', len(text), end='\n\n')
            
            if (currentChar == '{'):
                try:
                    block = self.getBlock(text[pos:])
                except IndexError:
                    # IndexError is recieved when the block tokens are unbalanced.
                    raise Exception("Invalid syntax: unbalanced block tokens.")
                    
                # We just assume that the getBlock call succeded
                # Because if not, an error has been generated
                # Slice off the '{' and '}' from the block
                block = block[1:-1]
                
                # Skip past the block, since it's being parsed already, and we
                # don't want that to happen twice
                pos += len(block) + 1
                # Recursively call parse
                tokenList.append(self.Parse(block))
            
            elif (currentChar == '}'):
                return(tokenList)
                
            elif (isNumber(currentChar)):
                # This converts a string of number characters
                # into an actual number
                # A float
                number = currentChar
                pos2 = pos + 1
                while (isNumber(text[pos2])):
                    number += text[pos2]
                    pos2 += 1
                    
                tokenList.append(Tokens.Token(Tokens.Misc['NUM'], float(number)))
                pos = pos2
                
            elif (currentChar == '='):
                tokenList.append(Tokens.Token(Tokens.Misc['ASSIGN'], currentChar))
                pos += 1
                
            else:
                if wordTools.getNextWord(text[pos:]) is not None:
                    word = wordTools.getNextWord(text[pos:])
                    
                    if (wordTools.isKeyWord(word) != False):
                        
                        if (word != 'if' or 'else' or 'elif' or 'true' or 'false'
                            or 'or' or 'and'):
                            word2 = wordTools.getNextWord(text[pos+len(wordTools.getNextWord(text[pos:])):])
                            tokenList.append(Tokens.Token(Tokens.Keywords[word], word2))
                        else:
                            tokenList.append(Tokens.Token(Tokens.Keywords[word], word))
                        
                    else:
                        tokenList.append(Tokens.Token(Tokens.Misc['UNDEF_WORD'], word))
                        
                    pos += len(word) + 1
                elif wordTools.getNextKeySequence(text[pos:]) is not None:
                    seq = wordTools.getNextKeySequence(text[pos:])
                    
                    tokenList.append(Tokens.Token(Tokens.KeySequences[seq], seq))
                    
                    pos += len(seq)
                
        return(tokenList)
        
def printNestedTLists(li):
    for item in li:
        if (type(item) == list):
            print('{')
            printNestedTLists(item)
            print('}')
        else:
            print(item.type, ':', item.value)
    
def main():
    parser = Parser(input("Enter test case: "))
    print(parser.text, end='\n\n')
    parser.tokenList = parser.Parse(parser.text)
    print(' ', end='\n\n')
    printNestedTLists(parser.tokenList)
    
    
main()
