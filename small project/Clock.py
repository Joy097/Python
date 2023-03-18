# DIGITAL CLOCK
import time


def Zero():
    if i<=9 and j>9 and x>9:
        print("\r Time : ",'0'+str(i),':',j,':',x," | (*_*) ",end='')
        time.sleep(1)
    if i>9 and j<=9 and x>9:
        print("\r Time : ",i,':','0'+str(j),':',x," | (*_*) ",end='')
        time.sleep(1)
    if i>9 and j>9 and x<=9:
        print("\r Time : ",i,':',j,':','0'+str(x)," | (*_*) ",end='')
        time.sleep(1)
    if i>9 and j<=9 and x<=9:
        print("\r Time : ",i,':','0'+str(j),':','0'+str(x)," | (*_*) ",end='')
        time.sleep(1)
    

    if i<=9 and j>9 and x<=9:
        print("\r Time : ",'0'+str(i),':',j,':','0'+str(x)," | (*_*) ",end='')
        time.sleep(1)

    if i<=9 and j<=9 and x>9:
        print("\r Time : ",'0'+str(i),':','0'+str(j),':',x," | (*_*) ",end='')
        time.sleep(1)

    if i<=9 and j<=9 and x<=9:
        print("\r Time : ",'0'+str(i),':','0'+str(j),':','0'+str(x)," | (*_*) ",end='')
        time.sleep(1)




while True:
    for i in range (24):
        for j in range(60):
            for x in range (60):
                Zero()

                

