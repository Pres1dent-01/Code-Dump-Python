def Armstrong(x):
    temp=0
    y = x
    while y > 0:
        temp+=(y%10)**3
        y=y//10
    return x == temp
        
num = int(input("Enter a number to find if it is Armstrong or not: "))
print(Armstrong(num))