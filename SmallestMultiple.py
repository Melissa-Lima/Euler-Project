from Primo import Prime

n=20
resultado=1

for i in range(2,n+1):
    potencia=1
    numero=0
    if (Prime(i)==True):
        while (numero<n):
            numero=i**potencia
            if (numero<n):
                resultado=resultado*numero
                potencia+=1
print(resultado)
