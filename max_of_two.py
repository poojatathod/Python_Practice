#que 1: Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise.)



def max1(x,y):
    if(x>y):
        return x
    else:
        return y



x=int(input("enter first no: " ))
y=int(input("enter second no: "))
z=max1(x,y)
print("maximum no is ",z)
