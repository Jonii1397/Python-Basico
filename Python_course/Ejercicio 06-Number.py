import math

print("Calcula el área y la circunferencia de un círculo de radio r")
r = int (input("Introduce el radio del círculo: "))

area = float(math.pi * (r*r))
cir = float (2 * math.pi * r)
print ("El área del círculo es: " , round(area,2) )
print ("La circunferencia del círculo es: " , round(cir,2) )
