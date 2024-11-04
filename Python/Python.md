Descargamos python en python.org
Todos los comandos y sentencias estarán en la nota IDE además de un resumen de lo que son las variables.
En la consola CMD escribimos python y ya se ejecuta.
Se puede escribir desde una simple operación matemática hasta un mensaje, con print<"Hola"> y para salir de la consola quit<>.
Nuestro entorno de desarrollo será IDLE.
Python es sensible a la sangría y una simple tabulación puede dar lugar a error.
Los tipos de datos están en otro archivo
barra \n-salto de linea
barra \t-Sangria de 4 caracteres
Cuando asignemos nombre a una variable es importante que el valor corresponda con su nombre haciendo de tu código un código legible y limpio.
Para instalar paquetes externos que no contengan las librerías de python vamos primero a google y buscamos la que nos interese o necesitemos.
Posteriormente desde el cmd de windows escribimos :
*pip install "nombre_modulo"*
Las paginas mas fiables son python.org o Pypi
Los módulos no son más que archivos .py, que almacenan funciones, variables y clases, y pueden ser importado por otros. Los paquetes agrupan estos módulos en carpetas, de los cuales uno debe ser __init__.py
Importar un módulo -> import modulo1
Importar una función del módulo ->from modulo1 import funcion
Ejecutar desde la consola -> ruta > python modulo1.py Importar un módulo de un (sub) paquete -> 
from paquete.subpaquete import modulo3
Todos los paquetes, para ser considerados como tales, deben contar con un archivo __init__.py (constructor)
Python para el manejor de errores usa el *try except finally*
Donde el primero es intenta esto(try), si sale mal haz esto(except), pase lo que pase haz esto(finally).
![[stemdo.udemy.com_course_python-total_learn_lecture_28848218.png]]
En el except se puede poner el tipo de error y soltar un mensaje dependiendo del tipo, eso si, un except por cada tipo de error que queramos manejar.

#### Decoradores
![[stemdo.udemy.com_course_python-total_learn_lecture_28854194.png]]
Para ejecutar la función sin la "decoración" eliminamos los arrobas y declaramos
mayuscula_decorada  = decorar_saludo(mayusculas)
mayuscula_decorada("Hola , esto es la prueba")

#### Generadores 
Son un tipo especial de función que en vez de devolvernos un valor terminado va produciendo ese valor poco a poco en medida de que lo vayamos necesitando.
Sustituimos la palabra clave return por *yield* que viene a significar, producir.
![[stemdo.udemy.com_course_python-total_learn_lecture_28863404.png]]
