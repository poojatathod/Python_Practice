#que 12:  procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:

#     ****
#     *********
#     *******


def histogram(list1):
    for item in list1:
        print ("*" * item)



inpt=input("enter element in the list: ")
list1=inpt.split()
list1=[int(a) for a in list1]
histogram(list1)

