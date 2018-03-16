#que 2: Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.


def max_of_three(a,b,c):
    if a>b:
         if a>c:
             return a
    elif c>b:
         return c
    else:
         return b

a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
c=int(input("enter value of c: "))
output=max_of_three(a,b,c)
print ("maxium no is: ",output)
