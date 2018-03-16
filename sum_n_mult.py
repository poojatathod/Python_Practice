#que 6: Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum1(list1):
    sum2=0
    for x in list1:
        sum2=sum2+x
    return sum2


def mult(list1):
    mul=1
    for x in list1:
        mul=mul*x

    return mul


inpt=input("enter a list of element: ")
list1=inpt.split()
list1=[int(a) for a in list1]

sum_of_list=sum1(list1)
mul_of_list=mult(list1)
print("sum of list element is: ", sum_of_list)
print("multiplication of list element is: ",mul_of_list)


