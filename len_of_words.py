#que 14: Write a program that maps a list of words into a list of integers representing the lengths of the correponding words.


def len_of_words(list1):
    for item in list1:
        print ("length of word", item, "is: ",len(item))



inpt=input("enter a list of string: ")
list1=inpt.split()
len_of_words(list1)

