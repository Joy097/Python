# a string must be started and ended with ' or "". 
#'string inside 'string' is not valid'
#'but a "quote inside" a string is valid'




str = 'loving python'
print(len(str))
#negative indexing
print('the position of first character can be',str[-13])
print('the position of last character for can be',str[-1])

# we cannot change or modify a character in a string
#concatenation

a='I'
a+='love'
a+='you'
print(a)

#string repetition
print('kire \n'*8)
for i in range (4):
    print("red")

#slicing
course = 'cse 110'
for i in range(4,7):
    print(course[i],end='')

print('\n')  #for 

slice = "Slice the CAKE"
print (slice[10:14])#print (10-13)
print(slice[10:])#print from (10 to last)
print(slice[:5])#print (0-4)
print(slice[0:10:2])#print(0,2,4,6,8) 0 to 10 and jump by 2 steps
print(slice[0::3])#print 0 to last and jump 3 steps
print(slice[:])#print all

#logical in
print('bay' in 'ebay')
print('bay' not in 'ebay')

st1= 'hey jude'
st2= 'jude'
st3= 'ruby'
if st2 in st1:
    print("sing a sad song and make it better")
if st3 not in st1:
    print("quit singing")

#iterate a string
index=0
s='hey shawty *v*'
while index <len(s):
    print(s[index])
    index+=1
print("gap_gap_gap")
for x in s:
    print(x,end='')
print("\n")
#ASCII
# the english characters represented by the number (0-127)
# to convert, we will use two function: ord and chr
print('ASCII value of the given character is: ',ord('a'))
print('ASCII value of the given character is: ',ord('s'))
print('ASCII character of the given value is: ',chr(125))
print('ASCII character of the given value is: ',chr(34))
print('\n')
#String functions
sf='  string functions ARE NOT COOL  '
print('lower all : ',sf.lower())
print('upper all : ',sf.upper())
print('strip before and after white space : ',sf.strip())
print('strip left space : ',sf.lstrip())
print('strip right space : ',sf.rstrip())
print('count the input character : ',sf.count('o'))
print('find the input character : ',sf.find('g'))
print('replace the input character : ',sf.replace('o','change'))
print('does the character start with input : ',sf.startswith('string'))
print('See all the functions :'.upper(),dir(''))
c='Dont yOU dARE'
v=c.swapcase()
print("to swap the cases . capital will be small and vice versa",v)
print('\n')
#Split and join
line = 'ami vaat khai'
line=line.split(' ') #['ami','vaat','khai']
line='-'.join(line)#ami-vaat-khai
#make a list from string
l=list(line)
# Change a value in a string :
#>>> string = "abracadabra"
#>>> l = list(string)
#>>> l[5] = 'k'
#>>> string = ''.join(l)
#>>> print string
#abrackdabra
# another approach :
# >>> string = string[:5] + "k" + string[6:]
#>>> print string
#abrackdabra