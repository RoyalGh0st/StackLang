import tokenizer
from tokenizer import Tokenizer

class Driver(object):
    def __init__(self, text):
        self.text = text
        # These are for math expressions.
        self.mathLRegister = 0
        self.mathRRegister = 0
        # The tokenizer
        self.tokenizer = Tokenizer()
        # Stack selectors
        self.currentStack = 0
        self.currentSlot = 0
        # Actual stacks
        self.Stacks = [[0 for x in range(3)] for y in range[50]
        
    def ConvertTokensToInt(self, posTokenList):
        val = 0
        total = 0
        currentNumIndex = 0
        Number = [self.tokenizer.tokenList[posTokenList].value]
        if (self.tokenizer.tokenList[posTokenList+1].type == tokenizer.INTEGER):
            val = self.tokenizer.tokenList[posTokenList+1].value
            currentNumIndex += 1
            Number.append(currentNumIndex, val)
            
            if (self.tokenizer.tokenList[posTokenList+2].type == tokenizer.INTEGER):
                val = self.tokenizer.tokenList[posTokenList+2].value
                currentNumIndex += 1
                Number.append(currentNumIndex, val)
                
                if (self.tokenizer.tokenList[posTokenList+3].type == tokenizer.INTEGER):
                    val = self.tokenizer.tokenList[posTokenList+3].value
                    currentNumIndex += 1
                    Number.append(currentNumIndex, val)
                    
                    if (self.tokenizer.tokenList[posTokenList+4].type == tokenizer.INTEGER):
                        val = self.tokenizer.tokenList[posTokenList+4].value
                        currentNumIndex += 1
                        Number.append(currentNumIndex, val)
                        
                        if (self.tokenizer.tokenList[posTokenList+5].type == tokenizer.INTEGER):
                            val = self.tokenizer.tokenList[posTokenList+5].value
                            currentNumIndex += 1
                            Number.append(currentNumIndex, val)
                            
                            if (self.tokenizer.tokenList[posTokenList+6].type == tokenizer.INTEGER):
                                val = self.tokenizer.tokenList[posTokenList+6].value
                                currentNumIndex += 1
                                Number.append(currentNumIndex, val)
                                
                                if (self.tokenizer.tokenList[posTokenList+7].type == tokenizer.INTEGER):
                                    val = self.tokenizer.tokenList[posTokenList+7].value
                                    currentNumIndex += 1
                                    Number.append(currentNumIndex, val)
                                    
                                    if (self.tokenizer.tokenList[posTokenList+8].type == tokenizer.INTEGER):
                                        val = self.tokenizer.tokenList[posTokenList+8].value
                                        currentNumIndes += 1
                                        Number.append(currentNumIndex, val)
        else:
            Number[currentNumIndex] = self.tokenizer.tokenList[posTokenList].value
            
        for num in Number:
            total += num
            
        return total
    
    # End of ConvertTokensToInt
    
    def stackAccess(stackNum, slotNum):
        self.currentStack = stackNum
        self.currentSlot = slotNum
        
    def assign(stack, slot, value):
        self.Stacks[stack][slot] = value
        
