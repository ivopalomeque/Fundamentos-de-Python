def convertir_temperatura(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(convertir_temperatura(20)) 

# Para trabajar con listas

def sumar_todos(*args):
    return sum(args)

suma = sumar_todos(1,2,6,3,7)

# Para trabajas con diccionarios
def describir_persona(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

describir_persona(nombre="Ivo", Edad=20, Profesion="Programador")