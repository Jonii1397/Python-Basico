#Nota 1
data_valid = False

while data_valid == False:
    nota1 = float(input("Escribe tu primera nota: "))
    if(nota1 < 0 or nota1 > 10):
        print ("La nota debe estar comprendida entre 0 y 10")
        continue
    else:

        data_valid = True

#Nota 2
data_valid = False

while data_valid == False:
    nota2 = float(input("Escribe tu primera nota: "))
    if(nota2 < 0 or nota2 > 10):
        print ("La nota debe estar comprendida entre 0 y 10")
        continue
    else:
        data_valid = True

#Numero de clases
while data_valid == False:
    total_clases = int(input("Escribe el numero de clases: "))
    if(total_clases <= 0):
        print ("El número de clases debe ser superior a 0")
        continue
    else:
        data_valid = True
        
#Numero de faltas
data_valid = False

while data_valid == False:
    ausencia = int(input("Escribe el numero de faltas: "))
    if(ausencia <= 0 or ausencia > total_clases):
        print ("El número de ausencias debe ser superior a 0 e inferior o igual al número de clases")
        continue
    else:
        data_valid = True




nota_media = (nota1 + nota2) /2
asistencia = (total_clases - ausencia)/total_clases

print("Nota promedio " , round(nota_media,2))
print("Porcentaje de asistencia" , str(round((asistencia *100),2))+ '%')

if(nota_media >= 6 and asistencia >= 0.8):
    print("Has aprobado")
elif(nota_media < 6 and asistencia < 0.8):
    print("Has suspendido debido a que tienes menos de un 6 de media y tu asistencia ha sido inferior al 80%")
elif(aistencia >= 0.8):
    print("Has suspendido por tener una nota media inferior a 6")
else:
    print("Has suspendido debido a que tu asistencia ha sido inferior al 80%")
