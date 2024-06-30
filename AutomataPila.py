import ADFComparaciones as comparaciones
from Clasificador import palabras_reservadas
from scan import scan
from MiExcepcion import MiExcepcion

def AutomataPilaEstructuras(lista_tokens, i):
    try:
        indice = i
        if (lista_tokens[i].get_dato() == "si"):
            indice = AutomataPilaSI(lista_tokens, i)
        elif lista_tokens[i].get_dato() == "mientras":
            indice = AutomataPilaMientras(lista_tokens, i)
        elif lista_tokens[i].get_dato() == "para":
            indice = AutomataFDPara(lista_tokens, i)
    except MiExcepcion as error:
        print(error.mensaje)
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
                pila_1.pop()
                indice = indice + 1
                estado_actual = "q3"
            elif (lista_tokens[indice].get_dato() == "finSi" and len(pila_1) != 0):
                estado_actual = "qf"
                print("Estructura IF correcta!")
                return indice + 1
        if (estado_actual == "q3"):
            if (lista_tokens[indice].get_dato() == "si"):
                pila_1.append("si")
                indice = indice + 1
                estado_actual = "q1"
            else:
                raise MiExcepcion("Error en estructura IF! ")

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
                if lista_tokens[indice].get_dato() in palabras_reservadas_tipo or lista_tokens[indice].get_tipo()=="ID":
                    estado_actual = "q7"
                    indice = indice + 1
                else:
                    raise MiExcepcion("Error! Estructura para incorrecta")
        if (estado_actual == "q7"):
                indice=scan(lista_tokens,indice)
                if lista_tokens[indice].get_dato()=="finPara":
                    indice=indice+1
                    estado_actual = "qf"
                    return indice + 1
                else:
                    raise MiExcepcion("Error! Estructura para incorrecta")



# string = """
#             si a > 5 o b < 10 o c == 5
#                 salah maleko
#                 malekon salah
#             finSi
#         """

# variable_random = scanner()
# variable_random.separador_tokens(string)
# # # for token in variable_random.lista_tokens:
# # #     print(token.get_dato() + " " + token.get_tipo())
# try:
#     print(AutomataPilaSI(variable_random.lista_tokens, 0))
# except MiExcepcion as e:
#     print("Coito")