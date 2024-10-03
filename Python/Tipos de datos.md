==String (cadena)==
	Pueden ser una frase, palabra o letra.
	![[Pasted image 20241003114711.png]]
	Los números que no vayan a ser usados para cálculos también es convenientes almacenarlos como un tipo String.
	Con cadena[0] , ese 0 es el indice de la cadena y se muetra el carácter que corresponde con esa posicion.
	len(cadena) obtiene la longitud del String.
	Si por ejemplo queremos más de un carácter sería cadena[0 : 2] y si ponemos [-1 ] es el útlimo carácter y si quedas [-2 : ] será desde esa posición hasta el final y al revés [ : 2] desde el principio hasta el tercer, recuerda que el primero es 0.
	El segundo indice de las llaves no está incluido.
	No se puede concatenar un string con otro tipo de dato sin previamente convertirlo a String, es decir,
	"hello" + 123 no funcionaria pero "hello " + str(123) si.
	Ejercicio 04-String.
	Ejercicio 05-String.

==Numbers==
	Pueden ser enteros o decimales ( int y float)
	Poner 2 ** 2 es 2 elevado a 2
	Se pueden hacer sumas, restas , multiplicaciones, divisiones o coger el resto( + , - , * , / , %) siendo cada símbolo correspondiente a lo anterior pudiendose sumar enteros y floats.
	El comando round redondea y con round ( 3.14151 , 2) redondea a dos decimales.
	Con import math importamos la librería de math.
	math.factorial(3) haría 3 * 2 , el 4, 4 * 3 y así sucesivamente.
	math.ceil redondea siempre hacia arriba.
	math.floor redondea siempre hacia abajo.
	math.log(20) devuelve el algoritmo natural de 20 a la base
	math.pi
	python math module para aprender mas
	[https://docs.python.org/3/library/math.html]()
	Ejercicio 06-Number.

==Listas y Tuplas.==
	Son los demoniados arrays, para crear una lista de alumnos haríamos  lo siguiente:
	Alumno = ["Joni", "Alba" , "Jose"]
	Se puede hacer como con los tipo numbers, si pones alumno[0] devuelve Joni y si pones len(alumno) devuelve 3 que es la longitud del array.
	Para modificar una lista pondríamos alumno[3] = "Lydia" y para añadir usaríamos el método append, alumno.append("Nombre") y para insertarlo en una posición específica es alumno.insert(0,"Madre Oscar").
	alumno.pop() elimina el último integrante de la lista y con alumno.remove("Oscar") , busca a ese en la lista y lo elimina.
	Dos listas se pueden fusionar pero nunca una lista se puede fusionar con una tupla.
	Si es algo que no va a cambiar nunca es mejor usar la tupla meses = ("enero", "febrero", etc)
	Esto no se puede modificar igual que una lista.
	Ejercicio 7 y 8 de listas.

==Diccionarios==
	Son como las listas pero los elementos están ordenados por llaves.
	persona = { "nombre" : "Joni" , "apellidos" : "Ramón" , "año de nacimiento" : "1997" }
	persona["nombre"] daria como resultado 'Joni'.
	persona["nombre"] = "Jonathan" sería para cambiar el valor de la clave nombre.
	Para añadir un campo más valdría como el comando de arriba y dandole el valor a esa nueva clave.
	Dentro de un mismo diccionario se pueden añadir listas, tuplas etc...
	El método .get devuelve el valor de la propiedad y si no lo encuentra podemos devolver un mensaje de error. He aquí un ejemplo : result = persona.get(user , "Esta información no está disponible")
	Con persona.clear() borramos toda información de un diccionario.

==Boolean==
	bandera = True,False. Han de ir siempre con mayúsculas.
	Comparaciones básicas :
		> , >= Mayor o mayor igual que
		< , <= Menor o menor igual que
		== Igual que
		!= No igual
	Ejercicio Boolean