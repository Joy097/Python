# ------------PROJECT---------------

# We have to :
# Read the file
# Create a directory where key:value = goal:name 
# because sorted() sorts a dictionary
# Sort the dictionary in descending order
# Write the sorted list in a new file


# 1. Open the file
file=open('goal_stats.txt')


# 2. Read and print the file
s=file.read()
print(s)
file.close()


# 3. Split in the basis of '|' and store in players_dict
file=open('goal_stats.txt')
players_dict={}                  # Create a dictionary
for line in file:
    temp=line.split('|')         # Split the lines in file on basis of '|' (see inside the file) and stored in the temp for one loop
    name=temp[0]                 # As the names are in temp [0]
    goals=int(temp[-1].strip())  # Removing the white spaces of goal with strip() and converting it in int 
    players_dict[goals]= name    # Stored in the players_dict Dictionary where Key:Value > goals:name


# 4. Sort the infos according to goals and stored in sorted_dict
goal_list=sorted(players_dict,reverse=True)   # 'players_dict' sorted reversely and stored in goal_list
sorted_dict={}
for goal in goal_list:
    name=players_dict[goal]
    sorted_dict[name]=goal                    # The name is the key and goal is the value in the new Dictionary


# 5. Printing the sorted infos
a=0
for i in sorted_dict:
    a+=1
    print(a,'.',i,':',sorted_dict[i])        # Simple print


# 6. Write this list in a new file           
n_file=open('best players.txt','w')          # Creating a file

for name,goal in sorted_dict.items():        # items give bunch of tuples with name and goal
    n_file.write(name+' : '+str(goal)+'\n')
n_file.close()

