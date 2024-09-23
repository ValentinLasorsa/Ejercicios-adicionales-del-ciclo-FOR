import os 
#EJ 1
print("Ejercicio 1")
total=0
for n in range (1,1000):
    num=23*n
    if num%23==0 and num<1000:
        print(num)
        total=total+num
print(total,"es la suma de todos los múltiplos de 23 menores a 1000")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 2
print("Ejercicio 2")
pos=0
neg=0
ceros=0
for i in range(1,16):
    num=int(input(f"Ingrese el {i} número "))
    if num >0:
        pos=pos+1
    elif num==0:
        ceros=ceros+1
    else:
        neg=neg+1
promPos=pos/15
promNeg=neg/15
promCer=ceros/15
print("El promedio de positivos:",promPos,"El promedio de negativos:",promNeg,"Y el promedio de ceros",promCer)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 3
print("Ejercicio 3")
ap=0
des=0
for u in range(1,26):
    nota=int(input(f"Ingrese la {u} nota "))
    while nota <0 or nota>10:
        nota=int(input(f"Ingrese la {u} nota coherentemente "))
    if nota>4:
        ap=ap+1
    else:
        des=des+1
porAp=(ap*100)/25
porDes=(des*100)/25
print(f"Porcentaje de aprobados: {porAp}% Porcentaje de desaprobados: {porDes}%")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')

#EJ 4
print("Ejercicio 4")
may=0
men=0
ig=0
for j in range(1,11):
    numero=int(input(f"Ingrese el {j} número "))
    if numero>15:
        may=may+1
    elif numero==15:
        ig=ig+1
    else:
        men=men+1
print(f"Mayores a 15: {may} Menores a 15:{men} Iguales a 15:{ig}")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')    

#EJ 5
print("Ejercicio 5")
sumaEdades=0
sumaAlturas=0
may35=0
for r in range(1,16):
    edad=int(input(f"Ingrese la {r} edad  "))
    altura=int(input(f"Ingrese la {r} altura (en centímetros) "))
    sumaEdades=sumaEdades+edad
    sumaAlturas=sumaAlturas+altura
    if edad>35:
        may35=may35+1
    if altura <160 and edad>40:
        print(altura)
print("Cantidad de personas mayores a 35 años:",may35)
promA=sumaAlturas/15
promE=sumaEdades/15
print("Estatura promedio:",promA,"Edad promedio:",promE)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')   

#EJ 6
print("Ejercicio 6")
numeroTabla=int(input("Ingrese un número "))
for h in range(1,18):
    print(numeroTabla*h)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')   

#EJ 7
print("Ejercicio 7")
contMayores=0
contMenores=0
porcMayores=0
porcMenores=0
for k in range(1,21):
    edad=int(input(f"Ingrese la {k} edad de la persona "))
    if edad>=18:
        contMayores+=1
    else:
        contMenores+=1
porcMayores=(contMayores*100)/20
porcMenores=(contMenores*100)/20
print("El porcentaje de mayores es del "+str(porcMayores)+"% y el de menores es del "+str(porcMenores)+"%")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')   

#EJ 8
print("Ejercicio 8")
numerosRuleta=0
cantNumerosImpares=0
cantNumerosPares=0
cant20Docena=0
numMax=0
promedioPares=0
for t in range (1,11):
    numerosRuleta=int(input(f"Ingrese el {t} número "))
    if numerosRuleta!=0:
        if numerosRuleta%2==0:
            cantNumerosPares+=1
        else:
            cantNumerosImpares+=1
    else: 
        print("Número 0!")
    if numerosRuleta >=13 and numerosRuleta <=24:
        cant20Docena+=1
    if numerosRuleta >numMax:
        numMax=numerosRuleta
promedioPares=cantNumerosPares/10
print("Cantidad de números impares:",cantNumerosImpares, " Promedio de números pares:",promedioPares)
print("La cantidad de números la 20 docena es de:",cant20Docena)
print("El número más alto fue:",numMax)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')   

#EJ 9
print("Ejercicio 9")
for q in range(1,21):
    horas=int(input(f"Ingrese la cantidad de horas trabajadas del empleado {q} "))
    tarifa=int(input(f"Ingrese la tarifa por hora del empleado {q} "))
    salario=horas*tarifa
    print("El salario que le corresponde es de $"+str(salario))
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')   

#EJ 10
print("Ejercicio 10")
sumaPares=0
sumaImpares=0
for y in range(1,26):
    num=int(input(f"Ingrese el {y} número "))
    if num%2==0:
        sumaPares=sumaPares+num
    else:
        sumaImpares=sumaImpares+num
print("Sumatoria de: Pares=",sumaPares, " Impares=",sumaImpares)
input("\033[1mPresione enter para finalizar\033[0m")
os.system('cls')   