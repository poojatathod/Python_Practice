#que 11: Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:s. For example, generate_n_chars(5,"x") should return the string "xxxxx". (Python is unusual in that you can actually write an expression 5 * "x" that will evaluate to "xxxxx". For the sake of the exercise you should ignore that the problem can be solved in this manner.)

def gen_n_char(n,char):
    for i in range(n):
        list1.append(char)
    return ''.join(list1)



list1=[]
inpt=int(input("enter a no n: "))
inpt1=input("enter a char: ")
output=gen_n_char(inpt,inpt1)
print (output)
