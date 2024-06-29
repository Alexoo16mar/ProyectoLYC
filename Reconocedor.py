import Clasificador as clas
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
        def add_token(string):
            if string != "":
                token = clas.tokenizer(string)
                self.lista_tokens.append(token)
        def add_caracter_esp_token(string):
            if string != "":
                token = clas.tokenizer_caracter_esp(string)
                self.lista_tokens.append(token)
        for linea in lineas:
            linea = linea.strip()
            palabra=''
            palabra_esp=''
            i=0
            while i < len(linea):
                caracter = linea[i]
                if caracter == ' ':
                    add_token(palabra)
                    palabra = ''
                elif clas.es_caracter_esp(caracter):
                    add_token(palabra)
                    palabra = ''
                    while i < len(linea) and clas.es_caracter_esp(linea[i]):
                        if not clas.es_caracter_esp(palabra_esp + linea[i]):
                            add_caracter_esp_token(palabra_esp)
                            add_caracter_esp_token(linea[i])
                            i += 1
                            palabra_esp = ''
                            continue
                        palabra_esp += linea[i]
                        i += 1
                    add_caracter_esp_token(palabra_esp)
                    palabra_esp = ''
                    continue
                else:
                    palabra += caracter
                i += 1
            add_token(palabra)
            if palabra_esp != '':
                add_caracter_esp_token(palabra_esp)
    
    def Reconocer(self, string):
        self.separador_tokens(string)
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
