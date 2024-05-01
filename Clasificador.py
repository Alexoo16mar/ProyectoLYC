from Token import Token

palabras_reservadas={
    "Tipo Dato":["int","string","float","bool","double","char"],
    "Condicional":["if"],
    "Cierre Condicional":["else"],
    "Bucle":["for","while","do"],
    "Control de Flujo":["case","switch","break","continue","return"],
    "Acceso":["public","private","protected"],
    "Flujo de entrada/salida":["cout","cin"],
    "Manipulador de flujo":["endl"],
    "Manejo de excepcion":["try","catch","throw","throws"],
    "Espacio de nombres":["namespace","using"],
    "Libreria":["#include<iostream>"],
}
caracteres_especiales = {
    "Operador Aritméticos": ['+', '-', '*', '/', '%', '**'],
    "Operador asignación": ['='], #, '+=', '-=', '*=', '/=', '%=', '**=', '//='], just in case :)
    "Operador de Comparación": ['==', '!=', '<', '>', '<=', '>='],
    "Operador Lógicos": ['and', 'or', 'not'],
    "Caracter de Agrupación": ['(', ')', '[', ']', '{', '}'],
    "Caracter Puntuación": [',', '.', ':', ';'],
    "Operador de membresía": ['in', 'not in'],
    "Operador de identidad": ['is', 'is not'],
    "Caracteres de escape": ['\\', '\'', '\"', '\n', '\t']
}

def tokenizer(dato):
    tipo="No encontrado"
    for categoria,valor in palabras_reservadas.items():
        if dato in valor:
            tipo = categoria
            break

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

mi_token = tokenizer("else")
print(mi_token.dato,mi_token.tipo)