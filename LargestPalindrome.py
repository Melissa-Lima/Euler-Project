largestPalin=0

for i in range (100,1000):
  for j in range (100,1000):
      prdct=i*j
      prdctStr=str(prdct) #Converte o produto em String
      if (prdctStr==prdctStr[::-1]): #Reverte a String
        palin=prdct
        if (palin>largestPalin):
            largestPalin=palin
print (largestPalin)
