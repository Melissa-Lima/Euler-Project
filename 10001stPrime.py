from Primo import Prime

n=10001
contador=0
i=2

while (contador<n):
    if (Prime(i)==True):
        contador+=1
        ultimoprimo=i
    i+=1
print(ultimoprimo)
