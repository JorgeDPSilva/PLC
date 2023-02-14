
import ply.yacc as yacc

from tp1_lexer import tokens

# guardas as variaveis num dicionario
variables = {}
functions = []
countWHILE = 0
countFor = 0
countIF = 0


def p_LstPrograms_Program(p):
    '''
    LstPrograms : Program
    '''
    parser.file.write(p[1])

def p_LstPrograms_LstPrograms(p):
    '''
    LstPrograms : LstPrograms Program 
    '''
    p[0] = p[1] + p[2]

def p_Program(p):
    '''
    Program : DECLARATIONS LCURLY LstDecl RCURLY Fs BEGIN LstInst END
    '''
    p[0] = p[3] + "JUMP main\n" + p[5] + "main: nop\n" + p[7] + "STOP"

#
## 
## DECLARATIONS -------------------------------------
##
#

def p_LstDecl_Decl(p):
    '''
    LstDecl : Decl
    '''
    p[0] = p[1] + "START\n"

def p_LstDecl_LstDecl(p):
    '''
    LstDecl : Decl LstDecl
    '''
    p[0] = p[1] + p[2]


def p_Decl_Int(p):
    '''
    Decl : IntWord Variables PONTeVIR
    '''
    p[0] = p[2]

def p_Decl_ArrayInt(p):
    '''
    Decl : ArrayInt Variables PONTeVIR
    '''
    p[0] = p[2]


#
#
#

def p_Variables_LstVar(p):
    '''
    Variables : Var VIR Variables
    '''
    p[0] = p[1] + p[3]


def p_Variables_Var(p):
    '''
    Variables : Var     
    '''
    p[0] = p[1]


def p_Var_ID(p):
    '''
    Var : ID
    '''
    p[0] = "PUSHI 0\n"
    variables[p[1]] = -1

def p_Var_Array(p):
    '''
    Var : ID LSQUARE NINT RSQUARE
    '''
    p[0] = "PUSHN " + str(p[3]) + "\n"
    variables[p[1]] = [-1] * p[3]

#
##-----------------------------------------

def p_Fs_Empty(p):
   '''
   Fs : 
   '''
   p[0] = ""

def p_Fs_LstFuntc(p):
    '''
    Fs : FUNCTIONS DOLLAR LstFunct DOLLAR
    '''
    p[0] = p[3]

def p_LstFunct_Func(p):
    '''
    LstFunct : Func
    '''
    p[0] = p[1]

def p_LstFunct_Recursive(p):
    '''
    LstFunct : LstFunct Func
    '''
    p[0] = p[1] + p[2]

def p_Func(p):
    '''
    Func : DEF FUNC_NAME LCURLY LstInst RETURN ID PONTeVIR RCURLY 
    '''
    x = p[2]
    x = x[:len(x) - 2]

    if x not in functions:
        functions.append(x)
        p[0] = x + ": nop\n" + p[4] + p[5].upper() + "\n" + "ret: nop" + "\n" + "PUSHG " + f"{get_indexVar(p[6])}\n" + "JUMP endret\n"
    else:
        p[0] = f"ERR 'A funcao {x} ja esta definida.'\nSTOP\n"

##-----------------------------------------

#
# Lista de instruções de cada programa
#

def p_LstInst_Instruction(p):
    '''
    LstInst : Instruction
    '''
    p[0] = p[1]

def p_LstInst_Recursive(p):
    '''
    LstInst : LstInst Instruction
    '''
    p[0] = p[1] + p[2]


#
# Instruction - atribuição, função ou if
#
def p_Instruction(p):
   '''
   Instruction : Atrib
               | Function
               | ifStatement
               | Loop
   '''
   p[0] = p[1]

#
# Loop - Ciclo for, while, while do, repeat-until 
#

def p_Loop(p):
    '''
    Loop : WHILE LROUND Condition RROUND LCURLY LstInst RCURLY
         | FOR LROUND Atrib Atrib Condition RROUND LCURLY LstInst RCURLY

    '''
    if p[1].upper() == "WHILE":
        parser.countWHILE += 1
        p[0] = "WHILE" + str(parser.countWHILE) + ":\n" + p[3] + "JZ ENDWHILE" + str(parser.countWHILE) + "\n" + p[6] + "JUMP WHILE" + str(parser.countWHILE) + "\nENDWHILE" + str(parser.countWHILE) + ":\n" 
    
    elif p[1].upper() == "FOR":
        parser.countFor += 1
        p[0] =  p[3] + "FOR" + str(parser.countFor) + ":\n" + p[5] + "JZ ENDFOR" + str(parser.countFor) + "\n" + p[8] + p[4]+ "JUMP FOR" + str(parser.countFor) + "\nENDFOR" + str(parser.countFor) + ":\n"


#
# ifStatement - if then else, if then
#

def p_ifStatementThen(p):
    '''
    ifStatement : IF LROUND Condition RROUND THEN LCURLY LstInst RCURLY
    '''
    parser.countIF += 1
    p[0] = p[3] + "JZ FIM" + str(parser.countIF) + "\n" + p[7] + "JUMP FIM" + str(parser.countIF) + "\n" + "FIM" + str(parser.countIF) + ":\n"


def p_ifStatement(p):
    '''
    ifStatement : IF LROUND Condition RROUND THEN LCURLY LstInst RCURLY ELSE LCURLY LstInst RCURLY
    '''
    parser.countIF += 1

    p[0] = p[3] + "JZ ELSE" + str(parser.countIF) + "\n" + p[7] + "JUMP FIM" + str(parser.countIF) + "\n" + "ELSE" + str(parser.countIF) + ":\n" + p[11] + "FIM" + str(parser.countIF) + ":\n"

#
# Atribuições "x = 4+5;"
# NOTA: mudar para só quando a variavel existe no dicionario
#

def p_Atrib(p):
    '''
    Atrib : ID ASSIGN Expr PONTeVIR
          | ID PLUSEQ Expr PONTeVIR
          | ID MINUSEQ Expr PONTeVIR
          | ID MULTEQ Expr PONTeVIR
          | ID DIVEQ Expr PONTeVIR
          | ID MODEQ Expr PONTeVIR
          | ID PLUSPLUS PONTeVIR
          | ID MINUSMINUS PONTeVIR
    '''
    if p[1] in variables:
        if p[2] == "=":
            p[0] = p[3] + "STOREG " + f"{get_indexVar(p[1])}\n"
        elif p[2] == "+=":
            p[0] = "PUSHG " + f"{get_indexVar(p[1])}\n" + p[3] + "ADD\n" + "STOREG " + f"{get_indexVar(p[1])}\n"
        elif p[2] == "-=":
            p[0] = "PUSHG " + f"{get_indexVar(p[1])}\n" + p[3] + "SUB\n" + "STOREG " + f"{get_indexVar(p[1])}\n"
        elif p[2] == "*=":
            p[0] = "PUSHG " + f"{get_indexVar(p[1])}\n" + p[3] + "MUL\n" + "STOREG " + f"{get_indexVar(p[1])}\n"
        elif p[2] == "/=":
            p[0] = "PUSHG " + f"{get_indexVar(p[1])}\n" + p[3] + "DIV\n" + "STOREG " + f"{get_indexVar(p[1])}\n"
        elif p[2] == "%=":
            p[0] = "PUSHG " + f"{get_indexVar(p[1])}\n" + p[3] + "MOD\n" + "STOREG " + f"{get_indexVar(p[1])}\n"
        elif p[2] == "++":
            p[0] = "PUSHG " + f"{get_indexVar(p[1])}\n" + "PUSHI 1\n" + "ADD\n" + "STOREG " + f"{get_indexVar(p[1])}\n"
        elif p[2] == '--':
            p[0] = "PUSHG " + f"{get_indexVar(p[1])}\n" + "PUSHI 1\n" + "SUB\n" + "STOREG " + f"{get_indexVar(p[1])}\n"
    else:
        p[0] = f"ERR 'A variável {p[1]} não existe'\nSTOP\n"


def p_Atrib_Array(p):
    '''
    Atrib : ID LSQUARE Expr RSQUARE ASSIGN ExprR PONTeVIR
    '''
    arrayindex = get_indexVar(p[1])
    p[0] = f"PUSHGP\nPUSHI {arrayindex}\n{p[3]}ADD\n{p[6]}STOREN\n" 
#
# Function - write and read function
#

def p_Function_WritePHRASE(p):
    '''
    Function : WRITE LROUND PHRASE RROUND PONTeVIR
    '''
    p[0] = "PUSHS " + p[3] + "\n" + "WRITES\n"


def p_Function_WriteExprR(p):
    '''
    Function : WRITE LROUND ExprR RROUND PONTeVIR
    '''
    p[0] = p[3] + "WRITEI\n"


#
# Condition - AND e OR
#

def p_Condition(p):
    '''Condition : ExprR'''
    p[0] = p[1]

def p_Condition_AND(p):
    '''Condition : ExprR AND Condition'''
    p[0] = p[1] + p[3] + "MUL\n"

def p_Condition_OR(p):
    '''Condition : ExprR OR Condition'''
    p[0] = p[1] + p[3] + "ADD\n"

#
# ExprR - operadores para comparacoes
#

def p_ExprR(p):
    '''ExprR : Expr'''
    p[0] = p[1]

# operador  == 
def p_ExprR_EQEQ(p):
    '''ExprR : Expr EQEQ Expr'''
    p[0] = p[1] + p[3] + "EQUAL\n"

def p_ExprR_NOTEQ(p):
    '''ExprR : Expr NEQ Expr'''
    p[0] = p[1] + p[3] + "EQUAL\n"
    
# operador  <
def p_ExprR_LT(p):
    '''ExprR : Expr LT Expr'''
    p[0] = p[1] + p[3] + "INF\n"


# operador  <=
def p_ExprR_LE(p):
    '''ExprR : Expr LE Expr'''
    p[0] = p[1] + p[3] + "INFEQ\n"


# operador  >
def p_ExprR_GT(p):
    '''ExprR : Expr GT Expr'''
    p[0] = p[1] + p[3] + "SUP\n"

# operador  >=
def p_ExprR_GE(p):
    '''ExprR : Expr GE Expr'''
    p[0] = p[1] + p[3] + "SUPEQ\n"
    

#
# Expr - Soma e subtracao
#

def p_Expr_Term(p):
    '''Expr : Term'''
    p[0] = p[1]


def p_Expr_PLUS(p):
    '''Expr : Expr PLUS Term'''
    p[0] = p[1] + p[3] + "ADD\n"


def p_Expr_MINUS(p):
    '''Expr : Expr MINUS Term'''
    p[0] = p[1] + p[3] + "SUB\n"


#
# Term - faz multiplcacoes, divisoes e modulos
#

def p_Term(p):
    '''Term : Factor'''
    p[0] = p[1]

def p_Term_Mult(p):
    '''Term : Term MULT Factor'''
    p[0] = p[1] + p[3] + "MUL\n"

    
def p_Term_Div(p):
    '''Term : Term DIV Factor'''
    p[0] = p[1] + p[3] + "DIV\n"


def p_Term_MOD(p):
    '''Term : Term MOD Factor'''
    p[0] = p[1] + p[3] + "MOD\n"


#
# Factor - deteta um inteiro, uma variavel
#

# PUSHG "index da variavel no dic variables"
def p_Factor_ID(p):
    '''Factor : ID'''
    if p[1] not in variables:
        p[0] = f"ERR 'Variavel {p[1]} não existe'\nSTOP\n"
    else:
        p[0] = f"PUSHG {get_indexVar(p[1])}\n"
        
def p_Factor_NINT(p):
    '''Factor : NINT'''
    p[0] = "PUSHI " + str(p[1]) + '\n'

def p_Factor_MinusNint(p):
    '''Factor : LROUND MINUS NINT RROUND'''
    x = -1 * p[3]
    p[0] = "PUSHI " + str(x) + '\n'

def p_FactorRead(p):
    '''
    Factor : READ LROUND RROUND
    '''
    p[0] = "READ\n" + "ATOI\n"

def p_FactorFunc(p):
    '''
    Factor : FUNC_NAME
    '''
    x = p[1]
    x = x[:len(x) - 2]
    p[0] = "PUSHA " + x + "\n" + "CALL\n" + "nop\n" + "JUMP ret\n" + "endret: nop\n"

def p_FactorArray(p):
    '''
    Factor : ID LSQUARE NINT RSQUARE
    '''
    if p[1] not in variables.keys():
        p[0] = f"ERR 'Variavel {p[1]} não existe'\nSTOP\n"
    else:
        x = p[3]
        if len(variables[p[1]]) > int(x) and int(x) >= 0:
            p[0] = "PUSHG " + p[3] + f"{get_indexVar(p[1]) + int(x)}\n"
        elif len(variables[p[1]]) <= int(x):
            p[0] = f"ERR 'O valor {p[3]} maior que o tamanho do array {p[1]}. '\nSTOP\n"
        elif int(x) < 0:
            p[0] = f"ERR 'O valor {p[3]} nao pode ser negativo. '\nSTOP\n"
        
def p_FactorArrayID(p):
    '''
    Factor : ID LSQUARE ID RSQUARE
    '''
    if p[1] not in variables.keys():
        p[0] = f"ERR 'Variavel {p[1]} não existe'\nSTOP\n"
    else:
        x = get_indexVar(p[3])
        if (get_indexVar(p[1]) < x):
            x += len(variables[p[1]]) - 1

        if len(variables[p[1]]) >= int(x) and int(x) >= 0:
            p[0] = "PUSHG " + f"{get_indexVar(p[1]) + int(x)}\n"
        elif len(variables[p[1]]) < int(x):
            p[0] = f"ERR 'O valor {p[3]} maior que o tamanho do array {p[1]}. '\nSTOP\n"
        elif int(x) < 0:
            p[0] = f"ERR 'O valor {p[3]} nao pode ser negativo. '\nSTOP\n"

def p_error(p):
    parser.success = False
    print('Syntax error!')


def get_indexVar(id):
    count  = 0
    for key in variables.keys():
        if key == id:
            return count
        else: 
            count+=1


###inicio do parsing
parser = yacc.yacc()
parser.countWHILE = 0
parser.countFor = 0
parser.countIF = 0
parser.success = True



