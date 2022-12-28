# Recursive Sigma
# Write a recursive function that given a number returns the sum of integers from 1 to that number. Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.

def sigma(num):
    if num >0:
        return num + sigma(num-1)
    return 0
print(sigma(5))

# Recursive Factorial
# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (123). Also, rFact(6.5) = 720 (123456).

def fact(num):
    if num > 0:
        return num fact(num-1)
    return 1
print(fact(6))

#BONUS: Flood Fill

def fill(canvas2d, staryXY, Color):
    width = len(canvas2d)