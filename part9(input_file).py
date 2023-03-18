#rules of inputing a file
# file = open('filename',mode='mode of operation(read/write)')
#file.close()


#file34 = open('abcd.txt',mode='r')#for the current directory
               # for different directory
file1=open('C:\\Users\\User\\Desktop\\pyy.txt' ,mode='r')
s=file1.read() # to read a file
print(s)
file1.close()  # closing the file is a good practise

print ('-------------')
    # reading files using for loop line by line
file=open('C:\\Users\\User\\Desktop\\pyy.txt' ,mode='r')

for line in file:
    print(line)
file.close()

print('---------just the first 2 lines--------')
    # print one or more specific line
file=open('C:\\Users\\User\\Desktop\\pyy.txt' ,mode='r')
print(file.readline())
print(file.readline())
file.close()
print('---------storing lines in a list--------')
file=open('C:\\Users\\User\\Desktop\\pyy.txt' ,mode='r')
lines=file.readlines() #reads lines and stores in a list
print(lines)
file.close()
print('\n')
# same work in for loop
file=open('C:\\Users\\User\\Desktop\\pyy.txt' ,mode='r')
lines=file.readlines() #reads lines and stores in a list
for l in lines :   
    print(l,end='') # end is used for removing the extra white line space  
file.close()        # we can also use l.rstrip() to remove the extra white space

print('\n------update inside file using Write---------')
# this write() function erase everything and write new lines
file=open('C:\\Users\\User\\Desktop\\pyy.txt' ,'w')
file.write('shob ki muche gelo naki ?\n')
file.write('accha pera nai. abar likhbo\n')
file.close()

print('---append lines---')
# just put 'a' instead of 'w' to append
file=open('C:\\Users\\User\\Desktop\\pyy.txt' ,'a')
file.write('1 ta line likhlam\n')
file.write('arekta line add korlam\n')
file.close()

print('--------lets practise-------')

file=open('file_input_practise.txt')

for line in file:
    print(line)
file.close()

#create and put the contents of file in a n_file
file=open('file_input_practise.txt')
n_file=open('file1_input_practise.txt','w')
for l in file:
    n_file.write(l)
file.close()
n_file.close()

#extract only the country names
file=open('file_input_practise.txt')
n_file=open('file2_input_practise.txt','w')
for l in file:
    temp=l.split()
    n_file.write(temp[1]+'\n')
file.close()
n_file.close()

#only the countries with 'B' will stay
file=open('file_input_practise.txt')
n_file=open('file2_input_practise.txt','w')
for l in file:
    temp=l.split()
    if temp[1][0]=='B':  # temp[1] is the country name
                         # temp[1][0] is the first letter
        n_file.write(temp[1]+'\n')

file.close()
n_file.close()

#append the populations
file=open('file_input_practise.txt')
n_file=open('file2_input_practise.txt','a')
for l in file:
    temp=l.split()
    n_file.write(temp[2]+'\n')

file.close()
n_file.close()

#split
red = 'babu tumi amar jaan baby ekdom'
blue=red.split()
print(blue)

#input list for = 1 2 3 4 5
ar = list(map(int, input().rstrip().split()))
