#que 5: Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") should return the string "tothohisos isos fofunon".



def translate(string):
    c=0
    list1=[]
    for x in string:
        for y in string1:
            if(x==y):
                c+=1
        if(c==0):
            list1.append(x)
            list1.append("o")
            list1.append(x)
        else:
            list1.append(x)
        c=0
    return ''.join(list1)

def translate1(string):
    list1=[]
    for x in string:
        if x not in string1:
            list1.append(x)
            list1.append("o")
            list1.append(x)
        else:
            list1.append(x)
    return ''.join(list1)


string=(input("enter a string: "))
string1="aeiouAEIOU "
output=translate1(string)
print(output)


#alternative function for translate is translate1 both gives same output
