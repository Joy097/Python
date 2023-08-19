list=['2. jabir','3. jaker','boroi']
for i in range(len(list)):
    if ord(list[i][0]) >47 and ord(list[i][0])<58:
        list[i] = list[i][3:]
    list[i] = str(i+1)+". "+list[i]
print(list)