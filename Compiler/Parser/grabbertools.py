'''
####################################################################################
# This file contains all of the regex functions specially tailored for the parser. #
# Functions like "getKeyWord", "getNextWord", and others.                          #
####################################################################################
'''

import tokens
import grabbertools

# The regex library
import re


def getNextWord(text):
    # This function grabs the next word from input text
    # And returns it
    getword = re.compile('^[a-zA-Z_]+') # Gets the next word from the input
    word = getword.match(text)
    if word is not None:
        wordindex = word.span()
    else:
        return None
    
    word = text[wordindex[0]:wordindex[1]]
    
    return (word)
# end getNextWord

def getNextNum(text):
    # Grabs the next set of numbers from the text
    # i.e. 24988 or 192498
    # Regex was not used for this because I couldn't get it to work
    num = ''
    pos = 0
    record = False
    
    while pos < len(text):
        currentchar = text[pos]
        
        if currentchar.isdigit() == False:
            record = False
        
        if currentchar.isdigit() == True:
            record = True
        
        if currentchar.isdigit() == False and record == True:
            break
        
        if record == True:
            num += currentchar
            
        pos += 1
    
    if num is not '':
        num = float(num)
    else:
        return None
    
    return (num)
    
def getNextChar(text):
    # Grabs the next character type from text
    # i.e. 'x' or 'z', but not "x" or "z" or "foobar"
    # Again, no regex, because regex annoys me for this kind of thing
    c = ''
    pos = 0
    record = False
    
    while (pos < len(text)):
        currentc = text[pos]
        
        if currentc == "'":
            c = text[pos+1]
            return c
        pos += 1

def getNextKeySeq(text):
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

def getNextVarDec(text):
    # Gets the next variable declaration from the text
    # See /docs/specs/statements.txt for more details on what a statement is
    # Regex annoyed me, so I didn't use it for this one
    print('\ncalled vdec on: ', text)
    
    getvdec = re.compile('''(((char)|(str)|(short)|(int)|(long)) \w( ?= ?(('\w')|("\w*")|(\d*))?));''')
    vdec = getvdec.match(text)
    
    if vdec is not None:
        vdecindex = vdec.span()
    else:
        print('vdec returns: None')
        return None
        
    vdec = text[vdecindex[0]:vdecindex[1]]
    
    print('vdec returns: ', vdec)
    
    return vdec
    
def getNextVarInit(text):
    # Gets the next initialization of a variable from the text
    
    getvarinit = re.compile(' *= *.+;')
    varinit = getvarinit.match(text)
    
    if varinit is not None:
        varinitindex = varinit.span()
    else:
        return None
    
    varinit = text[varinitindex[0]:varinitindex[1]]
    
    return varinit
    
