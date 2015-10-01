

#luis Martinez
#clase#3 quiz 2

compra=float(input("Ingrese monto compra:")) 

if compra >=500:
   descuento=0.30
   descuento=compra*0.30
   total=compra-descuento
   print(total) 

elif compra>=200 and compra<500:
   descuento=0.20
   descuento=compra*0.20
   total=compra-descuento
   print(total)

elif compra>=100 and compra<200:
   descuento=0.20
   descuento=compra*0.10
   total=compra-descuento
   print(compra) 

else:
   descuento=00 