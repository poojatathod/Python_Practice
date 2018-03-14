def isvowel(char):
    list=["a","e","i","o","u","A","E","I","O","U"]
    if char in list:
        return "true"
    else:
        return "false"

char="A"
print isvowel(char)
