__author__ = 'luis M'
_author__ = 'luis M'


def Menu():
    """Funcion que Muestra el Menu"""

    print ("""************Calculadora************

                 menu
1)suma    2)resta   3)multiplicar    4)dividir  5) Salir""")

def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion:  \n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese Numero\n"))
        y = int(input("numero\n"))
        if (opc==1):
            print ("La Suma es:"+ str ( x+y))
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print ("La Resta es:"+ str (x-y))
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print ("La Multiplicacion es:"+ str(x*y))
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print ("La Division es:"+ str( x/y))
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              opc = int(input("Selecione Opcion\n"))
Calculadora()


