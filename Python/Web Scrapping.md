Web Scraping es una **técnica utilizada mediante programas de software para extraer información de sitios web**.
Para su correcto uso hay que instalar previamente 3 librerías : Requests , lxml y Beautifulsoup4
Con el método .get de request , su parámetro ha de ser la página web que queremos "raspar" y se lo asignamos a una variable web
Creamos una variable datos = bs4.BeautifulSoup(web, 'lxml')
Ahora podemos imprimir cualquier etiqueta de html , por ejemplo, el título :
print(datos.select('etiqueta html'))->Si hay mas de uno devuelve una lista que podemos filtrar por índices y con el método .getText() obtenemos solamente el texto que estemos buscando.

Ahora bien, para obtener elementos de una clase
![[Pasted image 20241024090507.png]]
columna_lateral = sopa.select('.post-title-container a')  
for p in columna_lateral:  
    print(p.getText())
Esto seria un ejemplo de coger todos los a dentro del div post-tittle-containter y mediante el for imprimimos el texto de cada uno.

Para el tema de las imágenes es algo más sencillo
![[stemdo.udemy.com_course_python-total_learn_lecture_29276834.png]]
Con este método coge la imagen, y la pasa de binario a guardarla en tu ruta del proyecto.