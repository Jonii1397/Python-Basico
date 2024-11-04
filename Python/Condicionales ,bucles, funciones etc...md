==Condicionales==
	==If==
	Compara una serie de cosas y dependiendo de la condicion devuelve una cosa u otra.
	Esto es un ejemplo 
	![[Pasted image 20241003152220.png]]
	Vemos que aparece un else, quiere decir si no. Si no se cumple lo de arriba entonces muestrame otro mensaje
	Además esta el elif para añadir otra condición antes del else.
	Aquí otro ejemplo:
	![[Pasted image 20241003152440.png]]
	Primero se comprueba si son iguales, si no si uno es mayor que otro y si no, muestra un mensaje distinto.
	Se pueden ir anidando if dentro de otro if y no hay problema alguno.
	==AND y OR==
	Un and dentro de un if quiere decir que ambas condiciones han de ser correctas para entrar en el bucle, y or que una de las dos sea válida al menos.
	Aqui tenemos un ejemplo con la edad de antes con or
	![[Pasted image 20241003154010.png]]
	Con and habría que meter otro ejemplo ya que las edades es algo tosco para que cumplan dos requisitos.
	Dentro de un if pueden haber varias and y or o ambos, debemos poner parentesis en los ejemplos.
	in si esta dentro y not in si no está. 
	frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
	palabra1 = "éxito"
	palabra2 = "tecnología"
	mi_bool = (palabra1 not in frase) and (palabra2 not in frase)
	print(mi_bool)
	Ejercicio de los condicionales.
==Bucles==
	Son líneas de repetición, se utilizan para repetir líneas de código varias veces.
	Se utilizan para iterar listas, tuplas etc...
	==While==
	El bucle while quiere decir que mientras se cumpla, siga haciendo lo que sea. 
	Ver el ejemplo de while en los ejercicios.
	Dentro de un bucle puede haber o contener una serie de condicionales.
	Para salir de un bucle podemos usar break dentro del if, si cumple la condición automáticamente sale de ahí.
	==For==
	Trabajan como iteradores de secuencias.
	![[Pasted image 20241003163716.png]]
	Va a ir recorriendo y va a asignar a la variable post el text que hay en esa secuencia cada vez que lo recorre, si ejecutamos esto el resultado es este.
	![[Pasted image 20241003163804.png]]
	La sentencia continue en un for, salta al siguiente recorriendo si por ejemplo, cumple una condición(un campo vacío)
	Los for se pueden anidar también
	continue sigue el bucle en una condicion y break abandona ese bucle.
==Validación de datos y manejo de errores==
	Por ejemplo, para que una nota de un examen no sea inferior a 0 o superior a 10.
	Véase el ejemplo condicional y validación de los ejercicios.
	Para el manejo de errores vamos a usar la sentencias try y except.
	En el ejemplo y ejercicio de manejo de errores vemos como podemos usarlo.
==Funciones==
	Con las funciones podemos reutilizar bloques de código en todo nuestro programa.
	Para crear una función utilizamos def prueba_funcion()
	Pueden contener argumentos dentro de los paréntesis.
	Cuando creamos una función el código no se ejecuta y para ejecutarla debemos invocar la función
	![[Pasted image 20241007090428.png]]
	print, float, round etc son funciones incorporadas en python.
	Otro ejemplo de funciones pero con tuples sería este :
	![[stemdo.udemy.com_course_python-total_learn_lecture_28370608.png]]
	Con el método * args podemos definir funciones cuyos números de argumentos sea variado, es decir, no fijo.
	
La función format ayuda a formatear cadenas para no hacer unas concatenaciones largas o formatear los tipos de datos.
Por ejemplo:
Si tenemos color_auto = 'rojo' y matricula = 0976JCM
print("Mi auto es {} y de matricula {}".format(color_auto,matricula)) es importante que sea correspondiente al orden a las llaves.
Luego llegaron las cadenas literales
print(f"Mi auto es {color_auto} y de matricula {matricula}")
El método index() nos permite conocer el índice de un carácter.
mi_texto = 'hola'
mi_texto.index("o"), si ponemos mi_texto.index("o",3) quiere decir que va a buscar una o a partir del 4 carácter, recordamos que empieza en 0 y si ponemos después otro parámetro busca esa letra entre esos dos índices.
También podemos saber que carácter hay en un índice
mi_texto[3]
Las funciones min y max te devuelven los valores minimos y maximos de una serie de números o de una lista.
min = min(list()) y con max lo mismo.
sum, suma los valores y abs te da el valor absoluto.

Para el caso de los strings con min y max , es igual. Una lista de nombres devuelve el primero alfabéticamente o el último y para un string primero comprueba mayúsculas y luego minúsculas.

==Enumerate.==
	Fácil accesibilidad a los índices
	lista = [1,2,3,4,5]  
	for item in enumerate(lista):  
	   print(item).
	RESULTADO
	(0, 1)
	(1, 2)
	(2, 3)
	(3, 4)
	(4, 5)
==ZIP==
	Se usa para combinar dos listas.
	El resultado es una lista con tuplas. Como esto 
	![[Pasted image 20241014162149.png]]
	Llega al fin de la lista mas corta por si no hay los mismos elementos en unos u otros.
