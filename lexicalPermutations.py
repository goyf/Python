##Project Euler problem number 24
##What is the millionth lexicographic permutation of digits 0123456789
##https://projecteuler.net/problem=24

from math import factorial

digits = [0,1,2,3,4,5,6,7,8,9]
permutatedDigits = [0]*10
numberDigits = len(digits)
k = 1
currentDigit = 0
member = 1000000 #We want millionth permutation
originalMember = member


finished = False
while(finished == False):
    done = False
    while(done == False):
        noPermutations = (factorial(numberDigits)/numberDigits)*k

        if member > noPermutations:
            k += 1

        if member <= noPermutations:
            k -= 1
            permutatedDigits[currentDigit] = digits[k]
            digits.pop(k)
            done = True
    noPermutations = (factorial(numberDigits)/numberDigits)*k
    member = member - noPermutations
    k = 1
    currentDigit += 1
    numberDigits -= 1
    if numberDigits < 3:
        if originalMember % 2 == 0:
            permutatedDigits[currentDigit] = digits[1]
            permutatedDigits[currentDigit + 1] = digits[0]
            finished = True
        if originalMember % 2 != 0:
            permutatedDigits[currentDigit] = digits[0]
            permutatedDigits[currentDigit + 1] = digits[1]
            finished = True
            
    if currentDigit == (len(digits)-1):
        finished = True

print permutatedDigits
    
