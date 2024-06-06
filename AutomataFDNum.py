def error():
    print("Lexical Error.")

class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def AutomataFDDeclaraciones(lista_tokens, indice):
    try:
        if (lista_tokens[indice].get_dato() == "int"):
            indice = AFDDeclaracionInt(lista_tokens, indice)
        elif lista_tokens[indice].get_dato() == "double":
            pass
            #indice = AFDDeclaracionDouble(lista_tokens, indice)
        elif lista_tokens[indice].get_dato() == "float":
            pass
            #indice = AFDDeclaracionFloat(lista_tokens, indice)
        elif lista_tokens[indice].get_dato() == "bit":
            pass
            #indice = AFDDeclaracionBit(lista_tokens, indice)
    except MiExcepcion as error:
        print(error.mensaje)
        print("Error! de aqui en adelante el codigo no se ejecutara correctamente")
    return indice

def AFDDeclaracionInt(lista_tokens, indice):
    q = 0
    while q != 100 and q != -1:
        if q == 0:
            if lista_tokens[indice].get_tipo() == '<tipo>':
                q = 1
                indice += 1
            else:
                #error()
                q = -1
        elif q == 1:
            if lista_tokens[indice].get_tipo() == "ID":
                q = 2
                indice += 1
            else:
                #error()
                q = -1
        elif q == 2:
            if lista_tokens[indice].get_tipo() == "<Caracter_Puntuacion>":
                if lista_tokens[indice].get_dato() == ";":
                    q = 100
                    indice += 1
                elif lista_tokens[indice].get_dato() == ",":
                    q = 6
                    indice += 1
            elif lista_tokens[indice].get_tipo() == "<Operador_asignacion>":
                q = 3
                indice += 1
            else:
                #error()
                q = -1
        elif q == 3:
            if lista_tokens[indice].get_tipo() == "Numerico":
                q = 5
                indice += 1
            elif lista_tokens[indice].get_tipo() == "<Operador_Aritmetico>":
                q = 4
                indice += 1
            else:
                #error()
                q = -1
        elif q == 4:
            if lista_tokens[indice].get_tipo() == "Numerico":
                q = 5
                indice += 1
            else:
                #error()
                q = -1
        elif q == 5:
            if lista_tokens[indice].get_tipo() == "<Caracter_Puntuacion>":
                if lista_tokens[indice].get_dato() == ";":
                    q = 100
                    indice += 1
                elif lista_tokens[indice].get_dato() == ",":
                    q = 6
                    indice += 1
                else:
                    #error()
                    q = -1
            else:
                #error()
                q = -1
        elif q == 6:
            if lista_tokens[indice].get_tipo() == "ID":
                q = 2
                indice += 1
            else:
                #error()
                q = -1
    if q == 100:
        print("Declaracion de variable int correcta!")
        return indice
    if q == -1:
        raise MiExcepcion("Error en declaracion!")


def AFDDeclaracionDouble(token, indice):
    pass


def AFDDeclaracionFloat(token, indice):
    pass


def AFDDeclaracionBit(token, indice):
    pass