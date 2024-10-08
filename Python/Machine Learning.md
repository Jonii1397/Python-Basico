Es prácticamente el uso de un ordenador para generar conocimiento a partir de unos datos, como por ejemplo reconocimiento de imágenes.
Forma parte de la inteligencia artificial.
Hay que instalar pip install scipy, scikit-learn y ipython y "ipython[notebook]"
Para ejecutar jupyter notebook valdrá con escribir eso mismo desde la terminal y accederemos a un servidor local para poder escribir código.
Dentro de la carpeta de los ejercicios hay una carpeta llamada MachineLearning creada desde el book.
Coomand, shift p para abrir los atajos en el entorno.
Iris del biólogo Ronald Fisher fue un experimento basado en observar 150 flores.Buscar más información para comprender este ejemplo.
![[Pasted image 20241007153712.png]]
el target 0 del primer elemento se asocia a la primera fila de datos y  sucesivamente
![[Pasted image 20241007153821.png]]
El 0 se asocia a setosa, el 1 a versicolor y 2 a virginica.
Para ver esto mas a fondo en la primera imagen poner print(iris)
El comando print(iris.data.shape) nos da el número de filas y columnas.

KNN
**K-Nearest-Neighbor** es un algoritmo basado en instancia de tipo supervisado de Machine Learning. Puede usarse para clasificar nuevas muestras (valores discretos) o para predecir (regresión, valores continuos). Al ser un método sencillo, es ideal para introducirse en el mundo del  Aprendizaje Automático. Sirve esencialmente para clasificar valores buscando los puntos de datos “más similares” (por cercanía)

![[Pasted image 20241007155400.png]]
Como podemos observar el predict y un dato de iris anterior, predice que es de la flor cuyo indice es 0, es decir, setosa

Para lo siguiente vemos este ejemplo
![[Pasted image 20241007164255.png]]

Las dos primeras lineas : en Este código de Python, proveniente de la biblioteca scikit-learn, se utiliza comúnmente en el campo del aprendizaje automático para preparar los datos antes de entrenar un modelo. En esencia, lo que hace es **dividir un conjunto de datos en dos partes:** una para entrenar el modelo y otra para evaluarlo.
Lo siguiente - **Imprime la forma (shape) del arreglo `X_test`:** Esto significa que te mostrará las dimensiones de este arreglo en la consola.
- **La forma de un arreglo** generalmente se expresa como una tupla de números, donde cada número representa el tamaño de una dimensión. En el caso de matrices (como suelen ser los datos en machine learning), la forma normalmente tiene dos elementos:
    - **Primer elemento:** El número de filas, que corresponde al número de muestras o ejemplos en tu conjunto de prueba.
    - **Segundo elemento:** El número de columnas, que corresponde al número de características o atributos de cada muestra.
Las 3 siguientes lineas - - `knn`: Representa la instancia del modelo KNN que has creado previamente (usualmente utilizando `from sklearn.neighbors import KNeighborsClassifier` y definiendo parámetros como el número de vecinos).
    - `X_train`: Corresponde a las características de entrenamiento. Son los datos que tu modelo utilizará para "aprender" los patrones y relaciones entre las variables.
    - `y_train`: Representa la variable objetivo de entrenamiento. Son los valores que el modelo intentará predecir.
- **Función `fit`:** Esta función del modelo KNN se encarga de analizar los datos de entrenamiento y construir el modelo interno que utilizará para realizar las predicciones. En esencia, el modelo aprende de las relaciones entre las características y la variable objetivo en el conjunto de entrenamiento.

**2. predictions = knn.predict(X_test)**

- **Realización de predicciones:**
    - `knn`: Sigue siendo la instancia del modelo KNN previamente entrenado.
    - `X_test`: Corresponde a las características de prueba. Estos son datos nuevos e invisibles para el modelo durante el entrenamiento.
    - `predictions`: Esta variable almacenará las predicciones del modelo KNN para cada muestra en `X_test`.
- **Función `predict`:** Una vez que el modelo ha sido entrenado con `fit`, la función `predict` se utiliza para generar predicciones en nuevos datos. El modelo KNN analizará cada muestra en `X_test` y la comparará con sus "vecinos más cercanos" en el conjunto de entrenamiento. Basado en esa comparación, predecirá la clase o valor más probable para dicha muestra.
- Y las últimas líneas - `metrics.accuracy_score`: Esta función calcula la precisión del modelo.
- `y_test`: Contiene los valores reales de la variable objetivo para el conjunto de prueba.
- `predicciones`: Contiene las predicciones realizadas por el modelo para el conjunto de prueba.
- La función calcula la proporción de predicciones correctas entre el total de predicciones.