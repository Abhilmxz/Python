# Even Number Printing In pattern

n=int(input("Enter the number of rows: "))
k=2
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=2
    print()