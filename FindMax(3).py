""" 
write a code for finding a maximum from three numbers.
 """

x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))

if x>y and x>z:
    print(x,"is largest number.")

elif y>x and y>z:
    print(y,"is largest number.")

elif z>x and z>y:
    print(z,"is largest number.")

else:
    print(x,",",y,"and",z,"are equal numbers")

