nota = int(input(" Ingrese una nota entre 0/10: "))

while nota < 0 or nota > 10:
    nota = int(input("nota invalida, Ingrese una nota entre 0/10: "))

    
print(f" tu nota es : {nota} ")
