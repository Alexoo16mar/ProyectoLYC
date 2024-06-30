from Clasificador import palabras_reservadas,caracteres_especiales
from Token import Token
import MiExcepcion

def AFDComparaciones(lista_tokens,i):
    indice = i
    estado_actual = "q0"
    palabras_reservadas_comparacion = set(caracteres_especiales["<Operador_Comparacion>"])
    palabras_reservadas_opLogicos = set(palabras_reservadas["<Operador_Logico>"])
    while (estado_actual != "qf"):
        if (estado_actual == "q0"):
            if lista_tokens[indice].get_tipo()=="ID" or lista_tokens[indice].get_tipo()=="Numerico":
                estado_actual = "q1"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! condicion invalida ")
        if (estado_actual == "q1"):
            if lista_tokens[indice].get_dato() in palabras_reservadas_comparacion:
                estado_actual = "q2"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! condicion invalida ")
        if (estado_actual == "q2"):
            if lista_tokens[indice].get_tipo()=="ID" or lista_tokens[indice].get_tipo()=="Numerico":
                estado_actual = "q3"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! condicion invalida ")
        if (estado_actual == "q3"):   
            if lista_tokens[indice].get_dato() in palabras_reservadas_opLogicos:
                estado_actual = "q4"
                indice = indice + 1
            else:
                estado_actual="qf"
                return indice
        if (estado_actual == "q4"):   
            if lista_tokens[indice].get_tipo()=="ID" or lista_tokens[indice].get_tipo()=="Numerico":
                estado_actual = "q1"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! condicion invalida ")
