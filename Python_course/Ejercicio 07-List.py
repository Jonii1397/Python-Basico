print ("Este ejercicio pregunta por tu cumpleaños en el formato DD-MM-YYYY e imprime tu mes de nacimiento")

meses = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

cumple = input("Introduce tu fecha de cumpleaños en formato DD-MM-YYYY: ")

mescumple = int(cumple[3:5]) -1
bd_month = meses[mescumple]

print("Naciste en : " , bd_month)
