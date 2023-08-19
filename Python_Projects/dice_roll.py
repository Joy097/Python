import random
while True :
    inp = input('Enter x to continue and else to exit : ')
    ran = random.randint(1,6)
    if(inp=='x'):
        print(ran)
    else:
        print('Session ended')
        break