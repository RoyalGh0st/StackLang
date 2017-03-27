# This file contains the token constants and class
# It also contains prebuilt tokens themselves
# But only tokens that have defined values

###########################
# Miscallaneous Constants #
###########################
NUM, STR = 'NUM', 'STR'
PLUS, MINUS = 'PLUS', 'MINUS'
TIMES, DIVIDE = 'TIMES', 'DIVIDE'
RBRACE, LBRACE = 'RBRACE', 'LBRACE'
WHITESPACE = 'WHITESPACE'
UNDEF_CHAR = 'UNDEF_CHAR'
UNDEF_WORD = 'UNDEF_WORD'
LETTER = 'LETTER'
ASSIGN = 'ASSIGN'
END_OF_STATEMENT = 'END_OF_STATEMENT'
COLON = 'COLON'
SINGLE_QUOTE, DOUBLE_QUOTE = 'SINGLE_QUOTE', 'DOUBLE_QUOTE'

Misc = {
    'num': NUM,
    'str': STR,
    'PLUS': PLUS,
    'MINUS': MINUS,
    'TIMES': TIMES,
    'DIVIDE': DIVIDE,
    'WHITESPACE': WHITESPACE,
    'UNDEF_WORD': UNDEF_WORD,
    'ASSIGN': ASSIGN,
    'END_OF_STATEMENT': END_OF_STATEMENT
}

#####################
# Logical constants #
#####################
EQUAL_TO = 'EQUAL_TO' # Symbol: ==
NOT_EQUAL = 'NOT_EQUAL' # Symbol: !=
IF = 'IF'
ELIF, ELSE = 'ELIF', 'ELSE'
TRUE, FALSE = 'TRUE', 'FALSE'
OR = 'OR' # Symbol: ||
AND = 'AND' # Symbol: &&
SMALLER_EQUAL = 'SMALLER_EQUAL'
GREATER_EQUAL = 'LARGER_EQUAL'
SMALLER = 'SMALLER'
GREATER = 'GREATER'

Logic = {
    'EQUAL_TO': EQUAL_TO,
    'NOT_EQUAL': NOT_EQUAL,
    'if': IF,
    'elif': ELIF,
    'else': ELSE,
    'true': TRUE,
    'false': FALSE,
    'or': OR,
    'and': AND
}

##################################################
# Variable types and modifiers                   #
# Also basically everything to do with variables #
##################################################
# Types:
NUM, STR = 'NUM', 'STR' # num just grows in memory space if it is needed
CHAR = 'CHAR'
SHORT, INT, LONG = 'SHORT', 'INT', 'LONG'
FLOAT, DOUBLE = 'FLOAT', 'DOUBLE'

# Modifiers:
IMMUTABLE = 'IMMUTABLE'
VOLATILE = 'VOLATILE'
INTERNAL = 'INTERNAL'
EXTERNAL = 'EXTERNAL'
STATIC = 'STATIC'

# Constants for parsing
VAR_NAME = 'VAR_NAME'

Var = {
    'Short': SHORT,
    'Int': INT,
    'Long': LONG,
    'Float': FLOAT,
    'Double': DOUBLE,
    'Immutable': IMMUTABLE,
    'Volatile': VOLATILE,
    'Internal': INTERNAL,
    'External': EXTERNAL,
    'Static': STATIC
}

Keywords = {
    'short': SHORT,
    'int': INT,
    'long': LONG,
    'float': FLOAT,
    'double': DOUBLE,
    'Immutable': IMMUTABLE,
    'Volatile': VOLATILE,
    'Internal': INTERNAL,
    'External': EXTERNAL,
    'Static': STATIC,
    'if': IF,
    'elif': ELIF,
    'else': ELSE,
    'true': TRUE,
    'false': FALSE,
    'or': OR,
    'and': AND,
    'num': 'NUM',
    'str': 'STR'
}

KeySequences = {
    '||': OR,
    '&&': AND,
    '<=': SMALLER_EQUAL,
    '==': EQUAL_TO,
    '>=': GREATER_EQUAL,
    '<': SMALLER,
    '>': GREATER,
    '=': ASSIGN,
    ';': END_OF_STATEMENT,
    ':': COLON,
    "'": SINGLE_QUOTE,
    '"': DOUBLE_QUOTE,
    '+': PLUS,
    '-': MINUS,
    '*': TIMES,
    '/': DIVIDE
}

# Token class
class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
