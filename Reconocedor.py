import Clasificador
import AutomataPila
import AutomataFDNum
class scanner():
    def __init__(self):
        self.pila_estructuras=[]
        self.lista_tokens=[]
        self.lista_errores=[]
        self.lista_estructuras=[]
    
    def getListaTokens(self):
        return self.lista_tokens
    
    def separador_tokens(self, string):
        lineas = string.splitlines() #separar el script en lineas
        for linea in lineas:
            linea = linea.strip()
            palabra=''
            palabra_esp=''
            i=0
            while i < len(linea):
                caracter = linea[i]
                if caracter == ' ':
                    if palabra != '':
                        token = Clasificador.tokenizer(palabra)
                        self.lista_tokens.append(token)
                    palabra = ''
                elif Clasificador.es_caracter_esp(caracter):
                    if palabra != '':
                        token = Clasificador.tokenizer(palabra)
                        self.lista_tokens.append(token)
                    while i < len(linea) and Clasificador.es_caracter_esp(linea[i]):
                        palabra_esp += linea[i]
                        i+=1
                    token = Clasificador.tokenizer_caracter_esp(palabra_esp)
                    palabra_esp = ''
                    self.lista_tokens.append(token)
                    palabra = ''
                else:
                    palabra += caracter
                i+=1
        return self.lista_tokens
    
    def Reconocer(self, string):
        self.lista_tokens=self.separador_tokens(string)
        lista=self.lista_tokens
        i=0
        n = len(lista)
        print ("Lista de tokens:")
        for i in range(n):
            print(i,lista[i].get_dato(),"-->", lista[i].get_tipo())
        i=0
        while i<n:
            i=AutomataFDNum.AutomataFDDeclaraciones(lista, i)
            i=AutomataPila.AutomataPila(lista, i)
            i+=1
        print("Fin de la ejecucion")
