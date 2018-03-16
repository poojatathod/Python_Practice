#que 13: The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the largest one.

def max_of_list(list1):
    return max(list1)


inpt=input("enter a list of element: ")
list1=inpt.split()
list1=[int(a) for a in list1]
output=max_of_list(list1)
print("maximum no from a list is: ",output)
