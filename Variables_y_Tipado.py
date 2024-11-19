# Definición de variables
nombre = "Ivo"
año_actual = 2024
año_nacimiento = 2004
edadCalculada = año_actual - año_nacimiento
altura = 1.84
es_programador = True
salario = None

# Tipo de datos (Ver de que tipo es un dato dentro de una variable)
print(type(nombre))
print(type(año_actual))
print(type(edadCalculada))
print(type(altura))
print(type(es_programador))
print(type(salario))

# Formas de hacer print
print(f"Mi edad es {edadCalculada}, mi altura es: {altura}")
print("Mi nombre es " + nombre + ", mi edad es: ", edadCalculada )

# Constantes
PI = 3.1416
GRAVEDAD = 9.81
MAX_CONNECTIONS = 100

es_entero = isinstance(año_nacimiento, int)
es_string = isinstance(nombre, str)