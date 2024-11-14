def calcular_area_triangulo(base,altura):
    return base*altura/2

print(calcular_area_triangulo(2,4))

# Funciones anidadas
def calculadora(operacion,a,b):
    def suma(a,b):
        return a+b
    
    def multiplicación(a,b):
        return a*b
    
    if operacion == "suma":
        return suma(a,b)
    elif operacion == "multiplicación":
        return multiplicación(a,b) 
    else:
        return "Operación no válida"

# Ejemplos de uso
print(calculadora("suma",5,6))
print(calculadora("multiplicación",5,6))