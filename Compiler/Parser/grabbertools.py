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
    # Grabs the next char type from text
    # i.e. 'x' or 'z' or even 'abc' (but that's error checked in parseVarDec) 
    # but not "x" or "z" or "foobar"
    # Regex would not work here
    # So I didn't use it.
    char = ''
    pos = 0
    currentc = ''
    record = ''
    
    while (pos < len(text)):
        currentc = text[pos]
        
        if (currentc == "'"):
            char = text[pos+1]
            if (text[pos+2] is not "'"):
                return None
            break
            
        pos += 1
    
    return char
        
def getNextStr(text):
    # Grabs the next str type from text
    # i.e. "abc" or "d"
    # Regex didn't work here
    # Or maybe I'm just bad at it
    # Whichever
    pos = 0
    Str = ''
    currentc = ''
    record = False
    
    while (pos < len(text)):
        currentc = text[pos]
        
        if (currentc == '"'):
            if record == True:
                break
            else:
                record = True
        
        if record == True:
            Str += currentc
            
        pos += 1
        
    # That little bit is there because the function kept recording " as the first character
    # And I couldn't figure out why
    if (Str[0] == '"'):
        Str = Str[1:]
    
    return Str

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
    
    getvdec = re.compile('''(((char)|(str)|(short)|(int)|(long)) \w( ?= ?(('\w*')|("\w*")|(\d*))?));''')
    vdec = getvdec.match(text)
    
    if vdec is not None:
        vdecindex = vdec.span()
    else:
        return None
        
    vdec = text[vdecindex[0]:vdecindex[1]]
    
    return vdec
    
def getNextVarInit(text):
    # Gets the next initialization of a variable from the text
    
    getvarinit = re.compile('( *= *.+;)+?')
    varinit = getvarinit.match(text)
    
    if varinit is not None:
        varinitindex = varinit.span()
    else:
        return None
    
    varinit = text[varinitindex[0]:varinitindex[1]]
    
    return varinit
    
    
def getNextSimpleState(text):
    # Gets the next simple statement from the text
    
    pos = 0
    
    getstate = re.compile('''
    (((\+\+|\-\-)?(\w+|\d+) ?(\+|\-|\*|/|=) ?)+) ?(\w+|\d+);
    ''')
    
    state = getstate.match(text)
    
    if state is not None:
        state = text[state.span()[0]:state.span()[1]]
    else:
        return None
    
    return state
    
