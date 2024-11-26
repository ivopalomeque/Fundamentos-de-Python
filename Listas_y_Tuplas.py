mi_lista = ['pera', 'anana','frutilla', "uva"]

def mostrar_lista(list):
    print(list)

def agregar_fruta(list, fruta):
    list.append(fruta)

def insertar_fruta(list, fruta, pos):
    list.insert(pos, fruta)

def eliminar_fruta(list, fruta):
    try:
        list.remove(fruta)
    except ValueError:
        print(f'No se encontro la fruta: {fruta}')

def sacar_fruta(list, pos=0):
    try:
        list.pop(pos)
    except IndexError:
        print(f'No se encontro la posición: {pos}')



mostrar_lista(mi_lista)
nuevo_fruta = 'sandia'  # input('Ingrese la nueva fruta: ')
agregar_fruta(mi_lista, nuevo_fruta)
print('Luego de agregar sandia: ', mi_lista)
nuevo_fruta = 'melocoton'  # input('Ingrese la nueva fruta: ')
agregar_fruta(mi_lista, nuevo_fruta)
print('Luego de agregar melocoton: ', mi_lista)
nuevo_fruta = 'papaya'  # input('Ingrese la nueva fruta: ')
agregar_fruta(mi_lista, nuevo_fruta)
print('Luego de agregar papaya: ', mi_lista)
nuevo_fruta = 'melon'  # input('Ingrese la nueva fruta: ')
insertar_fruta(mi_lista, nuevo_fruta, 1)
print('Luego de insetar melon en la pos 1: ', mi_lista)
nuevo_fruta = 'fruilla'  # input('Ingrese la nueva fruta: ')
eliminar_fruta(mi_lista, nuevo_fruta)
nuevo_fruta = 'frutilla'  # input('Ingrese la nueva fruta: ')
eliminar_fruta(mi_lista, nuevo_fruta)
print('Luego de eliminar frutilla: ', mi_lista)
sacar_fruta(mi_lista, 9)
sacar_fruta(mi_lista, 0)
print('Luego de sacar la ultima fruta: ', mi_lista)
# cantidad de elementos de una lista - arr.length
print('La lista tiene actualmente:', len(mi_lista), "elementos")
# Ordenar lista
mi_lista.sort()
print('Lista ordenada: ', mi_lista)
# Lista en reversa
mi_lista.reverse()
print('Lista alverres: ', mi_lista)



# Acceso a elementos
print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[4])
#Acceder al ultimo elemento
print(mi_lista[-1])
print(mi_lista[-2])

# Error de indice (IndexError) print(mi_lista[5])

# Acceso con rangos
print(mi_lista)
print(mi_lista[:2])
print(mi_lista[:-2])
print(mi_lista[1:-1])
print(mi_lista[2:])
print(mi_lista[0:6:2])
print(mi_lista[::-1])
print(mi_lista[4:2:-1])

mi_tupla = tuple(mi_lista)
print("esta es mi tupla",mi_tupla)
print("tiene",len(mi_tupla),'elementos')

notas_alumnos = [6,8,10,7,5,6,7,4,5,8,9,7,7,6]
print("La suma de las notas es:", sum(notas_alumnos))
print("La minima de las notas es:", min(notas_alumnos))
print("La maxima de las notas es:", max(notas_alumnos))
print("el promedio de las notas es:", sum(notas_alumnos)/len(notas_alumnos))