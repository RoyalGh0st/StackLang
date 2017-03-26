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
    # At the moment, just mathematical operators
    # And semicolons
    getseq = re.compile('''(^[\\+|\\-|\\*|/|;)''')
    # ^^ gets all the key sequences
    seq = getseq.match(text)
    if seq is not None:
        seqindex = seq.span()
    else:
        return None
    
    seq = text[seqindex[0]:seqindex[1]]
    
    return(seq)

def isVarKeyWord(word):
    if (word == 'char'):
        return word
    elif (word == 'str'):
        return word
    elif (word == 'short'):
        return word
    elif (word == 'int'):
        return word
    elif (word == 'long'):
        return word
    else:
        return False
