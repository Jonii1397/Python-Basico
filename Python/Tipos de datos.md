==String (cadena)==
	Pueden ser una frase, palabra o letra.
	![[Pasted image 20241003114711.png]]
	Los números que no vayan a ser usados para cálculos también es convenientes almacenarlos como un tipo String.
	Con cadena[0] , ese 0 es el indice de la cadena y se muetra el carácter que corresponde con esa posicion.
	len(cadena) obtiene la longitud del String.
	Si por ejemplo queremos más de un carácter sería cadena[0 : 2] y si ponemos [-1 ] es el último carácter y si quedas [-2 : ] será desde esa posición hasta el final y al revés [ : 2] desde el principio hasta el tercer, recuerda que el primero es 0.
	Si añadimos un tercer argumento quiere decir cada cuantos caracteres salto, es decir [2:10:2] del 2 al 10 saltándose 2
	El segundo índice de las llaves no está incluido.
	No se puede concatenar un string con otro tipo de dato sin previamente convertirlo a String, es decir,
	"hello" + 123 no funcionaria pero "hello " + str(123) si.
	String tiene varios métodos como:
	upper()-Mayusculas
	lower()-Minusculas
	split()-Separar en partes(lista)
	join()-Unir items usando separador
	find()-Encontrar sub-string
	replace()-Reemplazar sub-string
	Ejercicio 04-String.
	Ejercicio 05-String.
==Numbers==
	Pueden ser enteros o decimales ( int y float)
	Poner 2 ** 2 es 2 elevado a 2
	Se pueden hacer sumas, restas , multiplicaciones, divisiones o coger el resto( + , - , * , / , %) siendo cada símbolo correspondiente a lo anterior pudiendose sumar enteros y floats.
	La división al piso se representa con // es decir 7 al piso de 2, daria 3 en lugar de 3.5
	Y la raiz cuadrada es **0.5
	El comando round redondea y con round ( 3.14151 , 2) redondea a dos decimales.
	Con import math importamos la librería de math.
	math.factorial(3) haría 3 * 2 , el 4, 4 * 3 y así sucesivamente.
	math.ceil redondea siempre hacia arriba.
	math.floor redondea siempre hacia abajo.
	math.log(20) devuelve el algoritmo natural de 20 a la base
	math.pi
	python math module para aprender mas
	https://docs.python.org/3/library/math.html
	num1=10  
	num2=25  
	num1=num2  
	print(num1, num2)
	El primero siempre coge el valor del segundo , esto seria 25 y 25
	Ejercicio 06-Number.
==Listas y Tuplas.==
	Son los demoniados arrays, para crear una lista de alumnos haríamos  lo siguiente:
	Alumno = ["Joni", "Alba" , "Jose"]
	Se puede hacer como con los tipo numbers, si pones alumno[0] devuelve Joni y si pones len(alumno) devuelve 3 que es la longitud del array.
	Para modificar una lista pondríamos alumno[3] = "Lydia" y para añadir usaríamos el método append, alumno.append("Nombre") y para insertarlo en una posición específica es alumno.insert(0,"Madre Oscar").
	alumno.pop() elimina el último integrante de la lista y con alumno.remove("Oscar") , busca a ese en la lista y lo elimina.
	.sorted->Ordena la lista
	frutas.pop(2)->Elimina el tercer elemento, el pop funciona con indices de esa manera.
	Dos listas se pueden fusionar pero nunca una lista se puede fusionar con una tupla.
	Si es algo que no va a cambiar nunca es mejor usar la tupla meses = ("enero", "febrero", etc)
	Esto no se puede modificar igual que una lista.
	Con mi_lista = list(mi_tupla) pasamos una tupla a una lista.
	 sorted(set(palabra)) pasa una lista ordenada a un set y elimina las duplicadas
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
	.key()->Devuelve todas las claves
	.values()->el valor de las claves
	.items()->Separados por clave,valor
	mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
	print(mi_dict["puntos"]["points2"][1])->Devuelve 300
==Boolean==
	bandera = True,False. Han de ir siempre con mayúsculas.
	Comparaciones básicas :
		> , >= Mayor o mayor igual que
		< , <= Menor o menor igual que
		== Igual que
		!= No igual
	Ejercicio Boolean
==Sets==
	Conjunto de datos ordenados de elementos únicos {'a','b','c',etc}
	set(1,2,3,4,5,6)
	mi_set = ([1,2,3])
	Los elementos no están ordenados en índices.
	Podemos unir varios sets con el método .union() y .add() para añadir un elemento
	.discard() ->eliminar un elemento  y .pop() elimina uno aleatorio al no estar indexado.
	