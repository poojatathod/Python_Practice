#que 8: Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome("radar") should return True.


def ispalindrome(string):
    rev=string[::-1]
    if rev==string:
        return True
    else:
        return False


inpt=input("enter a string: ")
output=ispalindrome(inpt)
print(output)

