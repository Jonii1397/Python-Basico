number = input("Type a number: ")

try:
    number = float(number)
    print("El número es número")
except:
    print("Invalid number")
