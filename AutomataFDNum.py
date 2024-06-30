from collections import deque
from queue import LifoQueue
from Clasificador import palabras_reservadas
import ADFComparaciones as comparaciones
from MiExcepcion import MiExcepcion

def scan(lista_tokens,i):
    if lista_tokens[i].get_tipo()=="<tipo>" or lista_tokens[i].get_tipo()=="ID":
        indice = AutomataFDDeclaraciones(lista_tokens,i)
    else:
        indice = AutomataPilaEstructuras(lista_tokens, i)
    if indice < len(lista_tokens) and lista_tokens[indice].get_tipo() not in ["<Cierre_Bucle>", "<Cierre_Condicional>", "<Cierre_Funcion>"]:
        indice = scan(lista_tokens,indice)
    return indice

def AutomataFDDeclaraciones(lista_tokens, indice):
    if (lista_tokens[indice].get_tipo() == "<tipo>"):
        if(lista_tokens[indice+2].get_dato()=="("):
            indice = AutomataPilaFunciones(lista_tokens,indice)
        else:
            indice = AutomataPilaEA(lista_tokens,indice)
    elif lista_tokens[indice].get_tipo() == "ID":
        if(lista_tokens[indice+1].get_dato() =="("):
            indice = AutomataPilaFunciones(lista_tokens,indice)
        else:
            indice = AutomataPilaEA(lista_tokens,indice)
    return indice

def AutomataPilaEA(lista_tokens,i):
    indice = i
    pila = deque()
    estado_actual = "q0"
    while estado_actual != "qf" and indice < len(lista_tokens):
        if estado_actual == "q0":
            if lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q1"
                indice += 1
            elif lista_tokens[indice].get_tipo() == "<tipo>":
                estado_actual = "q9"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        elif estado_actual == "q9":
            if lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q1"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        elif estado_actual == "q1":
            if lista_tokens[indice].get_dato() == "=":
                estado_actual = "q2"
                indice += 1
            else:
                estado_actual="qf"
                return indice
        elif estado_actual == "q2":
            if lista_tokens[indice].get_tipo() == "ID" or lista_tokens[indice].get_tipo() == "Numerico":
                estado_actual = "q3"
                indice += 1
            elif lista_tokens[indice].get_dato() == "(":
                estado_actual = "q5"
                indice += 1
                pila.append("(")
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        elif estado_actual == "q3":
            if lista_tokens[indice].get_dato() == ")":
                if len(pila) == 0:
                    raise MiExcepcion("Error! >> Expresion Incorrecta")
                else:
                    pila.pop()
                estado_actual = "q3"
                indice += 1
            elif lista_tokens[indice].get_tipo() == "<Operador_Aritmetico>":
                estado_actual = "q8"
                indice += 1
            else:
                estado_actual="qf"
                return indice
        elif estado_actual == "q5":
            if lista_tokens[indice].get_tipo() == "Numerico" or lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q6"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        elif estado_actual == "q6":
            if lista_tokens[indice].get_dato() == ")":
                estado_actual = "q3"
                indice += 1
            elif lista_tokens[indice].get_tipo() == "<Operador_Aritmetico>":
                estado_actual = "q7"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        elif estado_actual == "q7":
            if lista_tokens[indice].get_dato() == "(":
                estado_actual = "q5"
                pila.append("(")
                indice += 1
            elif lista_tokens[indice].get_tipo() == "Numerico" or lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q6"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
        elif estado_actual == "q8":
            if lista_tokens[indice].get_dato() == "(":
                estado_actual = "q5"
                pila.append("(")
                indice += 1
            elif lista_tokens[indice].get_tipo() == "Numerico" or lista_tokens[indice].get_tipo() == "ID":
                estado_actual = "q3"
                indice += 1
            else:
                raise MiExcepcion("Error! >> Expresion Incorrecta")
    return indice

def AutomataPilaFunciones(lista_tokens, i):
    indice = i
    pila_1 = LifoQueue() # para los tipos de funciones
    pila_2  = LifoQueue() # para : y end
    estado_actual = "q0"
    palabras_reservadas_tipo = set(palabras_reservadas["<tipo>"])
    while (estado_actual != "qf"):
        if (estado_actual == "q0"):
                if lista_tokens[indice].get_dato() in palabras_reservadas_tipo:
                    pila_1.put(lista_tokens[indice].get_dato())
                    estado_actual = "q1"
                    indice = indice + 1
                elif lista_tokens[indice].get_tipo()=="ID":
                    estado_actual = "q2"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q1"):
                if lista_tokens[indice].get_tipo()=="ID":
                    estado_actual = "q2"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q2"):
                if lista_tokens[indice].get_dato()=="(":
                    estado_actual = "q3"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q3"):
                if lista_tokens[indice].get_dato()==")":
                    estado_actual = "q8"
                    indice = indice + 1
                elif(lista_tokens[indice].get_dato() in palabras_reservadas_tipo):
                    estado_actual = "q4"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q4"):
                if lista_tokens[indice].get_tipo()=="ID":
                    estado_actual = "q5"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q5"):
                if lista_tokens[indice].get_dato()==")":
                    estado_actual = "q8"
                    indice = indice + 1
                elif lista_tokens[indice].get_dato()=="=":
                    estado_actual = "q6"
                    indice = indice + 1
                elif lista_tokens[indice].get_dato()==",":
                    estado_actual = "qm"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q6"):
                if lista_tokens[indice].get_tipo()=="ID" or lista_tokens[indice].get_tipo()=="Numerico":
                    estado_actual = "q7"
                    indice = indice + 1
                elif lista_tokens[indice].get_dato()==",":
                    estado_actual = "qm"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q7"):
                if lista_tokens[indice].get_dato()==")":
                    estado_actual = "q8"
                    indice = indice + 1
                elif lista_tokens[indice].get_dato()==",":
                    estado_actual = "qm"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "qm"):
                if lista_tokens[indice].get_dato() in palabras_reservadas_tipo:
                    estado_actual = "q4"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
                        
        if (estado_actual == "q8"):
                if lista_tokens[indice].get_dato()==":":
                    pila_2.put(":")
                    estado_actual = "q9"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q9"):
                indice=scan(lista_tokens,indice)
                print(indice)
                if lista_tokens[indice].get_dato()=="finFun" and pila_1.empty():
                    pila_2.get()
                    if pila_2.empty():
                        estado_actual = "qf"
                        print("Funcion correcta!")
                        return indice + 1
                    else:
                        raise MiExcepcion("Error! Funcion mal declarada ")
                elif(lista_tokens[indice].get_dato()=="retornar" and  not(pila_1.empty())):
                    pila_1.get()
                    estado_actual = "q10"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q10"):
                if lista_tokens[indice].get_tipo()=="ID" or lista_tokens[indice].get_tipo()=="Numerico" :
                    estado_actual = "q11"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")
        if (estado_actual == "q11"):
                if lista_tokens[indice].get_dato()=="finFun" and pila_1.empty():
                    estado_actual="qf"
                    print("Funcion correcta!")
                    return indice+1
                else:
                    raise MiExcepcion("Error! Funcion mal declarada ")

def AutomataPilaEstructuras(lista_tokens, i):
    indice = i
    if (lista_tokens[i].get_dato() == "si"):
        indice = AutomataPilaSI(lista_tokens, i)
    elif lista_tokens[i].get_dato() == "mientras":
        indice = AutomataPilaMientras(lista_tokens, i)
    elif lista_tokens[i].get_dato() == "para":
        indice = AutomataFDPara(lista_tokens, i)
    return indice

def AutomataPilaSI(lista_tokens, i):
    indice = i
    pila_1 = []  # para if else
    estado_actual = "q0"
    while (estado_actual != "qf"):
        if (estado_actual == "q0"):
            if lista_tokens[indice].get_dato() == "si":
                pila_1.append("si")
                estado_actual = "q1"
                indice = indice + 1
            else:
                raise MiExcepcion("Error en estructura SI!")
        if (estado_actual == "q1"):
            indice = comparaciones.AFDComparaciones(lista_tokens,indice) # try catch incorporado
            estado_actual = "q2"
        if (estado_actual == "q2"):
            indice=scan(lista_tokens,indice)
            if (lista_tokens[indice].get_dato() == "sino" and len(pila_1) != 0):
                indice = indice + 1
                estado_actual = "q3"
            elif (lista_tokens[indice].get_dato() == "finSi" and len(pila_1) != 0):
                pila_1.pop()
                estado_actual = "qf"
                print("Estructura IF correcta!")
                return indice + 1
            else:
                raise MiExcepcion("Error en estructura IF! ")
        if (estado_actual == "q3"):
            if (lista_tokens[indice].get_dato() == "si"):
                # pila_1.append("si")
                indice = indice + 1
                estado_actual = "q1"
            else:
                estado_actual = "q2"

def AutomataPilaMientras(lista_tokens, i):
    indice = i
    pila_1 = []  # para mientras
    estado_actual = "q0"
    
    while (estado_actual != "qf"):
        if (estado_actual == "q0"):
            if lista_tokens[indice].get_dato() == "mientras":
                pila_1.append("mientras")
                estado_actual = "q1"
                indice += 1
            else:
                raise MiExcepcion("Error en estructura \"mientras\"!")
        if (estado_actual == "q1"):
            indice = comparaciones.AFDComparaciones(lista_tokens,indice) # try catch incorporado
            estado_actual = "q2"
        if (estado_actual == "q2"):
            indice=scan(lista_tokens,indice)
            estado_actual = "q3"
        if (estado_actual == "q3"):
            if (lista_tokens[indice].get_dato() == "finMientras"):
                pila_1.pop()
                indice += 1
                estado_actual = "qf"
                print("Estructura MIENTRAS correcta!")
                return indice
            else:
                raise MiExcepcion("Error en estructura MIENTRAS!")

def AutomataFDPara(lista_tokens, i):
    indice = i
    estado_actual = "q0"
    palabras_reservadas_tipo = set(palabras_reservadas["<tipo>"]) 
    while (estado_actual != "qf"):
        if (estado_actual == "q0"):
            if lista_tokens[indice].get_dato()=="para":
                estado_actual = "q1"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! Estructura para incorrecta")
        if (estado_actual == "q1"):
            if lista_tokens[indice].get_dato() in palabras_reservadas_tipo:
                estado_actual = "q2"
                indice = indice + 1
            elif lista_tokens[indice].get_tipo()=="ID":
                estado_actual = "q3"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! Estructura para incorrecta")
        if (estado_actual == "q2"):
            if lista_tokens[indice].get_tipo()=="ID":
                estado_actual = "q3"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! Estructura para incorrecta")
        if (estado_actual == "q3"):
            if lista_tokens[indice].get_dato()=="desde":
                estado_actual = "q4"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! Estructura para incorrecta")
        if (estado_actual == "q4"):
            if lista_tokens[indice].get_tipo()=="Numerico" or lista_tokens[indice].get_tipo()=="ID":
                estado_actual = "q5"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! Estructura para incorrecta")
        if (estado_actual == "q5"):
            if lista_tokens[indice].get_dato()=="hasta":
                estado_actual = "q6"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! Estructura para incorrecta")
        if (estado_actual == "q6"):
            if lista_tokens[indice].get_tipo() =="Numerico" or lista_tokens[indice].get_tipo()=="ID":
                estado_actual = "q7"
                indice = indice + 1
            else:
                raise MiExcepcion("Error! Estructura para incorrecta")
        if (estado_actual == "q7"):
            indice=scan(lista_tokens,indice)
            if lista_tokens[indice].get_dato()=="finPara":
                indice=indice+1
                estado_actual = "qf"
                print("Estructura PARA correcta!")
                return indice
            else:
                raise MiExcepcion("Error! Estructura para incorrecta")