#que 10: function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.i


def overlapping(list1,list2):
    for x in list1:
        for y in list2:
            if x==y:
                return True
    return False



l1=input("enter 1st list: ")
list1=l1.split()
list1=[int(a) for a in list1]

l2=input("enter 2nd list: ")
list2=l2.split()
list2=[int(a) for a in list2]

output=overlapping(list1,list2)
print (output)
