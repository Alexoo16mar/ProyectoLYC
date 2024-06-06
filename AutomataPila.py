
class MiExcepcion(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

def AutomataPila(lista_tokens, i):
    try:
        indice = i
        if (lista_tokens[i].get_dato() == "if"):
            indice = AutomataPilaIF(lista_tokens, i)
        elif lista_tokens[i].get_dato() == "while":
            indice = AutomataPilaWHILE(lista_tokens, i)
        elif lista_tokens[i].get_dato() == "for":
            indice = AutomataPilaFOR(lista_tokens, i)
        elif lista_tokens[i].get_dato() == "do":
            indice = AutomataPilaDOWHILE(lista_tokens, i)
        elif lista_tokens[i].get_dato() == "switch":
            indice = AutomataPilaSWITCHCASE(lista_tokens, i)
    except MiExcepcion as error:
        print(error.mensaje)
    return indice

def AutomataPilaIF(lista_tokens, i):
    indice = i
    pila_1 = []  # para if else
    pila_2 = []  # para { }
    estado_actual = "q0"
    while (estado_actual != "qf"):
        if (estado_actual == "q0"):
            if lista_tokens[indice].get_dato() == "if":
                pila_1.append("if")
                estado_actual = "q1"
                indice = indice + 1
            else:
                raise MiExcepcion("Error en estructura IF!")
        if (estado_actual == "q1"):
            if lista_tokens[indice].get_dato() == "(":
                # pila no hace nada
                estado_actual = "q2"
                indice = indice + 1
            else:
                raise MiExcepcion("Error en estructura IF!")
        if (estado_actual == "q2"):
            if lista_tokens[indice].get_dato() == "condicion":
                indice = indice + 1
                estado_actual = "q3"
            else:
                raise MiExcepcion("Error en estructura IF!")
        if (estado_actual == "q3"):
            if lista_tokens[indice].get_dato() == ")":
                # pila no hace nada
                estado_actual = "q4"
                indice = indice + 1
            else:
                raise MiExcepcion("Error en estructura IF!")
        if (estado_actual == "q4"):
            if lista_tokens[indice].get_dato() == "{":
                pila_2.append(lista_tokens[i].get_dato())
                estado_actual = "q5"
                indice = indice + 1
            else:
                raise MiExcepcion("Error en estructura IF!")
        if (estado_actual == "q5"):
            while (lista_tokens[indice].get_dato() != "}"):
                indice = indice + 1
                estado_actual = "q5"
        if (estado_actual == "q5"):
            if (lista_tokens[indice].get_dato() == "}"):
                pila_2.pop()
                indice = indice + 1
                estado_actual = "q6"
            else:
                raise MiExcepcion("Error en estructura IF!")
        if (estado_actual == "q6"):
            if (lista_tokens[indice].get_dato() == "else" and len(pila_1) == 0):
                pila_1.pop()
                indice = indice + 1
                estado_actual = "q7"
            else:
                estado_final = "qf"
                print("Estructura IF correcta!")
                return indice + 1
        if (estado_actual == "q7"):
            if (lista_tokens[indice].get_dato() == "{"):
                pila_2.append("{")
                indice = indice + 1
                estado_actual = "q5"
            elif (lista_tokens[indice].get_dato() == "if"):
                pila_1.append("if")
                indice = indice + 1
                estado_actual = "q1"
            else:
                raise MiExcepcion("Error en estructura IF! ")


def AutomataPilaFOR(token):
    pass


def AutomataPilaWHILE(token):
    pass


def AutomataPilaDOWHILE(token):
    pass


def AutomataPilaSWITCH(token):
    pass


def AutomataPilaSWITCHCASE(token):
    pass


def condicion():
    pass
