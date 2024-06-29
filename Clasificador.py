from Token import Token
import re

palabras_reservadas={
    "<tipo>":["entero","real"],#,"float","bool","double","char"],
    "<Condicional>":["si"],
    "<Cierre_Condicional>":["sino", "finSi"],
    "<Bucle>":["para","mientras"],
    "<Cierre_Bucle>":["finPara","finMientras"],
    "<Operador_Logico>":["y","o","no"],
}
caracteres_especiales = {
    "<Operador_Aritmetico>": ['+', '-', '/', '%', '*'],
    "<Operador_asignacion>": ['=', '+=', '-=', '=', '/=', '%=', '*=', '//='],
    "<Operador_Comparacion>": ['<', '>', '<=', '>=','==', '!='],
    "<Operador_Incremento>": ['++', '--'],
    "<Caracter_Puntuacion>": [','],
    "<Caracter_Agrupacion>": ['(', ')', '[', ']', '{', '}']
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

def es_caracter_esp(dato):
    encontrado=False
    for categoria,valor in caracteres_especiales.items():
        if dato in valor:
            encontrado = True
            break
    return encontrado

def tokenizer_caracter_esp(dato):
    tipo="No encontrado"
    for categoria,valor in caracteres_especiales.items():
        if dato in valor:
            tipo = categoria
            break
    nuevoToken = Token(dato, tipo)
    return nuevoToken
