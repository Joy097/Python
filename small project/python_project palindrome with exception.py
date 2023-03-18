try:
    list=[]
    c=0
    e=int(input('give the palindrome range : '))
    print(type(e))
    
    for i in range(e):
        print('-----')
        z=int(input('Give '+str(i)+' no integer : '))
        list.append(z)
    
    def checkpalindrome():
        
        mid=len(list)//2
        
        for i in range(mid):
            
            if list[i]!=list[-1-i]:
                global c 
                c=1
                print("Sorry! The list is not a palindrome")
                break
        
    
    checkpalindrome()
    
    if c==0:
        print('yay.............. The list is a palindrome')


except IndexError:
    print('IndexError occured')

except ValueError:
    print('ValueError occured')

except TypeError:
    print('TypeError occured')

except Exception:
    print('other exception occured')

else:
    print('Congrats! your code is free of errors')

finally:
    print('The END of the world')
