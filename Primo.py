import math

def Prime(n):
    soma=0
    for i in range (1,int(math.sqrt(n))+1): #Forçar a ser inteiro porque o range requer inteiros
        if (n%i==0):
            soma=soma+1
            if soma>1:
                return (False)
    return (True)
