# pedir 5 numeros y decir cual fue el mayor

i = 0

mayor = None

while i < 5:
    numero = int(input("insertar un numero: "))
    if i == 0 or numero > mayor:
        mayor = numero

        mayor = numero
    i += 1

print(f"El mayor numero es {mayor}")
