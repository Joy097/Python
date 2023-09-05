def count_substring(string, sub_string):
    #print(string, sub_string)
    
    a=0    
    for i in range(len(string)):
        if string[i]==sub_string[0]:
            #print(string[i])
            
            y=i#2
            #print(y)
            #print(len(sub_string))
            
            h=0
            for j in range(len(sub_string)):
                
                if y>=len(string) :
                    break
                if string[y]==sub_string[j] :
                   h+=1
                   
            
                y+=1
            #print(h)
            
            if h==len(sub_string):
                a+=1 
    #print(a)
    
                
    return a
    

if __name__ == '__main__':
    string = input('give the main string : ').strip()
    sub_string = input('give the sub string : ').strip()
    
    count = count_substring(string, sub_string)
    print(count)