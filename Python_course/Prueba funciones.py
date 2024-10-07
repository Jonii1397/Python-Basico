'''
def di_hola():
    print("Hola")
    
di_hola()
'''


def di_hola(person):
    print("Hola " + person + ", como estas?")
    
di_hola("Joni")
di_hola("Jose")

def fahr2celsius(fahr):
    celsius = (5*(fahr-32)) / 9
    return celsius

print (round(fahr2celsius(100),2))
