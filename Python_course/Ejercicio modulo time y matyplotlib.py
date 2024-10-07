import time as t
import matplotlib.pyplot as plt

times = []
mistakes = 0

print ("Ejercicio de time y matplotlib")
print ("La palabra para escribir para ayudar a escribir mas rapido es 'python'")
input("Presiona enter para continuar")

while len(times)<5:
    start = t.time()
    cadena =  str(input("Escribe la palabra: "))
    end = t.time()
    time_pasado = end - start
    times.append(time_pasado)
    
    if (cadena.lower() != "python"):
         mistakes +=  1
         
print ("Has tenido " + str(mistakes)+ " errore(s)")
print ("Veamos tu evolucion")
t.sleep(3)

#Creamos el grafico
x = [1,2,3,4,5]
y = times
plt.plot(x,y)

legend = ["1" , "2" , "3" , "4" , "5"]
plt.xticks(x,legend)
plt.ylabel("Tiempo en segundos")
plt.xlabel("Intentos")
plt.title("Tu evolucion escribiendo")
plt.show()
