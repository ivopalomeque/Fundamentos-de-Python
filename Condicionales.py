edad = input("Ingrese su edad: ")
if edad.isdigit():
    edad = int(edad)
    if edad >= 18:
        print("Usted es mayor de edad")
        print("Puede votar")
    elif 13 <= edad < 18:
        print("Es adolescente")
    elif edad>0:
        print("Es un niño")
    else:
        print("Edad invalida")
else:
    print("La edad ingresada no es un número")

# Métodos de String 
nombre_usuario = input ("Ingrese su nombre de usuario: ")
if nombre_usuario.strip().lower() == "admin":
    print("Bienvenido, administrador")    
else:
    print("No eres administrador")