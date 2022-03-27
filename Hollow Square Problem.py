n=n1=int(input("Enter a odd number : "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 or i==n or j==1 or j==n:
            
            if i%2!=0 and j%2!=0:
                
                if j>i:
                    print(j+1-i, end="")
                
                elif i>j:
                    print(i+1-j, end="")
                
                else:
                    print(j//i, end="")
            else:
                if j==n and i%2==0 and j%2!=0: 
                    print(" " * (len(str(j))-1), end="")

                print("*", end="")
        else:
            
            if j%2!=0 and j<n-1:
                print(" " * len(str(j)), end="")

            elif i%2!=0 and j==n-1:
                n1 = n1-2
                if i < 10:
                    print(" " * (1+len(str(n))-len(str(n1))), end="") 
                else:
                    l = len(str(i))-1
                    print(" " * (len(str(n))-(l*len(str(n1)))), end="") 

            else:
                print(" ", end="")
    print()