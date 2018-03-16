#que 3:Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)

def len_of_str(string):
    c=0
    for x in string:
        c+=1

    return  c

string=input("enter a string: ")
output=len_of_str(string)
print("Length of the string is: ",output)
