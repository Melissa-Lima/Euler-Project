n=100

sumSquare=0
for i in range (1,n+1):
    sumSquare=sumSquare+i**2
print(sumSquare)

squareSum=0
for i in range (1,n+1):
    squareSum=squareSum+i
print(squareSum**2)

print((squareSum**2)-sumSquare)
