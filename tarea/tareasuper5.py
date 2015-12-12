__author__ = 'luis M'
 #programa de supermercado ABC

print("   *****************")
print("   * SUPER MERCADO *")
print("   *****************")
lista= []
opcion=0;
contador = -1

while opcion != "4":
 print("1.  Agregar producto")
 print("2.  Eliminar producto")
 print("3.  Productos en lista ")
 print("4.  Salir")

 opcion=input("   Elija una opcion: ")

 if opcion == "1":
  objeto=input("Que quieres agregar? ")
  contador = contador + 1
  objeto = (str(contador) + "." + str(objeto))
  lista.append(objeto)

 if opcion == "2":
  print(lista)
  eliminar = int(input("Que quieres eliminar de la lista? "))
  print("Creo que ya se a eliminado : " + lista[eliminar])
  del lista[eliminar]

 if opcion == "3":
  print(lista)

 print("toca enter para continuar")
 input()
 os.system("cls")
