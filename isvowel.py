#que 4: Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

def isvowel():
    s="aeiou"
    z=len(s)
    inpt=str(input("enter a single charector: "))
    for x in s:
        if(inpt==x):
            print("isvowel")

    print(inpt, "is not vowel")
isvowel()
