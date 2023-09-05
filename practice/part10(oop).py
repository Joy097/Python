#-----object oriented programing-----
print (type(1234))    # Integer class 
print (type('1234'))  # String class
# so, every object has a type

#when ever I create an object , a constructor will be called
print("-------------------------")


#===================== CLASS =====================#

class Student:  # Class/Design/Blueprint
    def __init__(self,NAME,ID):         # constructor
                            #init is a method
        print('an object is created')
        #name=NAME >>  local variable
        self.name=NAME # Now this variable is assigned 
        self.id=ID          #for a specific memory location
                       #of an object.(ex-s1,s2)  
    def details(self):
        
        print(self.name)
        print(self.id)
        

   #===========================================#  
   
   #============== Requirements ===============#

# In oop, we have to just work on the above class
# But we can not change anything in the requirements
#otherwise out output will change


#creating an object - {variable = classname()}

#**** WHEN A OBJECT IS CREATED, (ex.-s1) a default
# parameter, 'MEMORY LOCATION' for that object is 
# created in the memory for that object(ex-s1,s2).
# and 'SELF' is the location in memory parameter.  



s1=Student('Ashraf',18201012)  #1st object/Instance
           # s1, s2 is an user defined object
           #x=4 > integer object (System defined)

print(s1.name)
print(s1.id)
# updated name 
s1.name = 'Jhon'
print("updated > ",s1.name)

print("-------------------------")
#print(s1) #<__main__.Student object at 0x00000248F3CC0F70>

s2=Student('Xarif',18201033)

#print(s2) #<__main__.Student object at 0x000001FE2BDD0F40>
           # so, the m. location of s1 and s2 is different

print(s2.name)
print(s2.id)

print("------------------------")
#calling through an constructor
s1.details()
s2.details()