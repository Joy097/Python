dict = {'key':'value',1:'dog','course':'python',
'highest':{'name':'Dora','mark':100}}
print(dict['key'])
print(dict.get('highest'))
print(dict.get('high'))#not found in dict. so, gave none
print(dict.get('high','painai vai'))#show message for not finding
print(dict['highest']['name'])
dict[1]='kukur'
print(dict.get(1))

print('------update----------')
dict.update({'key':'abul'}) 
dict.update({'choto':'babul'}) 
print(dict)
#clear() clears everything inside
a=dict.pop("key")#remove the selected value
b=dict.popitem()#remove the last value
print(b)
print(a)
print(dict)
del dict[1]#same as pop
#del dict = deletes the dictionary itself
print(dict)
dd = {'k':'value','pet':'boss','see':'pyc',
'car':{'brand':'hyundai','model':'sonata','year':2016}}
print(dd.keys())
print(dd.values())
print(dd.items())

#dictionary in loop(iteration)
for key in dd:
    print(key)
for key in dd.keys():
    print(key)
for key in dd.values():
    print(key)
for key,value in dd.items():
    print(key,'=',value)

#other
print(len(dd))
print(max(dict.keys()))
print(max(dict.values()))
print(min(dict.keys()))
print(min(dict.values()))
print(sorted(dd.keys()))
print(sorted(dict.values()))