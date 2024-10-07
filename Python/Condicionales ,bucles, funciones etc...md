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
	