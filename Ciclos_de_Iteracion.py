letras = ['a','b','c','d']

# Imprime el contenido (Valor)
for item in letras:
    print(item)

    # En javascript
        # const letras = ['a','b','c','d']
        # letras.forEach(letra => { console.log(letra)}

# Imprime las pociciones del contenido (Indice)
for item in range(5):
    print(item)

    # En javascript
        # for (let i = 0; i < 5; i++) {
        #     console.log(i); }

# Imprime el contenido y la posición del contenido (Indice y Valor)
for index, letras in enumerate(letras):
    print(index, letras)

    # En javascript
        # for(let i = 0; i < letras.length; i++) {
        #     console.log(i, letras[i]); }

for i in range(5):
    print(i)
else:
    print('Chau mundo')

# Iteramos y realizamos una acción con cada elemento con cada una
cuadrados = [i**2 for i in range(5)]
print(cuadrados)
    
    # En javascript 
        # letrasMayusculas = letras.map(letra => {
        # return letra.toUpperCase()
        # })
        # console.log(letrasMayusculas)

# Cuando i es igual a 3,5 u 11 se ejecuta la siguiente línea
for i in range(5):
    if i == 3 or i == 5 or i == 11:
        continue
    print(i)

# Estructura While (Igual que el js)
contador = 0 
while contador < 15:
    print('While',contador)
    contador += 1

# Estructura While con else (Igual que el js)
contador = 0 
while contador < 15:
    print('While con else',contador)
    contador += 1
else:
    print('Chau Mundo')

# Estructura While con condición
contador = 0 
while contador < 15:
    if contador == 3 or contador == 5 or contador == 11:
        continue
else:
    print('Contiene 3, 5 o 11')