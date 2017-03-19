''' This file contains the Token class and all of the tokens + constants. '''

''' Variable constants/prefixes/keywords '''
NUM, STR = 'NUM', 'STR' # Num is the generic number type, can hold any length. Str is just a string.
INT, LONG = 'INT', 'LONG'
FLOAT, DOUBLE = 'FLOAT', 'DOUBLE'
CHAR = 'CHAR'
BOOL = 'BOOL'
VOID, NULL = 'NULL' # Something interesting: they both compile down to Null, so they are the same thing.
IMMUTABLE = 'IMMUTABLE'

''' Logical constants. '''
TRUE, FALSE = 'TRUE', 'FALSE'
OR, AND = 'OR', 'AND'
LESS_EQUALTO, GREATER_EQUALTO = 'LESS_EQUALTO', 'GREATER_EQUALTO'
IF, ELIF, ELSE = 'IF', 'ELIF', 'ELSE'
WHILE, WHILE_NOT = 'WHILE', 'WHILE_NOT'
FOR = 'FOR'
EQUAL_TO = 'EQUALTO' # Equal to is '=='
NOT_EQUAL_TO = 'NOT_EQUAL_TO'
IS, IS_NOT = 'IS', 'IS_NOT' # Check if the memory addresses are the same

''' Creation keywords '''
N_OBJECT = 'N_OBJECT'
N_CLASS = 'N_CLASS'
NEW = 'NEW'

''' Object environment constants '''
CHANNEL_ = 'CHANNEL'
PORT_ = 'PORT'

''' Key characters/sequences '''
L_PAREN, R_PAREN = 'L_PAREN', 'R_PAREN'
L_BRACE, R_BRACE = 'L_BRACE', 'R_BRACE'
L_BRACKET, R_BRACKET = 'L_BRACKET', 'R_BRACKET'
L_ANGLEBRACE, R_ANGLEBRACE = 'L_ANGLEBRACE', 'R_ANGLEBRACE' # The angle braces are '<' and '>'
UP_ARROWHEAD = 'UP_ARROWHEAD' # Up arrowhead is '^'
PLUS, MINUS = 'PLUS', 'MINUS'
TIMES, DIVIDE = 'TIMES', 'DIVIDE'
PIPE = 'PIPE' # Is '|'
BACKSLASH = 'BACKSLASH'
SLASH = 'SLASH'
TILDE = 'TILDE'
SEMICOLON = 'SEMICOLON'
MODULO = 'MODULO'
COMMENT_BEGIN, COMMENT_END = 'COMMENT_BEGIN', 'COMMENT_END'

class Token(object):
  def __init__(self, type, value):
    self.type = type
    self.value = value
  
