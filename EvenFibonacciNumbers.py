from Fibonacci import Fibonacci

soma=0
i=1
while (Fibonacci(i)<4000000):
	if (Fibonacci(i)%2==0):
		soma=soma+Fibonacci(i)
	i+=1
print(soma)
