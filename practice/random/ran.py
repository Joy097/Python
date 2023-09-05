import random as r
num = int(input())

#Id - 18201064
list1=[]
list2=[]

for i in range(num):
    s = input()
    a1 = s.split(" ")
    list1.append(a1[0])
    list2.append (int(a1[1]))
#print(list1)
#print(list2)

cno= 9996
list= []
for i in range (cno):
    li=[]
    for j in range (4):
        s = r.choice(list2)
        li.append(s)
    list.append(li)


def children(p1, p2):
    c1 = []
    c2 = []
    c1.append(p1[0])
    c1.append(p1[1])
    c1.append(p2[2])
    c1.append(p2[3])

    c2.append(p2[0])
    c2.append(p2[1])
    c2.append(p1[2])
    c2.append(p1[3])

    return c1,c2


def fitness(c1, l1, l2):
    w=0
    for i in range (4):
        g=int(c1[i])
        k=l2.index(g)
        if l1[k] == "d" :
              w+=g
        else:
              w-=g
    if w==0:
         return True
    else :
         return False




def result(c1, l2):
    res=""
    for i in range (len(l2)):
        res1= l2[i]
        if int(res1) not in  c1:
            res+="0"
        else :
            res+="1"
    return res



ab = ""
for i in range (999):
    child = []

    for j in range (len(list)):
        p1= r.choice(list)
        p2 = r.choice(list)
        c = children(p1,p2)
        child.append(c)
        ch1=c[0]
        ch2 = c[1]
        if fitness(ch1, list1, list2):
          ab = result(ch1, list2)
        if fitness(ch2, list1, list2):
          ab = result(ch2, list2)
        l = child
if ab != "":
    print(ab)
else:
    print("-1")








