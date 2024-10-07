#En este ejercicio no están implementadas las validaciones para las entradas de datos
import json
import pprint
import requests
import random
import html
url = "https://opentdb.com/api.php?amount=1"
endGame = ""
score = 0
incorrect_score = 0
while (endGame != 'quit'):
    r = requests.get(url)
    if(r.status_code != 200):
        endGame=input("Hay un problema, pulsa enter para probar otra vez o 'quit' para salir")
    else:
        answer_number = 1
        data = json.loads(r.text)
        #Cogemos los datos que necesitamos del json
        #pprint.pprint(data) para ver el json
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        answers.append(correct_answer)
        #Barajamos el array de respuesta porque siempre se añadiria la correcta al final
        random.shuffle(answers)

        print(html.unescape(question + "\n"))

        for answer in answers:
            print(str(answer_number) + "-" + html.unescape(answer))
            answer_number += 1

        user_answer = input("\nEscribe el número de la respuesta correcta: ")
        user_answer = answers[int(user_answer) - 1]

        if(user_answer == correct_answer):
            print("Enhorabuena, has acertado")
            score += 1
        else:
            print("Has fallado, la respuesta correcta era : " + correct_answer)
            incorrect_score += 1
        print("\n################")
        print ("Respuestas correctas : " + str(score) )
        print ("Respuestas incorrectas : " + str(incorrect_score) )

        print("################")

        endGame = input("Pulsa enter para volver a jugar o 'quit' para salir ").lower()
print("Gracias por jugar")
