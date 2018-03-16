#que 15: Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def longest_word(string):
    list1=[]
    for x in string:
        list1.append=len(x)
    outpt=max(list1)
    outpt1=list1.index(outpt)
    outpt2=string[outpt1]
    return outpt2




string=input("enter a string: ")
string=string.split()
output=longest_word(string)
print(output)
