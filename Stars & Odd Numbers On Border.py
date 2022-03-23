n = int(input("Enter A Odd Number : "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            if i%2==0 and j%2==0:
                if i>=j:
                    print(i+1-j, end="")
                else:
                    print(j+1-i, end="")
            else:
                print("*", end="")
        else:
            print(" ", end="")  
    print()      