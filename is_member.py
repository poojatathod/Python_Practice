#que 9: Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)


def ismember(x,list1):
    for y in list1:
        if y==x:
            return True
    return False

list1=input("enter a list of no: ")
#list1=list1.split()
#list1=[int(a) for a in list1]
x=input("enter a number: ")
output=ismember(x,list1)
print (output)
