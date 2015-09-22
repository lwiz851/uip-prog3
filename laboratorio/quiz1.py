#calcular area y perimetro de un rectangulo dada la base y la altura de 5cm, 7cm respectivamente
#ademas debe convertir , la medida del area , y perimetro a otra medida de metros y pulgada

base=5 
altura=7

area= base*altura
perimetro=altura+base *2

area_metro=area/100
area_pulgada=area* 0.39370

perimetro_metro=perimetro/0.01
perimetro_pulgada=perimetro*0.39370

print("El area es " + str(area))
print("El perimetro es " + str(perimetro))
print("El total en metros del area es " + str(area_metro))
print("El total en pulgada del area es " + str(area_pulgada))
print("El total en metro del perimetro es" + str(perimetro_metro))
print("El total en pulgada del perimetro " + str(perimetro_pulgada))