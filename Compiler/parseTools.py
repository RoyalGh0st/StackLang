'''
####################################################################################
# This file contains all of the regex functions specially tailored for the parser. #
# Functions like "getKeyWord", "getNextWord", and others.                          #
####################################################################################
'''

import Tokens

# The regex library
import re

def getNextWord(text):
    # This function grabs the next word from input text
    # And returns it
    getword = re.compile('^[\w]+') # Gets the next word from the input
    word = getword.match(text)
    if word is not None:
        wordindex = word.span()
    else:
        return None
    
    word = text[wordindex[0]:wordindex[1]]
    
    return (word)
# end getNextWord

def getNextKeySequence(text):
    # This function grabs the next key sequence from input text
    getseq = re.compile('''(^[(\\|\\|)|(&&)|(==)|(!=)|(>=)|(<=)|(/\\*)|(\\*/)|(//)]{2})|(^[=|<|>|\\.|\\'|"|;|:|,|+|-|*])''')
    # ^^ gets all the key sequences
    seq = getseq.match(text)
    if seq is not None:
        seqindex = seq.span()
    else:
        return None
    
    seq = text[seqindex[0]:seqindex[1]]
    
    return(seq)

def isKeyWord(word):
    # The name here might be a bit misleading
    # The function checks if the word input is a key word
    # And if so, return the corresponding token constant
    if (word == 'if'):
        return (Tokens.IF)
    elif (word == 'else'):
        return (Tokens.ELSE)
    elif (word == 'elif'):
        return (Tokens.ELIF)
    elif (word == 'short'):
        return(Tokens.SHORT)
    elif (word == 'int'):
        return (Tokens.INT)
    elif (word == 'long'):
        return (Tokens.LONG)
    elif (word == 'float'):
        return (Tokens.FLOAT)
    elif (word == 'double'):
        return (Tokens.DOUBLE)
    elif (word == 'true'):
        return (Tokens.TRUE)
    elif (word == 'false'):
        return (Tokens.FALSE)
    else:
        return False
