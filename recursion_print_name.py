def recursive_name(num):
    if num > 0:
        print("Ab", end=" ")
        recursive_name(num -1)

number = int(input("Enter a number: "))
recursive_name(number)

