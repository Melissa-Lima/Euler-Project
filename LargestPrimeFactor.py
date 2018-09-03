import math
from Primo import * #importa tudo do arquivo Primo.py


n=600851475143
for i in range (int(math.sqrt(n)),0,-1):
    if (n%i==0):
        if Prime(i)==True:
                print(i)
                break
