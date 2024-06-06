import Reconocedor as rec

cadena="""int entero = 45 ;
	float flotante = 17.458 ;
	double mayor = 18.79847 ;
	char letra = 'a' ;
    if ( condicion ) {
        cout << " mayor es: " << mayor << endl ;
    } else {
        cout << " mayor es: " << flotante << endl ;
    }
"""

scanner = rec.scanner()
scanner.Reconocer(cadena)