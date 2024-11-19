color = "azul"

match color:
    case "azul":
        print("10% de descuento")
    case "rojo":
        print("20% de descuento")
    case "verde":
        print("30% de descuento")
    case "amarillo":
        print("40% de descuento")

dia_semana = "jueves"

match dia_semana:
    case "lunes" | "martes" | "miércoles":
        print ("Es un día laboral")
    case "jueves" | "viernes":
        print ("Hoy es Jueves!!")
    case "sabado" | "domingo":
        print ("Es fin de semana")

numero = 25

match numero:
    case n if n<0:
        print("El numero es negativo")
    case n if n>0:
        print("El numero es positivo")
    case _:
        print("El numero no es negativo ni positivo")