from Token import Token
import re

palabras_reservadas={
    "<tipo>":["int","string","float","bool","double","char"],
    "<Condicional>":["if"],
    "<Cierre_Condicional>":["else"],
    "<Bucle>":["for","while","do"],
    "<Control_Flujo>":["case","switch","break","continue","return"],
    "<Acceso>":["public","private","protected"],
    "<Flujo_entrada/salida>":["cout","cin"],
    "<Manipulador_flujo>":["endl"],
    "<Manejo_excepcion>":["try","catch","throw","throws"],
    "<Espacio_nombres>":["namespace","using"],
    "<Libreria>":["#include<iostream>"],
}
caracteres_especiales = {
    "<Operador_Aritmético>": ['+', '-', '', '/', '%', '*'],
    "<Operador_asignación>": ['='], #, '+=', '-=', '=', '/=', '%=', '*=', '//='], just in case :)
    "<Operador_Comparación>": ['==', '!=', '<', '>', '<=', '>='],
    "<Operador_Lógicos>": ['and', 'or', 'not'],
    "<Caracter_Agrupación>": ['(', ')', '[', ']', '{', '}'],
    "<Caracter_Puntuación>": [',', '.', ':', ';'],
    "<Operador_membresía>": ['in', 'not in'],
    "<Operador_identidad>": ['is', 'is not'],
    "<Caracteres_escape>": ['\\', '\'', '\"', '\n', '\t'],
}

def tokenizer(dato):
    tipo="No encontrado"
    for categoria,valor in palabras_reservadas.items():
        if dato in valor:
            tipo = categoria
            nuevoToken = Token(dato, tipo)
            return nuevoToken
    regex = re.compile(r'^[a-zA-Z_]\w*$')
    regex_num = re.compile(r'^[+-]?\d+(\.\d+)?$')
    if (regex.match(dato)):
        tipo = "ID"
    elif(regex_num.match(dato)):
        tipo = "Numerico"

    nuevoToken = Token(dato, tipo)
    return nuevoToken

def esCaracterEsp(dato):
    encontrado=False
    for categoria, valor in caracteres_especiales.items():
        if dato in valor:
            encontrado = True
            break
    return encontrado

def tokenizerCaracter(dato):
    tipo="No encontrado"
    for categoria,valor in caracteres_especiales.items():
        if dato in valor:
            tipo = categoria
            break
    nuevoToken = Token(dato, tipo)
    return nuevoToken

# mi_token = tokenizer("else")
# print(mi_token.dato,mi_token.tipo)