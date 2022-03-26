n1=int(input("Enter a odd number : "))
numbers = 0
difference = 1
if n1 > 9:
    difference = n1 - 9
    numbers = difference//2

for i in range(1, n1+1):
    for j in range(1, n1+1):
        if i==1 or i==n1 or j==1 or j==n1:
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
            if j==n1-1 and i>10 and n1-i >= 9 and i%2!=0:
                extra_space = numbers 
                print(" " * (extra_space - 1), end="")
        
            elif j==n1-1 and (n1-i > 9 or n1-i < difference) and i%2!=0:
                extra_space = numbers 
                print(" " * (extra_space), end="")
            
            elif j==n1-1:
                extra_space = numbers 
                print(" " * (extra_space + 1), end="")

            else:
                print(" ", end="")
    print() 