import math

num = int(input("Enter any number: "))
is_prime = True

if num < 2:
    is_prime = False

for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
        is_prime = False

print(is_prime)