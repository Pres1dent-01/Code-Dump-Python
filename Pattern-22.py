n = 7
max_num = 4

for i in range(n):
    row = ""
    for j in range(n):
        ring = min(i, n-1-i, j, n-1-j)
        value = max_num - ring
        row += str(value)
    print(row)