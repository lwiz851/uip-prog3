# tarea 3 luis Martinez
#numeros triangulares



numero =(input("Ingrese numero:"))

counter = 0


while counter < int(numero):
   counter += 1
   r = (counter * (counter + 1)) / 2

   print("%d - %d" % (counter, r))



