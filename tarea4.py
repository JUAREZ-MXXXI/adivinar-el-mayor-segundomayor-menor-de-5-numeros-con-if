# Hallar el segundo mayor, el mayor y el menor con if 
a1 = int(input("Ingrese el primer numero: "))
b2 = int(input("Ingrese el segundo numero: "))
c3 = int(input("Ingrese el tercero numero: "))
d4 = int(input("Ingrese el cuarto numero: "))
e5 = int(input("Ingrese el quinto numero: "))

numeros = [a1, b2, c3, d4, e5]

maximo = max(numeros)
numeros.remove(maximo)  

segundo_max = max(numeros)

max = a1
min = a1

if b2 > max:
    max = b2
if c3 > max:
    max = c3
if d4 > max:
    max = d4
if e5 > max:
    max = e5

if b2 < min:
    min = b2
if c3 < min:
    min = c3
if d4 < min:
    min = d4
if e5 < min:
    min = e5

print("El número mayor es:", max)
print("El segundo numero mayor es:", segundo_max)
print("El número menor es:", min)
