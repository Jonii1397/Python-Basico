Para usar cualquier módulo es importante que previamente los instalemos desde la terminal y luego importemos con la palabra import, anteriormente hemos usado los módulos math y random, por ejemplo. 
![[Pasted image 20241007100134.png]]
Se utiliza para crear una interfaz gráfica para los programas en Python https://wxpython.org/index.html
Para trabajar con base de datos SQL puedes usar https://www.sqlalchemy.org/
Biblioteca de algoritmos y herramientas matemáticas para cálculos científicos.
https://scipy.org/
Juegos en python https://www.pygame.org/news
Para hacer machine learning se utiliza https://scikit-learn.org/stable/
Ahora veamos algunos:
==Time==
	time.localtime()- Fecha actual. .tm_hour , tm_min etc para ver hora, minutos, segundos etc..
	Para los días es de 0 a 6 siendo 0 lunes y 6 domingo.
	Todo lo tenemos aqui:
	https://docs.python.org/3/library/time.html
	Con la funcion time.sleep() podemos atrasar la siguiente línea de código x segundos que es el argumento de la función.
==Matplotlib==
	Es utilizado para hacer gráficos en python.
	![[Pasted image 20241007100335.png]]
	https://www.w3schools.com/python/matplotlib_pyplot.asp
	https://matplotlib.org/stable/
	Cualquier pagina web puede ayudarnos a todas las funciones disponible de este módulo.
	Ejercicio de time y matplotlib.
==Request==
	import requests
	Sirve para hacer peticiones HTTP en Python.	
	Con requests.status_code obtenemos los códigos de estado.
	Los mas importantes son :
	200 - Todo ok
	403- Prohibido, no se ha enviado la autenticación correctamente.
	404- No encontrado
	500-Internal server error
	Con el headers obtenemos la cabecera de la información
	![[Pasted image 20241007113108.png]]
	El header tiene parametros como ["Date"]
==Solicitud HTTP a API==
	Api significa interfaz de programación de aplicaciones. Están detrás de la mayoría de las aplicaciones de nuestro teléfono.
	Todas las API devuelven una respuesta en formato JSON.
==JSON==
	Notación de objetos de Java Script
	Son objetos de tipo de diccionario.
	El atributo loads convierte el text de una solicitud en formato JSON, te lo devuelve en formato diccionario.
	Instalamos pprint para facilitar su lectura si sale un error puede que esté instalado por defecto.
	.dumps convierte el diccionario en json.
==Archivos==
	Creamos un archivo de texto y lo guardamos como tal, en la carpeta de los ejercicios.
	Con el comando open abrimos el txt y poner la ruta, si se encuentra en la misma solo haría falta poner le nombre, si no, su ruta correspondiente y como segundo parámetro lo que vas a hacer, r -read, w-write etc. Por defecto se abre en lectura y podríamos omitir ese segundo parámetro.
	![[Pasted image 20241007133753.png]]
	Aquí el ejemplo con el write que lo que hace es sobrescribirlo ![[Pasted image 20241007133934.png]]
	Con a de append, añade texto a lo que ya está escrito.
	![[Pasted image 20241007134114.png]]
	Con x creamos un archivo de texto que no está creado.
	![[Pasted image 20241007134247.png]]
==Lectura Excel==

