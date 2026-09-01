def Palindrome(x):
    if x < 0:
        return False
    s = str(x)
    return x == s[::-1]

num = int(input("Enter any number to check palindrome: "))
print(Palindrome(num))



    