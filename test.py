n=int(input("Enter a odd number : "))
n1 = n 
if n > 9:
    odd_numbers = (n-9)//2
    extra_space = odd_numbers

for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 or i==n or j==1 or j==n:
            if i%2!=0 and j%2!=0:
                if j>i:
                    print(j+1-i, end="")
                elif i>j:
                    print(i+1-j, end="")
                elif j==i:
                    print(j//i, end="")
            else:
                print("*", end="")
        else:
            n1 = n1-2
            if j!=n and j>10 and j%2!=0 and i<10:
                print("a" * (len(str(j))), end="")
            elif j==n-1 and i%2==0:
                print("b" * (len(str(n))), end="")
            elif j==n-1 and i%2!=0 and i<10:
                print("c" * ((len(str(n)))+1-len(str(n1))), end="")
            else:
                print("d", end="")
    print()