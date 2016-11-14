##Project Euler Problem Number 3
##Find the largest prime factor 600851475143

prime = 600851475143
n = 2
highestN = 0

while(prime != 1):
    if prime % n == 0:
        prime = prime / n
        if n > highestN:
            highestN = n
    else:
        n += 1
    
print highestN
