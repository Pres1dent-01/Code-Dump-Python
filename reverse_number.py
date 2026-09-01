num = input("Enter a number: ")
temp = ""

for i in range(len(num)-1, -1, -1):
    if num[i] == "-":
        pass
    else:
        temp += num[i]
temp = int(temp)

if int(num) < 0:
    temp = temp*-1

print(temp)
