import re


class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __str__(self):
        return f"Token: {self.tipo}, lexema: {self.valor}"


class Lexer:
    def __init__(self, codigo):
        self.codigo = codigo
        self.posicion = 0

    def obtener_siguiente_token(self):
        if self.posicion == len(self.codigo):
            return Token("FIN", None)

        # Ignora los espacios en blanco
        while (self.posicion < len(self.codigo) and
               (self.codigo[self.posicion].isspace() or self.codigo[self.posicion] == ':' or self.codigo[self.posicion] == '\n')):
            self.posicion += 1

        # Coincidir con identificadores
        if re.match(r'[a-zA-Z¡]', self.codigo[self.posicion]):
            inicio = self.posicion
            while (self.posicion < len(self.codigo) and
                   re.match(r'[a-zA-Z0-9¡]', self.codigo[self.posicion])):
                self.posicion += 1
            valor = self.codigo[inicio:self.posicion]
            # Manejar palabras clave
            if valor == 'true' or valor == 'false':
                return Token("VALOR BOOLENO", valor == 'true')
            elif valor == 'fun':
                return Token("PALABRA RESERVADA FUNCION", valor)
            elif valor == 'return':
                return Token("PALABRA RESERVADA PARA RETORNAR", valor)
            elif valor == 'F':
                return Token("PALABRA RESERVADA DE FOR", valor)
            elif valor == '¡si':
                return Token("PALABRA RESERVADA SENTENCIA IF", valor)
            return Token("IDENTIFICADOR", valor)

        if self.codigo[self.posicion] == '=':
            self.posicion += 1
            return Token("ASIGNACION", '=')

        if re.match(r'\d', self.codigo[self.posicion]):
            inicio = self.posicion
            while (self.posicion < len(self.codigo) and
                   (re.match(r'\d', self.codigo[self.posicion]) or self.codigo[self.posicion] == '.')):
                self.posicion += 1
            valor = float(self.codigo[inicio:self.posicion])
            return Token("VALOR NUMERICO", valor)

        # Coincidir con valores booleanos
        if self.codigo.startswith('true', self.posicion):
            self.posicion += 4
            return Token("BOOLEANO", True)
        elif self.codigo.startswith('false', self.posicion):
            self.posicion += 5
            return Token("BOOLEANO", False)

        if self.codigo[self.posicion] == '*':
            inicio = self.posicion
            while (self.posicion < len(self.codigo) and
                   self.codigo[self.posicion] != '*'):
                self.posicion += 1
            if self.posicion < len(self.codigo) and self.codigo[self.posicion] == '*':
                self.posicion += 1
                valor = self.codigo[inicio + 1:self.posicion - 1]
                return Token("SIMBOLO_ESPECIAL", '*')

        if self.codigo[self.posicion] == '[':
            self.posicion += 1
            return Token("CORCHETE_IZQUIERDO", '[')
        elif self.codigo[self.posicion] == ']':
            self.posicion += 1
            return Token("CORCHETE_DERECHO", ']')
        elif self.codigo[self.posicion] == '{':
            self.posicion += 1
            return Token("LLAVE_IZQUIERDA", '{')
        elif self.codigo[self.posicion] == '}':
            self.posicion += 1
            return Token("LLAVE_DERECHA", '}')
        elif self.codigo[self.posicion:self.posicion + 2] == '=>':
            self.posicion += 2
            return Token("FLECHA", '=>')

        if self.codigo[self.posicion] == '(':
            self.posicion += 1
            return Token("PARENTESIS_IZQUIERDO", '(')
        elif self.codigo[self.posicion] == ')':
            self.posicion += 1
            return Token("PARENTESIS_DERECHO", ')')
        elif re.match(r'[a-zA-Z]', self.codigo[self.posicion]):
            inicio = self.posicion
            while (self.posicion < len(self.codigo) and
                   re.match(r'[a-zA-Z0-9]', self.codigo[self.posicion])):
                self.posicion += 1
            valor = self.codigo[inicio:self.posicion]
            return Token("L", valor)
        elif re.match(r'[<>=]=?', self.codigo[self.posicion:self.posicion + 2]):
            operador = self.codigo[self.posicion:self.posicion + 2]
            self.posicion += 2
            return Token("OPERADOR_COMPARACION", operador)
        elif self.codigo[self.posicion:self.posicion + 1] == ',':
            self.posicion += 1
            return Token("SIMBOLO_COMA", ',')
        elif self.codigo[self.posicion:self.posicion + 1] == '!':
            self.posicion += 1
            return Token("SIMBOLO_CIERRE SENTENCIA", '!')
        elif self.codigo[self.posicion:self.posicion + 2] == '++':
            self.posicion += 2
            return Token("INCREMENTO", '++')
        elif self.codigo[self.posicion:self.posicion + 2] == '--':
            self.posicion += 2
            return Token("DECREMENTO", '--')

        # Coincidir con la declaración de función y la palabra clave 'return'
        if self.codigo[self.posicion:self.posicion + 3] == 'fun':
            self.posicion += 3
            return Token("PALABRA_RESERVADA_FUNCIONES", 'fun')
        elif self.codigo[self.posicion:self.posicion + 6] == 'return':
            self.posicion += 6
            return Token("PALABRA_CLAVE_RETURN", 'return')

        if self.codigo[self.posicion:self.posicion + 2] == 'F(':
            inicio = self.posicion
            while (self.posicion < len(self.codigo) and
                   self.codigo[self.posicion] != ')'):
                self.posicion += 1
            if self.posicion < len(self.codigo) and self.codigo[self.posicion] == ')':
                self.posicion += 1
                valor = self.codigo[inicio:self.posicion]
                return Token("FUNCION_F", valor)

        if self.posicion < len(self.codigo):
            lexema_no_reconocido = self.codigo[self.posicion]
            self.posicion += 1
            return Token("LEXEMA_NO_RECONOCIDO", lexema_no_reconocido)

        #ignora otros caracteres inesperados
        self.posicion += 1
        return self.obtener_siguiente_token()
