row = int(input("Enter the number of rows : "))
print(" ")
for i in range(1, row+1):
    for j in range(row, i-1, -1):
        print((row-j+1), end=" ")
    print()
