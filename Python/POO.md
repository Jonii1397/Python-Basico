El código que define un objeto es denominado *clase*.
Todo puede estar definido por una clase (pájaro, silla, mesa etc..)
Por ejemplo un pájaro tiene unas características como color, tipo, edad tamaño , etc.. esto se conoce como *atributos*.
Las clases tienen un conjunto de funcionalidades llamadas *métodos* como volar, comer , piar.
Muchos pájaros serían objetos, cada instancia de la clase pájaro se denomina *objetos*.

Los 6 principios de la POO son:
1. Herencia
	1. Podemos crear una clase Hija que herede de la clase Padre, para que ocurra esto valdría con que en los argumentos de la clase Hija pasemos como parámetros la clase de la que quiere heredar, en este caso , Padre.
	2. Hereda métodos y atributos y puede modificarlos o crear unos nuevos.
	3. El método basses te dice de quien heredas y subclasses a quien le das la herencia.
	4. ![[stemdo.udemy.com_course_python-total_learn_lecture_28728888.png]]
2. Polimorfismo(Muchas-formas)
	1. Objetos de diferentes formas pueden compartir el mismo nombre de métodos.
	2. ![[stemdo.udemy.com_course_python-total_learn_lecture_28743852.png]]
	3. Se puede hacer mediante un loop while y distinguiria cada método de cada objeto, con una función pero declarando un objeto por cada instancia a esa función.![[stemdo.udemy.com_course_python-total_learn_lecture_28743852 (1).png]]
	4. 
3. Cohesión
	1. https://escueladirecta-blog.blogspot.com/2021/09/cohesion-pilares-de-la-programacion.html
4. Abstracción
	1. https://escueladirecta-blog.blogspot.com/2021/10/acoplamiento-pilares-de-la-programacion.html
5. Acoplamiento
	1. https://escueladirecta-blog.blogspot.com/2021/10/abstraccion-pilares-de-la-programacion.html
6. Encapsulamiento
	1. https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html
#### Clases
Se define con class Dinosaurio: y el objeto de la clase pájaro sería 
mi_dino = Dinosaurio()
![[Pasted image 20241016155611.png]]
Tenemos creada la clase Dinosaurio y 3 instancias a esa clase.

#### Atributos
Existen dos tipos:
1)Los de clase. Todos los objetos tendrán ese atributo.
2)Los de instancia. Pertenecen únicamente a cada objeto.
![[Pasted image 20241016160234.png]]
Los atributos de clase van justo debajo de la clase sin el constructor. 
alas = True y puede ser print(Pajaro.alas) o print(mi_pajaro.alas)
![[Pasted image 20241016161429.png]]

#### Métodos
Se define como una función en Python.
![[stemdo.udemy.com_course_python-total_learn_lecture_28722636.png]]
El argumento self es obligatorio en cada método.
Para llamar a esos métodos valdría con la instancia . y el método que queramos invocar.

#### Tipos de métodos
Los decoradores nos permiten crear distintos tipos de métodos : 

1.Métodos de instancia. Son aquellos métodos que hemos visto anteriormente , definidos por self y que luego pueden ser llamados.
1. Acceden y modifican atributos del objeto
2. Acceder a otros métodos
3. Modificar el estado de la clase

![[stemdo.udemy.com_course_python-total_learn_lecture_28726342 (1).png]]
El método pintar_negro hace referencia a la primera característica de los métodos de instancia ya que accede y modifica un atributo.
El método volar llama a otro método piar y piolin.alas = False modifica el estado de la clase, cambiando su valor.

2.Métodos de clase -> @classmethod. Se sustituye self por *cls*, pueden modificar los atributos de la clase.
Está relacionado con la clase en sí misma .No hace falta una instancia para ejecutarlo

![[stemdo.udemy.com_course_python-total_learn_lecture_28726342 1.png]]
(Haría falta la cantidad de huevos en los paréntesis)

3.Métodos estáticos -> @staticmethod. Sólo puede recibir parámetros.
No pueden acceder a ningún tipo de atributo.
![[stemdo.udemy.com_course_python-total_learn_lecture_28726342 1.png]]

#### Herencia extendida
![[stemdo.udemy.com_course_python-total_learn_lecture_28733770.png]]
El método super hace que no tengamos que volver a declarar los atributos de instancia de la clase que hemos heredado.
La clase pájaro que hereda de animal puede tener métodos propios, métodos heredados pero modificados y atributos propios, por ejemplo la altura_vuelo es perteneciente a los pájaros pero no a todos los animales.
Y la herencia múltiple es que Pajaro pueda heredad de Animal y Ave, por ejemplo y Pajaro ser la 'clase padre' de Canario.
![[stemdo.udemy.com_course_python-total_learn_lecture_28733770 (1).png]]

#### Métodos especiales 
![[stemdo.udemy.com_course_python-total_learn_lecture_28744840.png]]
Habría que añadir print(len(mi_cd)), str(mi_cd) y del mi_cd este último se ve en pantalla.
