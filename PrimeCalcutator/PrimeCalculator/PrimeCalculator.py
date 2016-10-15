import math
N = 100

primes = [1] * N

for i in range(2, math.ceil(math.sqrt(N))):
    if primes[i]!=0:

        for j in range(1 , math.ceil(N/i)):
            primes[i*j] = 0
            #print("for sure ", i, "*",j,"=",(i*j)," is not prime")

print("done")
for i in range(1,N):           
    if primes[i]:              
        print(i)               
                               
                               
                               
#for i in range(1,100):         
#    prime = true               
#    for d in range(2,i):       
#        if i%d == 0:           
#            prime = false      
#    if prime == true:
#          print(i)

            
         


    
