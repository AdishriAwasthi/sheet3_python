n=int(input("enter a number : "))
for i in range (n,0,-1):
    for j in range (n-i):
        print("-", end =" ")
    for j in range (i):
        print("*  ", end=" ")
    
    print()

# OUTPUT
 
#  * * * * *          
# _ * * * *        
# _ _ * * *         
# _ _ _* *        
# _ _ _ _* 
