#Exception
#Exception a type of error

# 1. Syntax error if i<10 => here a clone (:) is expected
# 2. Logical error => if output is even but we print odd
# 3. Run time error => is the EXCEPTION (the error that occurs when running a code)
# 
# Example 1 :
# a=5,b=0 
# x=a/b,print(x) => Zero Division Error (Exception)
# 
# Exception occurs when during the program execution
# So, We have to handle exception.


# ================ Exception Handling ================

try:
    a=int(input('give an integer : ')) # if we enter a string then it will give value error and enter exception 
    b=2    # Error occurs for 0 but not for 2

    print('start procedure : try block')
    x=a/b
    print('end procedure : try block')
    print(x)


# if error occur in 'try' block, then it will enter in except block
except Exception:
    print('cannot divide by zero : Exception block') 


# if the program do not enter the exception block, then it will enter else block
else:
    print('no exception occured : else block')  


# program will always enter the 'finally' block with or without exception
finally:
    print('end procedure with finally block : finally block') 

#========== Basic of Exception (runtime error) ==========

print('---------- specific exceptions ----------')

#================ Types of Exception ================
# Index error : when index is out of range
# Name error : when a variable is not found locally or globally
# Indentation error : incorrect indentation
# Zero Division error
# Type error : incorrect object type for a function
# Runtime error : outside these errors

# Handling different type of exception :

try:
    a=int(input('give an integer : ')) 
             # Putting string will give ValueError
    b=int(input('give an integer : '))    
    x=a/b    # b = 0 will give ZeroDivisionError
    print(x)

# Exception For ZeroDivisionError =>
except ZeroDivisionError:
    print('ZeroDivisionError : number cannot be divided by Zero  ')

# Exception For ValueError =>
except ValueError:
    print('ValueError : give the correct input format')

# Exception block for any kind of Exception
# So, we have to put it in the last to avoid occurance for every exceptions
except Exception:
    print('Exception : other exceptions occured ')

finally:
    print('program terminates')

#-------manually putting exception-----

a=int(input('give an integer : '))
b=int(input('give an integer : ')) 
if b==0:
    raise ZeroDivisionError('b cannot be zero')
x=a/b   
print(x)


'''''
 If we put the Exception at first in the exception block
 then no other exception will occur.
 So, we have to maintain Exception hierarchy
 Exception Hierarchy link : https://docs.python.org/3/library/exceptions.html 
 Example :
 we have to take FloatingPointError block first 
 and lastly take Exception block.
 
'''''