import Reconocedor as rec

cadena="""entero a = 45,c = 17
	real b =(17.458+2-4),d=8.5
    si a > b
        a = 10
    finSi
"""

scanner = rec.scanner()
scanner.separador_tokens(cadena)
for token in scanner.getListaTokens():
    print(token.get_dato(), token.get_tipo())


