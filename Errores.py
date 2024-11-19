try:
    numero = int(input("Ingresa un número: "))
    print(f"Número Ingresado: {numero}")
except ValueError:
    print("Error: debe ingresar un valor numérico")

try:
    numerador = int(input("Ingrese el numerador: ")) 
    denominador = int(input("Ingrese el denominador: ")) 
    resultado = numerador/denominador
    print("Resultado de la división: (resultado}")
except ZeroDivisionError:
    print("Error: se intentó dividir por cero.")
except KeyboardInterrupt:
    print("Adios vaquero.")
else:
    print("Numeros ingresados de forma válida")
# finally:
#     print("Cerrando todos los recusros antes de finalizar el programa")


class ErrorNumeroNegativo(Exception): 
    pass

calculo_salario_anual = int(input("Ingrese su sueldo mensual: "))
try:
    calculo_salario_anual = calculo_salario_anual * 12
    if calculo_salario_anual < 0: 
        raise ErrorNumeroNegativo("Se ingresó un número negativo")
except ErrorNumeroNegativo:
    print("Error: el salario no puede ser negativo")