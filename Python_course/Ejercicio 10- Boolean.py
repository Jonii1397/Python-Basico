print("Este programa comparara tu edad con la de un usuario")

age = 26

ageuser = int(input("Introduce tu edad: "))

'''
if(age == ageuser ):
    print("Tenéis la misma edad")
elif(age < ageuser):
   print("El admin es menor que el usuario")
else:
     print("El admin es mayor que el usuario")
'''

if(age == ageuser or age > ageuser):
    print("Tenéis la misma edad o admin es mayor")
else:
     print("El admin es menor")

