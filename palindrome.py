s = input ("enter a string : ")

def palindrome (string):
    x = ""
    for i in string:
        x = i+x
        print (x)
    return x

if s == palindrome(s):
    print("palindrome")
else:
    print("not palindrome")