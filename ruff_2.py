sf='BANANA'
print('find the input character : ',sf.find('ANA'))

exit()
def swap_case(s):
    a=''
    
    for i in range(len(s)):
        
        q=int(ord(s[i]))
        
        e=s[i]
        
        
        
        if q>64 and q<91 :
            a+=e.lower()
            print(e.lower())
            
        elif q>160 and q<187 :
            a+=e.upper()
            
            
        
        else:
            a+=e
           
        
    
    
    return a


s = 'Ami Vaat Khai !'
result = swap_case(s)
print(result)
exit()
s='ascii character of the given value is: '
a=s[4]
print(a.upper())


exit()

values = input("Input some comma seprated numbers : ")
list = values.split(",")
a=0
for i in list:
    list[a]=int(i)
    a+=1
t = tuple(list) # converting list to tuple
print('List : ',list)
print('Tuple : ',tuple)
