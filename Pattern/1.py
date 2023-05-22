num_row=int(input("Enter the number of rows : "))
for i in range (num_row,0,-1):
    for j in range (0,num_row-i):
        print(" ",end="")
    for j in range (0,i):
        print("*",end=" ")
    print()