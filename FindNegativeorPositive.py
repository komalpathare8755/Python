""" 
Write a program to find number is either positive or negative
"""

x=int(input("Enter the number:"))

if x>0:
    print(x," is positive")

elif x<0:
    print(x,"is negative")

elif x==0:
    print(x,"is neither positive nor negative")