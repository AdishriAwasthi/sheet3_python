n=int(input("enter a number : "))
for i in range(n,0,-1):
    print("*",end=" ")
    for j in range (1,i):
        print("-",end=" ")

    print("*")

#  OUTPUT
# * - - - - *
# * - - - *
# * - - *
# * - *
# * *
cvbnm,