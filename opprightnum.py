n=int(input("enter a number : "))
for i in range (n-1,0,-1):
    for j in range (1,i+1):
        print(j,end= " ")
    print()

# OUTPUT
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 
