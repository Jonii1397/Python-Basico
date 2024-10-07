import random
print("Programa en el que el usuario introduce 8 nombres para almacenarlos en una lista y devolviendo uno al azar")

str = []

for x in range(0,8):
    person = input("Introduce nombre: ")
    str.append(person)

index = random.randint(0,7)

random_person = str[index]

print(random_person)
