import os
print("DIRECTORIO TELEFONICO")
opcion=0;
agenda={}
while opcion != "5":
	print("1: Agregar numero ")
	print("2. Eliminar numero")
	print("3. Imprimir numero")
	print("4. Buscar numeros")
	print("5. Salir")

	opcion=input("eliga una opcion: ")

	if opcion == "1":
		nombre=str(input("Ingrese en nombre de la persona: "))
		numero=int(input("Ingrese el numero de telefono: "))
		agenda[nombre] = numero
	if opcion == "2":
		print(agenda)
		eliminar=input("Ingrese el nombre de la persona que desea eliminar: ")
		if eliminar in agenda:
			del agenda[eliminar]
			print("Se a eliminado el elemento: " + str(eliminar))
		else:
			print("Ese nombre no existe en la agenda")
	if opcion == "3":
		print(agenda)
	if opcion == "4":
		buscar=str(input("A quien desea buscar? "))
		if buscar in agenda:
			print("Numero: " + str(agenda[buscar]))
		else:
			print("Ese nombre no existe en la agenda")
	print("Pulse enter para continuar")
	input()
	os.system("cls")