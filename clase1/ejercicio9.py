
numeros = [3,5,2,8,1,9,4,2,10]
pares = []
impares = []
#mostrar los numeros pares

for numero in numeros: 
    if(numero % 2 == 0 ):
     pares.append(numero)

    else:
     impares.append(numero)

print(pares)
print(impares)
print(f"tus numeros pares son: {len(pares)}")
print(f"tus numeros impares son: {len(impares)}")

cantimpares = len(impares)
cantpares = len(pares)
if (cantimpares == cantpares):
  print("son iguales")
  
elif(cantimpares < cantpares):
  print("impares son menos")
else:
  print("pares son mas ")



#el resto sirve para calcular pares e impares

