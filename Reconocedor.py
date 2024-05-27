import Clasificador
from Token import Token
class reconocedor():
    def __init__(self):
        self.pila_estructuras=[]
        self.lista_tokens=[]
        self.lista_errores=[]
        self.lista_estructuras=[]
    
    def getListaTokens(self):
        return self.lista_tokens
    
    def ReconocerF1(self, string):
        lineas = string.splitlines() #separar el script en lineas
        for linea in lineas:
            linea = linea.strip()
            palabra=''
            for caracter in linea:
                if caracter == ' ':
                    if palabra != '':
                        token=Clasificador.tokenizer(palabra)
                        self.lista_tokens.append(token)
                    token=Clasificador.tokenizer(palabra)
                    self.lista_tokens.append(token)
                    palabra=''
                elif Clasificador.esCaracterEsp(caracter):
                    if palabra != '':
                        token=Clasificador.tokenizer(palabra)
                        self.lista_tokens.append(token)
                    token = Clasificador.tokenizerCaracter(caracter)
                    self.lista_tokens.append(token)
                    palabra=''
                else:
                    palabra+=caracter
        return self.lista_tokens
    
    def Reconocer(self, string):
        self.lista_tokens=self.ReconocerF1(string)
        

cadena="""int entero=45;
	float flotante = 17.458;
	double mayor = 18.79847;
	char letra = 'a';
"""
mi_reconocedor=reconocedor()
mi_reconocedor.ReconocerF1(cadena)
Lista=mi_reconocedor.getListaTokens()
for token in Lista:
    print(token.dato,token.tipo+"\n")

# expresion regular para caracter especial:
# [!@#$%^&*_()+{}|:"<>?~`-=[]\;',./]