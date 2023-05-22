def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos +1

    return found

arr=[]
n=int(input("Enter the number of elements : "))
print("Enter the elements : ")
for i in range(0,n):
    ele=int(input())
    arr.append(ele)
search=int(input("Enter the element to be searched : "))
print(sequentialSearch(arr, search))
