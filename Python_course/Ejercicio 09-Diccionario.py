print("Información personal")
persona = {"nombre" : "Jonathan" , "genero" : "Masculino" , "edad" : "26" , "direccion" : "Montijo" , "tlf" : "689067005"}

user = input("Introduce la información que quieras saber: ")

result = persona.get(user , "Esta información no está disponible")

print(result)
