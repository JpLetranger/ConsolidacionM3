# Creamos la lista con todos los nombres

nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Separamos a los personajes en 3 listas

magos = ["Harry Houdini", "David Blaine", "Teller"]

cientificos = ["Newton", "Hawking", "Einstein"]

otros = ["Messi", "Pele", "Juanes" ]


# Creamos la funcion para hacer grandiosos a los magos
def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

# Creamos la funcion para imprimir los nombres 
def imprimir_nombres(nombres):
    for nombre in nombres:
        print(nombre)

# Imprimir la lista completa de nombres 

print("\nLista completa de nombres:\n")
imprimir_nombres(nombres)

# Llamamos a la funcion que agrega "el gran" a los magos

hacer_grandioso(magos)

# Imprimimos las listas segun lo pedido

print("\nMagos grandiosos:\n")
imprimir_nombres(magos)


print("\nCientíficos:\n")
imprimir_nombres(cientificos)


print("\nOtros:\n")
imprimir_nombres(otros)
