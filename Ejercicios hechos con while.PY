import os 
#EJ 1
print("Ejercicio 1")
k=23
i=1
while 23*i<1000:
    total=23*i
    print(total)
    i+=1
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#EJ 2
print("Ejercicio 2")
u=1
num=int(input(f"Ingresar el {u} número "))
cantPos=0
cantNeg=0
cantCeros=0
promPos=0
promNeg=0
while u!=15:
    u+=1
    if num>0:
        cantPos+=1
    elif num==0:
        cantCeros+=1
    else:
        cantNeg+=1 
    num=int(input(f"Ingresar el {u} número "))
promPos=cantPos/15
promNeg=cantNeg/15
print("El promedio de positivos fue de:",promPos,"El promedio de negativos fue de:",promNeg,"Y la cantidad de ceros fue:",cantCeros)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#EJ 3
print("Ejercicio 3")
a=1
ap=0
des=0
porAp=0
porDes=0
nota=int(input(f"Ingresar la {a} nota "))
while a!=25:
    a+=1
    while nota<0 or nota>10:
        nota=int(input(f"Ingresar la {a} nota válida "))
    if nota >=4:
        ap+=1
    else:
        des+=1
    nota=int(input(f"Ingresar la {a} nota "))
porcAp=(ap*100)/25
porcDes=(des*100)/25
print("Porcentaje aprobados:"+str(porAp)+"% Porcentaje desaprobados:"+str(porDes)+"% ")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')