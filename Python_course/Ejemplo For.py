print("Ejemplo con array")
random = ["Hola", "Adios", "Que tal", "", "bien" , "" , "amor"]

for post in random:
    if post == '':
        continue
    else:
        print(post)

print("-------------------------------------------")

print("Ejemplo con string")
cadena = "Hola me llamo Jonathan"
for char in cadena:
        print(char)
        
print("-------------------------------------------")

print("Ejemplo con numeros")
for x in range(0,11):
    print (x)

print("-------------------------------------------")
print("Ejemplo con diccionario")
persona = {"nombre" : "Jonathan" , "genero" : "Masculino" , "edad" : 26}

for y in persona:
    print(y , ":" , persona[y])
