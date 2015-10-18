#tarea 4 l martinez
# un programa  al cual se le ingresa x cantidad de minuto y el dice a que equivale a dia hora,minutos.

minuto=input ("ingrese: minuto:")

minuto = int(minuto)



dia =1440
hora=60


if minuto > dia:
   rd=minuto//dia
   res=minuto%dia
   h=res//hora
   m=res%hora



   print("los dias son:"+ str(rd) + "las hora: "+str(h) + "los minuto son: "+str((m)))

elif minuto <= dia:
   h=minuto//hora
   m=minuto%hora
   d=0

   print("los dias son:"+str(d)+"las hora son:"+str(h)+"los minutos son:"+str((m)))

