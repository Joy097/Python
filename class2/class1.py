try:
    def sum(a,b):
        sum=a+b
        return sum
    def sub(a,b):
        sub=a-b
        return sub
    def mult(a,b):
        mult=a*b
        return mult
    def div(a,b):
        div=a/b
        return div
    
    

    print(sum(2,0))

except ZeroDivisionError:
    print("handeling the zero error")
    div=0
    print(div)

except:
    print("there is an error")

else:

    print("work done successfully")



