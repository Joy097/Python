string=input("Please enter a string: ")
result=''
for i in string:
    code=ord(i)
    if(32<=code and 47>=code or 58<=code and 64>=code or 91<=code and 96>=code or 123<=code and 126>=code):
        continue
    else:
        result+=chr(code)

print(result)