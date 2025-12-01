def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista


# --------------------------
# PROGRAMA PRINCIPAL
# --------------------------

datos = [45, 17, 23, 67, 21, 12, 40, 7]

print("=== MÉTODOS DE ORDENAMIENTO ===")
print("1. Burbuja")
print("2. Inserción")
print("3. Selección")

opcion = int(input("Elige una opción (1-3): "))

print("\nLista original:", datos)

if opcion == 1:
    print("Ordenado con Burbuja:", burbuja(datos.copy()))
elif opcion == 2:
    print("Ordenado con Inserción:", insercion(datos.copy()))
elif opcion == 3:
    print("Ordenado con Selección:", seleccion(datos.copy()))
else:
    print("Opción no válida")
