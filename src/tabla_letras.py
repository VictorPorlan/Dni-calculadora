class tabla_letras:
    letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    longitud = [*range(0, len(letras))]
    tabla = dict(zip(longitud, letras))
    def __init__(self, numero):
        self.numero = int(numero)

    def calcular_letra(self):
        try:
            return tabla_letras.tabla[self.numero % len(tabla_letras.letras)]
        except:
            'Ha ocurrido un error calculando la letra'
    
        
    