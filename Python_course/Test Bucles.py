Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Alumno ["Joni", "Alba" , "Jose"]
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Alumno ["Joni", "Alba" , "Jose"]
NameError: name 'Alumno' is not defined
Alumno = ["Joni", "Alba" , "Jose"]
Alumno
['Joni', 'Alba', 'Jose']
alumno = Alumno
alumno[3] = "Lydia"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    alumno[3] = "Lydia"
IndexError: list assignment index out of range
alumno[2] = "Lydia"
alumno
['Joni', 'Alba', 'Lydia']
alumno.append = "Jose"
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    alumno.append = "Jose"
AttributeError: 'list' object attribute 'append' is read-only
alumno.append = ("Jose")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    alumno.append = ("Jose")
AttributeError: 'list' object attribute 'append' is read-only
alumno.append("Jose")
alumno
['Joni', 'Alba', 'Lydia', 'Jose']
alumno.append("Hobbit")
alumno
['Joni', 'Alba', 'Lydia', 'Jose', 'Hobbit']
alumno.insert(0,"Madre Oscar")
alumno
['Madre Oscar', 'Joni', 'Alba', 'Lydia', 'Jose', 'Hobbit']
alumno.pop(0)
'Madre Oscar'
alumno.pop
<built-in method pop of list object at 0x000001B2237980C0>
alumno.pop()
'Hobbit'
alumno
['Joni', 'Alba', 'Lydia', 'Jose']
alumno2 = ["Raul" , "Adrian"]
alumno + alumno2
['Joni', 'Alba', 'Lydia', 'Jose', 'Raul', 'Adrian']
meses.append("otro")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    meses.append("otro")
NameError: name 'meses' is not defined
meses = ("en" ,"feb" )
meses.append("otro")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    meses.append("otro")
AttributeError: 'tuple' object has no attribute 'append'
meses.insert("otro")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    meses.insert("otro")
AttributeError: 'tuple' object has no attribute 'insert'

====== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 08-List.py =====
Lista de personas añadiendo un usuario
La lista es : ['Joni', 'Alba', 'Jose']
Introduce su nombre: Lydia
La lista nueva sería : ['Joni', 'Alba', 'Jose', 'Lydia']

====== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 07-List.py =====
Este ejercicio pregunta por tu cumpleaños en el formato DD-MM-YYYY e imprime tu mes de nacimiento
Introduce tu fecha de cumpleaños en formato DD-MM-YYYY
====== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 07-List.py =====
Este ejercicio pregunta por tu cumpleaños en el formato DD-MM-YYYY e imprime tu mes de nacimiento
Introduce tu fecha de cumpleaños en formato DD-MM-YYYY: 13-12-1997

====== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 07-List.py =====
Este ejercicio pregunta por tu cumpleaños en el formato DD-MM-YYYY e imprime tu mes de nacimiento
Introduce tu fecha de cumpleaños en formato DD-MM-YYYY: 13-12-1997
Naciste en :  Diciembre
persona { "nombre" : "Joni" , "apellidos" : "Ramón" , "año de nacimiento" : "1997" }
SyntaxError: invalid syntax
persona = { "nombre" : "Joni" , "apellidos" : "Ramón" , "año de nacimiento" : "1997" }
type(persona)
<class 'dict'>
ç
persona["nombre"]
'Joni'
persona["nombre"] = "Jonathan"
persona
{'nombre': 'Jonathan', 'apellidos': 'Ramón', 'año de nacimiento': '1997'}

== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py ==
Información personal
Introduce la información que quieras saber nombre
Traceback (most recent call last):
  File "C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py", line 6, in <module>
    print("El", user , "es" , persona["user"])
KeyError: 'user'

== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py ==
Información personal
Introduce la información que quieras sabernombre
Traceback (most recent call last):
  File "C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py", line 6, in <module>
    print("El", user , "es" , persona["user"])
KeyError: 'user'

== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py ==
Información personal
Introduce la información que quieras sabernombre
El nombre es Jonathan

== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py ==
Información personal
Introduce la información que quieras sabernombre
Traceback (most recent call last):
  File "C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py", line 6, in <module>
    result = user.get(user , "Esta información no está disponible")
AttributeError: 'str' object has no attribute 'get'

== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py ==
Información personal
Introduce la información que quieras sabernombre
El nombre es Jonathan

== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 09-Diccionario.py ==
Información personal
Introduce la información que quieras saber: name
El name es Esta información no está disponible

==== RESTART: C:/Users/jramon/Desktop/Python_course/Prueba if y booleans.py ====
Traceback (most recent call last):
  File "C:/Users/jramon/Desktop/Python_course/Prueba if y booleans.py", line 1, in <module>
    num1 = float("Introduce un primer numero ")
ValueError: could not convert string to float: 'Introduce un primer numero '

==== RESTART: C:/Users/jramon/Desktop/Python_course/Prueba if y booleans.py ====
Introduce un primer numero 4
Introduce un segundo numero 3
No son iguales ambos números

==== RESTART: C:/Users/jramon/Desktop/Python_course/Prueba if y booleans.py ====
Introduce un primer numero 4
Introduce un segundo numero 2
4.0 es mayor que 2.0

==== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 10- Boolean.py ===
Este programa comparara tu edad con la de un usuario
Introduce tu edad
==== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 10- Boolean.py ===
Este programa comparara tu edad con la de un usuario
Introduce tu edad: 20
El admin es mayor que el usuario

==== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 10- Boolean.py ===
Este programa comparara tu edad con la de un usuario
Introduce tu edad: 26
Tenéis la misma edad

==== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 10- Boolean.py ===
Este programa comparara tu edad con la de un usuario
Introduce tu edad: 40
El admin es menor que el usuario

==== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 10- Boolean.py ===
Este programa comparara tu edad con la de un usuario
Introduce tu edad: 26
El admin es menor

==== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio 10- Boolean.py ===
Este programa comparara tu edad con la de un usuario
Introduce tu edad: 25
Tenéis la misma edad o admin es mayor

=== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio condicionales.py ==
Calcular el indice de masa corporal de una persona
Introduce tu peso en kg: 70.1
Introduce tu altura en metros: 176
Poco peso

=============================================================================== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio condicionales.py ==============================================================================
Calcular el indice de masa corporal de una persona
Introduce tu peso en kg: 71.3
Introduce tu altura en metros: 1.76
Normal

=== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio condicionales.py ==
Calcular el indice de masa corporal de una persona
Introduce tu peso en kg: 71.3
Introduce tu altura en metros: 1.76
Mi IMC es  23.02
Normal

=== RESTART: C:/Users/jramon/Desktop/Python_course/Ejercicio condicionales.py ==
Calcular el indice de masa corporal de una persona
Introduce tu peso en kg: 70
Introduce tu altura en metros: 1.70
Mi IMC es  24.22
Normal

======== RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo While.py =======
introduce el nombre de una personaJoni
Traceback (most recent call last):
  File "C:/Users/jramon/Desktop/Python_course/Ejemplo While.py", line 6, in <module>
    people.insert(person)
TypeError: insert expected 2 arguments, got 1

======== RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo While.py =======
introduce el nombre de una personaJoni
Traceback (most recent call last):
  File "C:/Users/jramon/Desktop/Python_course/Ejemplo While.py", line 6, in <module>
    people.insert(person)
TypeError: insert expected 2 arguments, got 1

======== RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo While.py =======
introduce el nombre de una persona: Joni
introduce el nombre de una persona: Alba
introduce el nombre de una persona: Jose
introduce el nombre de una persona: osaar
introduce el nombre de una persona: paqui
['Joni', 'Alba', 'Jose', 'osaar', 'paqui']

======== RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo While.py =======
introduce el nombre de una persona: H
introduce el nombre de una persona: O
introduce el nombre de una persona: L
introduce el nombre de una persona: A
introduce el nombre de una persona: S
['H', 'O', 'L', 'A', 'S']

========= RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo For.py ========
Hola
Adios
Que tal
bien
amor

========= RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo For.py ========
Hola
Adios
Que tal

bien

amor

========= RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo For.py ========
Hola
Adios
Que tal
bien
amor

========= RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo For.py ========
Ejemplo con array
Hola
Adios
Que tal
bien
amor
-------------------------------------------
Ejemplo con string
H
o
l
a
 
m
e
 
l
l
a
m
o
 
J
o
n
a
t
h
a
n

========= RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo For.py ========
Ejemplo con array
Hola
Adios
Que tal
bien
amor
-------------------------------------------
Ejemplo con string
H
o
l
a
 
m
e
 
l
l
a
m
o
 
J
o
n
a
t
h
a
n

========= RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo For.py ========
Ejemplo con array
Hola
Adios
Que tal
bien
amor
-------------------------------------------
Ejemplo con string
H
o
l
a
 
m
e
 
l
l
a
m
o
 
J
o
n
a
t
h
a
n
-------------------------------------------
Ejemplo con numeros
0
1
2
3
4
5
6
7
8
9
10

========= RESTART: C:/Users/jramon/Desktop/Python_course/Ejemplo For.py ========
Ejemplo con array
Hola
Adios
Que tal
bien
amor
-------------------------------------------
Ejemplo con string
H
o
l
a
 
m
e
 
l
l
a
m
o
 
J
o
n
a
t
h
a
n
-------------------------------------------
Ejemplo con numeros
0
1
2
3
4
5
6
7
8
9
10
-------------------------------------------
Ejemplo con diccionario
nombre : Jonathan
genero : Masculino
edad : 26
