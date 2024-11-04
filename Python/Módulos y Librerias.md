Para usar cualquier módulo es importante que previamente los instalemos desde la terminal y luego importemos con la palabra import, anteriormente hemos usado los módulos math y random, por ejemplo. 
![[Pasted image 20241007100134.png]]
Y luego lo importemos en nuestro IDE
'from random import randint' si en el import ponemos un * , importamos todo de esa librería.
Se utiliza para crear una interfaz gráfica para los programas en Python https://wxpython.org/index.html
Para trabajar con base de datos SQL puedes usar https://www.sqlalchemy.org/
Biblioteca de algoritmos y herramientas matemáticas para cálculos científicos.
https://scipy.org/
Juegos en python https://www.pygame.org/news
Para hacer machine learning se utiliza https://scikit-learn.org/stable/
Algunos importes más utilizados de random son :
1)randint-> números aleatorios entre una serie de números->aleatorio = randint(1,50)
2)uniform-> valor aleatorio decimal entre una serie de numeros->aleatorio = round(uniform(1,5),1)
3)random-> numero aleatorio entre 0 y 1.
4)choice->Selección aleatoria de un elemento dentro de una lista.->aleatorio = choice(colores)
5)shuffle->Mezclar aleatoriamente elementos de una lista
![[stemdo.udemy.com_course_python-total_learn_lecture_28159238.png]]
La comprensión de listas es una forma mas eficiente de crear listas, sería asi : 
![[stemdo.udemy.com_course_python-total_learn_lecture_28161730.png]]
La forma de leer esto es, lista es igual a letra de cada letra de la palabra o sustituir palabra por la palabra, por ejemplo ' modulo ', funcionaria igual arrojando el resultado lista = ['m','o','d','u','l','o'] 
Incluso se puede meter un if dentro ![[stemdo.udemy.com_course_python-total_learn_lecture_28161730 (1).png]]

Ahora veamos algunos módulos más a fondo:
#### Time
time.localtime()- Fecha actual. .tm_hour , tm_min etc para ver hora, minutos, segundos etc..
Para los días es de 0 a 6 siendo 0 lunes y 6 domingo.
Todo lo tenemos aqui:
https://docs.python.org/3/library/time.html
Con la funcion time.sleep() podemos atrasar la siguiente línea de código x segundos que es el argumento de la función.
#### Matplotlib
Es utilizado para hacer gráficos en python.
![[Pasted image 20241007100335.png]]
https://www.w3schools.com/python/matplotlib_pyplot.asp
https://matplotlib.org/stable/
Cualquier pagina web puede ayudarnos a todas las funciones disponible de este módulo.
Ejercicio de time y matplotlib.
#### Request
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
#### Solicitud HTTP a API
Api significa interfaz de programación de aplicaciones. Están detrás de la mayoría de las aplicaciones de nuestro teléfono.
Todas las API devuelven una respuesta en formato JSON.
#### JSON
Notación de objetos de Java Script
Son objetos de tipo de diccionario.
El atributo loads convierte el text de una solicitud en formato JSON, te lo devuelve en formato diccionario.
Instalamos pprint para facilitar su lectura si sale un error puede que esté instalado por defecto.
.dumps convierte el diccionario en json.
#### Archivos
Manipular archivos con E/S->entrada/salida o I/O->Input/Output
Creamos un archivo de texto y lo guardamos como tal, en la carpeta de los ejercicios.
Con el comando open abrimos el txt y poner la ruta, si se encuentra en la misma solo haría falta poner le nombre, si no, su ruta correspondiente y como segundo parámetro lo que vas a hacer, r -read, w-write etc. Por defecto se abre en lectura y podríamos omitir ese segundo parámetro.
![[Pasted image 20241007133753.png]]
Aquí el ejemplo con el write que lo que hace es sobrescribirlo ![[Pasted image 20241007133934.png]]
Con el método write está también writelines y como parámetros hay que pasarle una lista.
f.writelines(['hola','mundo','aqui','estoy'])
![[stemdo.udemy.com_course_python-total_learn_lecture_28540623.png]]
Con a de append, añade texto a lo que ya está escrito.
![[Pasted image 20241007134114.png]]
Con x creamos un archivo de texto que no está creado.
![[Pasted image 20241007134247.png]]
Vamos a cerrar cada archivo cuando dejemos de utilizarlo con:
f.close().
y con readline() en singular leemos una línea de ese archivo
![[Pasted image 20241016095259.png]]
y con readlines() en plural , crea una lista con cada linea que tenga el archivo de texto.

	
#### Lectura Excel
En la carpeta de los ejercicios hay un archivo Excel que podemos usar de ejemplo.
pip install pandas y xlrd por separado.
Con panda.ExcelFile("excel.xlsx") Abrimos el documento y para ver el nombre de las hojas file.sheet_names si no funciona, instalar pip install openpyxl.
file.parse(''). Para ver la hoja que queremos.
Para imprimir una columna, se usa el punto y el nombre de cada columna.
El comando sum(), suma los elementos de una columna.
.loc[indice] imprime la fila correspondiente a ese índice.
sheet.set_index("Columna", inplace = True) Reemplaza el índice.
sheet = sheet.reset_index()-Resetea el índice.
sheet.loc[sheet["Amount"] == 99]Devuelve la fila que corresponda con esa condición, .idmax(), etc...
#### Directorios
Trabajar sobre archivos que se encuentran en directorios diferentes al de nuestro código requiere del soporte del módulo OS, que contiene una serie de funciones para interactuar con el sistema operativo. 
import os
Podemos importar ademas system -> system ('cls') elimina lo que hay antes de esto en consola.
os.getcwd(): obtiene y devuelve el directorio de trabajo actual. Será el mismo en el que corre el programa si no se ha modificado.
os.chdir(ruta): cambia el directorio de trabajo a la ruta especificada 
os.makedirs(ruta): crea una carpeta, así como todas las carpetas intermedias necesarias de acuerdo a la ruta especificada.
os.path.basename(ruta): dada una ruta, obtiene el nombre del archivo (nombre de base) os.path.dirname(ruta): dada una ruta, obtiene el directorio (carpeta) que almacena el archivo
os.path.split(ruta): devuelve una tupla que contiene dos elementos: el directorio, y el nombre de base del archivo. 
os.rmdir(ruta): elimina el directorio indicado en la ruta.
En Windows, es necesario indicar las rutas con dobles barras invertidas (\\) para que sean correctamente interpretadas por Python
Para el tema de las barras invertidas citado anteriormente esta sería una buena solución
![[stemdo.udemy.com_course_python-total_learn_lecture_28541365.png]]

Path vale para crear o mover archivos, enumerar archivos y crear rutas basadas en strings es decir, cualquier secuencia de strings transformarlos a una ruta de acceso.

#### Collections
from collections import *
Ayuda a completar y manipular los datos de una manera más eficiente.
Sus herramientas mas importantes son:
1. counter. Ayuda a contar los elementos de una lista convirtiéndolo en un diccionario. Podemos contar elementos de un string.
	1. ![[Pasted image 20241021153443.png]]
	
1. defaultdict. Diccionario por defecto. Asigna un valor a un elemento que no exista de ese diccionario. Se crea ese nuevo valor con esa clave default.
	1. ![[Pasted image 20241021153407.png]]
	
1. namedtuple. Tupla con nombres. Es una forma mas eficiente de encontrar una tupla.
	1. ![[stemdo.udemy.com_course_python-total_learn_lecture_28998004.png]]

#### Shutil
Sirve para mover directorios o archivos.
Un ejemplo sería import shutil
shutil.move('curso.txt'  , ruta)
Para entender Os ver directorios arriba.
También puede eliminar archivos de 3 maneras distintas :
	1. unlink eliminar un archivo en una ruta especifica(OS)
	2. rmdir elimina una carpeta vacía en una ruta.(OS)
	3. rmtree eliminar todo en una ruta(Shutil)
Este ultimo no almacena los archivos eliminados en la papelera, los borra sin dejar rastro alguno.
Para evitar esto existen algunas alternativas, lo primero es descargar el modulo send2trash con pip install que quiere decir 'enviar a la papelera'
send2trash.send2trash('archivo.txt')
El método walk funciona de esta manera 
![[stemdo.udemy.com_course_python-total_learn_lecture_28999432.png]]
#### DateTime
import datetime
Este módulo sirve para almacenar hora y fecha en variables , hacer cálculos de tiempo y mostrar en diferentes formatos la fecha, hora , ambas, etc...
tiempo = datetime.time(h, m , s  … ) lo que no se rellena se autoguarda con el valor 0. 
fecha = datetime.date(año , mes , día).
fecha.ctime()->formato tipo día de la semana , mes y día , la hora y el año
fecha.year()->el año
fecha.today()-> aunque hayamos escrito otra fecha, muestra el día que es al momento
fecha = fecha.replace(month = 11) -> reemplaza el mes escrito

#### Expresiones Regulares
Funciones :
	search( ): devuelve un objeto "match" que contiene información acerca del hallazgo si se encuentra en algún punto del string. 
	findall( ): devuelve una lista que contiene todos los hallazgos del patrón.
Para formar patrones, utilizamos los siguientes cuantificadores y caracteres especiales:
![[Pasted image 20241022132246.png]]
patrón = r'\d\d\d-\d\d\d-\d\d\d\d'
la r significa que es una expresión regular
la d significa dígitos ( 3 dígitos , un guion , 3 dígitos un guion y 4 dígitos)
también se puede mediante agrupación de dígitos. 
patrón = r '\d{3} - \d{4} '
![[stemdo.udemy.com_course_python-total_learn_lecture_29030152.png]]
La palabra se encuentra en el texto entre el índice 13 y el 18
.span a búsqueda -> La posición exacta
.start y .end -> Donde comienza y donde acaba

El texto contiene dos veces la palabra ayuda y solo muestra la posición de la primera.
Con el método .findall() nos muestra una lista con las dos palabras 'ayuda'
Con el ejemplo for hallazgo in re.findinter(patron,texto):
print (hallazgo.span()) -> Muestra la posicion para cada una de las palabras.![[stemdo.udemy.com_course_python-total_learn_lecture_29030152 1.png]]

Sin el .group() lo que hace es que muestra como lo anterior, la posición de los índices de la longitud de la búsqueda.![[stemdo.udemy.com_course_python-total_learn_lecture_29030152 (1).png]]
Esto es otro ejemplo de búsqueda y su visualización , esta vez con el compile y dentro de cada paréntesis los caracteres especiales.

#### Comprimir y descomprimir archivos
Se usan los módulos **zipfile** y **shutil** 
![[stemdo.udemy.com_course_python-total_learn_lecture_29030642.png]]
En esta imagen primero importamos el módulo y luego creamos una variable con zipfile.ZipFile y le damos el nombre que le queramos dar a nuestro archivo comprimido, con la extensión de comprimido que se quiera y con la 'w' de write para poder modificarlo.
Con el .write(''nombre_de_archivo_a_comprimir') dentro de esa ruta donde hemos creado el .zip y con .close() cerramos. (Como hacíamos con los archivos).
Para extraerlos , cambiamos la w por la r de read y tiene un método que es .extractall() que extrae todo lo que hay dentro y .extract('nombre del archivo que queramos sacar').

Con shutil :
![[stemdo.udemy.com_course_python-total_learn_lecture_29030642 (1).png]]Y para descomprimir con shutil es shutil.unpack_archive("carpeta zip", "carpeta de extraccion" , "extension").