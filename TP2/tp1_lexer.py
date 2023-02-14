import ply.lex as lex
import sys

tokens = [

    # (Identifier, int)
    'ID','NINT',

    #Operators(+,-,*,/,%, <, ==, &&, or, <, <=, >, >=, !=)
    'PLUS','MINUS','MULT','DIV','MOD', 'EQEQ',
    'AND', 'OR', 'LT', 'LE', 'GT', 'GE', 'NEQ',

    #Assign(=, ++, --, +=, -=, *=, /=, %=)
    'ASSIGN', 'PLUSPLUS', 'MINUSMINUS', 'PLUSEQ','MINUSEQ', 'MULTEQ','DIVEQ','MODEQ',

    #Words 
    'FUNCTIONS','DECLARATIONS','BEGIN','WRITE','READ','IF'
    ,'THEN','ELSE','END','PHRASE', 'IntWord','WHILE','ArrayInt','FOR',
    'DEF','FUNC_NAME','RETURN',

    # Delimeters ( ) [ ] { } , ;
    'LROUND','RROUND','LSQUARE','RSQUARE',
    'LCURLY','RCURLY', 'VIR','PONTeVIR', 'DOLLAR'
]

#Operators(+,-,*,/,%, <, ==, &&, ||, <, <=, >, >=, !=)
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_EQEQ = r'=='
t_AND = r'&&'
t_OR = r'\|\|'
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_NEQ = r'!='

#Assign(=, ++, +=, -=, *=, /=, %=)
t_ASSIGN = r'='
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'
t_PLUSEQ = r'\+\='
t_MINUSEQ = r'\-\='
t_MULTEQ = r'\*\='
t_DIVEQ = r'\/\='
t_MODEQ = r'\%\='

# Delimeters ( ) [ ] { } , ; :
t_LROUND = r'\('
t_RROUND = r'\)'
t_LSQUARE = r'\['
t_RSQUARE = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_PONTeVIR = r';'
t_VIR = r','
t_DOLLAR = r'\$'


def t_BEGIN(t):
    r'(?i:begin)'
    return t

def t_WRITE(t):
    r'(?i:write)'
    return t

def t_READ(t):
    r'(?i:read)'
    return t

def t_DECLARATIONS(t):
    r'(?i:declarations)'
    return t

def t_IntWord(t):
    r'(?i:int)'
    return t

def t_ArrayInt(t):
    r'(?i:arrayint)'
    return t

def t_IF(t):
    r'(?i:if)'
    return t

def t_THEN(t):
    r'(?i:then)'
    return t

def t_ELSE(t):
    r'(?i:else)'
    return t

def t_END(t):
    r'(?i:end)'
    return t

def t_PHRASE(t):
    r'\"[a-zA-Z0-9 =:,\"\n]+'
    return t

def t_FUNC_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*\(\)'
    return t

def t_WHILE(t):
    r'(?i:while)'
    return t

def t_FOR(t):
    r'(?i:for)'
    return t

def t_FUNCTIONS(t):
    r'(?i:functions)'
    return t

def t_RETURN(t):
    r'(?i:return)'
    return t

def t_DEF(t):
    r'(?i:def)'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NINT(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'\#.*'
    pass


t_ignore = ' \r\n\t'

def t_error(t):
    print('Illegal character: ' + t.value[0])
    t.lexer.skip(1)
    return

lexer = lex.lex() 

