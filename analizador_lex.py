import ply.lex as lex
from ply.lex import LexError

tokens = [
    'Palabra_reservada_For', 'Palabra_reservada_Funcion', 'Valor_booleano', 'Palabra_reservada_sentencia_if',
    'Identificador', 'ASIGNACION', 'String', 'Valor_numerico', 'Simbolo_cierre_de_sentencia', 'PARENTESIS_izquierdo',
    'PARENTESIS_derecho', 'LLAVE_izquierda', 'LLAVE_derecha', 'Operador_comparacion', 'Palabra_reservada_para_retorno',
    'COMA', 'Corchete_izquierdo', 'Corchete_derecho', 'Simbolo_especial', 'Incremento', 'Decremento', 'NUEVA_LINEA'
]

#Reglas
t_ASIGNACION = r'='
t_Simbolo_cierre_de_sentencia = r'\!'
t_PARENTESIS_izquierdo = r'\('
t_PARENTESIS_derecho = r'\)'
t_LLAVE_izquierda = r'\{'
t_LLAVE_derecha = r'\}'
t_Operador_comparacion = r'==|<=|>=|<|>'
t_COMA = r','
t_Corchete_izquierdo = r'\['
t_Corchete_derecho = r'\]'
t_Simbolo_especial = r'\*'
t_Incremento = r'\+\+'
t_Decremento = r'--'


def t_Palabra_reservada_For(t):
    r'F'
    return t

def t_Palabra_reservada_sentencia_if(t):
    r'¡si'
    return t

def t_Palabra_reservada_Funcion(t):
    r'fun'
    return t

def t_Palabra_reservada_para_retorno(t):
    r'return'
    return t


def t_Identificador(t):
    r'[a-z]+'
    lower_value = t.value.lower()
    if lower_value == 'F':
        t.type = 'Palabra_reservada_For'
    elif lower_value == '¡si':
        t.type = 'Palabra_reservada_sentencia_if'
    elif lower_value == 'fun':
        t.type = 'Palabra_reservada_Funcion'
    elif lower_value == 'return':
        t.type = 'Palabra_reservada_para_retorno'
    elif lower_value == 'true' or lower_value == 'false':
        t.type = "Valor_booleano"
    return t



def t_Valor_booleano(t):
    r'true|false'
    return t


def t_String(t):
    r'\*[a-z0-9 ]*\*'
    return t


def t_Valor_numerico(t):
    r'-?\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_NUEVA_LINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    pass

t_ignore = ' \t'

# Función para manejar errores en el lexer
def t_error(t):
    error_message = f"Lexema no reconocido"
    print(error_message)
    t.lexer.skip(1)

lexer = lex.lex()