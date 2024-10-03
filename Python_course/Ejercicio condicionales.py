print("Calcular el indice de masa corporal de una persona")

weight = float(input("Introduce tu peso en kg: "))
height = float(input("Introduce tu altura en metros: "))

imc = float(weight / (height * height))

print("Mi IMC es " , round(imc,2))

if(imc <= 18.5):
    print("Poco peso")
elif((imc > 18.5) and (imc <= 24.9)):
     print("Normal")
elif((imc > 24.9) and (imc <= 29.9)):
    print("Sobrepeso")
else:
     print("Obesidad")
