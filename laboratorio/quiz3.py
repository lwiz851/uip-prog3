# dado un intervalo de tiempo en segundo, calcular los segundo restante que corresponde 
# para convertir  exactamente en minutos. este programa debe funcionar 5 vece


  
#segundo=float(input ("ingrese:segundos:"))

cont = 5

while cont > 0:
   segundo=input ("ingrese:segundos:")

   segundo = int(segundo)

   minuto =60


   #  r = residuo de la divicion 1, m=  a los minuto 

   if segundo  >  minuto:
      mt=segundo/minuto
      r=segundo%minuto
      s=mt*minuto
      sexacto=s-r
      me=sexacto/minuto
      mexacto=sexacto//minuto
   
      segundosrestantes=minuto-r

   
      # print("los cantidad de segundos restante es: "+ str  (segundosrestantes)  +"los minuto son:"+str (mexacto) +"y los segundo son:"+str((r)))
      print(" minutos: "+ str  (mexacto)+ " segundo: " + str (r) + " segundos restante:" + str((segundosrestantes)))



   elif segundo <= minuto:
      segundosrestante=minuto-segundo
      esminuto=0
      print("los minutos " + str(esminuto)  +"segundos restantes:"+str((segundosrestante)))
   
   cont = cont - 1
