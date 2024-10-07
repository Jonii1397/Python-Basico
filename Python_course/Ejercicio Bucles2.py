import random
print("Juego de adivinanza con colores.Prueba con amarillo,rojo,azul,blanco,negro,marron o verde")

colors = ["amarillo","rojo","azul","blanco","negro","marron","verde"]

while True:
    color = colors[random.randint(0, len(colors)-1)]
    guess = input("Puedes adivinar el color que estoy pensando? Prueba: ")

    while True:
        if(color == guess.lower()):
            break
        else:
            guess = input("Has fallado! Intentalo de nuevo: ")

    print ("Has acertado, estaba pensando en el ", color)

    volver = input("Quieres volver a jugar? Escribe 'no' para salir ")

    if volver.lower() == 'no':
        break
print("Gracias por jugar")
    
