#tarea 4 l martinez
# un programa  al cual se le ingresa x cantidad de minuto y el dice a que equivale a dia hora,minutos.

minuto=input ("ingrese: minuto:")

minuto = int(minuto)



day = 1440
hour=60


if minuto > day:
   rd=minuto//day
   res=minuto%day
   h=res//hour
   m=res%hour






   print("los dias son:"+ str(rd) + "las hora: "+str(h) + "los minuto son: "+str((m)))

elif minuto <= day:
   h=minuto//hour
   m=minuto%hour
   d=0

   print("los dias son:"+str(d)+"las hora son:"+str(h)+"los minutos son:"+str((m)))

