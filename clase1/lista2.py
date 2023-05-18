

nombres = ["juan","carolina","maria","andres","pablo"]
mayusculas = []
#print(nombres[2])=Martina
#print(nombre.upper) es para pasar a mayuscula
#print(nombre.lower) es para pasar a minuscula

for nombre in nombres:
    mayusculas.append(nombre.upper())

print(mayusculas)




numeros = [23, -14,0,0,21,-9,-5,34,89]
contPos = 0
contNeg = 0
contCeros = 0
for numero in numeros:
    if (numero == 0):
        contCeros += 1
         

    elif(numero < 0):
        contNeg += 1


    
    else:
        contPos += 1
print("cero:",contCeros)
print("positivo:",contNeg)
print("negativo:",contPos)


