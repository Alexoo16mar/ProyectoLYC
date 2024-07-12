import Reconocedor as rec

cadena="""
    real funcion1(entero a, real b, real c=3):
        si a>0
            a=a+1
            si b>0
                si c>0
                    c=c+1
                sino si c<0
                    c=c-1
                    si c==0
                        c=0
                    sino si c!=0
                        c=1
                    finSi
                finSi
            finSi
            a=a+
        finSi
        retornar c
    finFun
"""

scanner = rec.scanner()
scanner.Reconocer(cadena)

