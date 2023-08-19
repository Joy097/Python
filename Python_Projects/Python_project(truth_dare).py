
#---------------------------------------------------------------The Ulmimate Truth/Dare Game-------------------------------------------------------#
import random

#truths
list1=[' Whats the last lie you told ?',
'What was the most embarrassing thing you haveve ever done on a date ?',
'Whats your most bizarre nickname ?','If you met a genie, what would your three wishes be ?'
,'Whats the meanest thing youve ever said to someone else ?',
'Who are you most jealous of ?','Whats one thing youd do if you knew there no consequences ?',
'Do you believe in any superstitions ? If so, which ones ?','What app do you waste the most time on ?',
'Have you ever picked your nose in public ?','Whats the longest youve gone without showering ?',
'what are you thinking now ?','Whats your biggest regret in life ?','Do you still have feelings for any of your exes ?',
'If you switched genders for a day, what would you do?',
'Whats the most childish thing you still do?','Would you date someone shorter than you?',
' Name one thing youd change about every person in this room.','in this room you have to makeout with someone. who is that?',
'whom do you want to have sex with?','are you horny enough to have sex with anyone in this room?','How many people have you kissed?',
'Who in this room would you list as your emergency contact?','Whats the scariest thing thats ever happened to you?',
'If you could set anyone here up with your best friend, who would it be and why?','Have you ever farted in public ?',
'You have to marry someone in this room. who is that?','You have one week to live.What would you do?',
'Whens the last time you cried and why?','you have to go on a tour with someone in this room.who is that?',
'Whats the last thing you Googled?','Whats the hardest drug youve ever tried?','Whens the last time you peed your pants?',
'Whats your biggest insecurity?','Whats the best lie youve ever told anyone?','Whats the weirdest thing youve ever done in a bathroom?',
'Whens the last time you watched porn','Whats the worst advice someone else has ever given you?',
'Who was the last person you said, “I love you” to?','Whats the scariest thing youve ever done?','something that still haunts you',
'Who in this room do you trust the least?','what would you say to propose someone?','what is the dumbest thing you have ever done?',
'Have you ever said, “I love you” and not really meant it? To whom?','Whats the weirdest thought youve had sitting on a toilet?',
'Whats something youre embarrassed that youre good at?','Who would you bring with you on a deserted island?','Whats something youve done that youd judge someone else for doing?',
'Tell one of your biggest secret that we dont know','Tell one of your biggest secret that we dont know','Do you touch yourself ?']
#dares
list2=['Call your ex','Call your crush','propose someone in this room','propose your crush in text',
'Let another player post a status on your social.',' Do freestyle rap for 1 minute about the other participants.','Kiss the person next to you in any direction',
'Dance with no music for 1 minute.','Let the person on your right draw on your face.','Give your phone to another player who can send one text saying anything they want to one of your fb friend.',
'Swap clothes with someone of the opposite sex(the cloths that you are actually wearing.not something like jacket)','Call a friend, pretend its their birthday, and sing “Happy Birthday” to them.',
'Take a selfie on the toilet and post it.','Spin around 12 times and try to walk straight.','Put on a blindfold and touch the other players faces until you can figure out who it is.',
'Do 5 minutes of stand-up comedy.','Quack like a duck until your next turn.','stare at the player next to you until the next round','Act like a chicken until your next turn.',
'sing a song to impress someone in this room','Find your first crush on social and DM them',
'group dare: you are even. so, even ones switch your seat with the person next to you','Describe the most attractive quality of every person in the room.',
'Describe the most disgusting thing of every person in the room.','Put on makeup without looking in the mirror, then leave it like that for the rest of the game',
'let the opposit person draw something on your face','Read aloud the last five things you searched on your phone.',
'In the next 10 minutes, find a way to scare another player and make it a surprise','Prank call one of your family members.','Prank call a person of your opposit gender and seduce him/her. It must be someones crush in this room :)',
'Bark like a dog','show the recent 5 photos in your gallery']

#insult
list3=['Looser!','Good for nothing!','Asshole','Go home fucker','Fuck your dog','quit! ballsack!','Lick my ass','this group dont need a boring person like you',
'you should better get out of the room','stay with your mom child','Get some balls dude','Dick sucker']


#counting the lists
a=0
for i in list2:
    a+=1
print(a,'')

#take player number
v = int(input("give the number of players : "))

#take players name
Names=[] #just the list of names
names={} #names with truth scores
scores={}
for i in range (v):
    n=input("Give your name  : ")
    Names.append(n)
    names[n]=0
    scores[n]=0


j=1
while True:

    round=int(input('How many round do you want to play ? : ')) # taking the number of rounds
    
    #start the game
    i=0
    while(i<round):
        q=random.choice(Names)                 # select a random name 
        print('your turn : ',q)                # print the name
        a = input ("truth or dare? : ")        # pick truth or dare
        if a=='truth':                         # truth block
            if names[q]<2:                     # can continue if he has not choosen truth 2 times in a row
                 print(random.choice(list1))   # pick random truth
                 names[q]+=1
                 c=input('Did the player succeed to say the truth ? (yes/no) : ') # score part
                 if c=='yes':                     # if yes the score will add 1                   
                     scores[q]+=1
                     print('Congrats!')
                 elif c=='no':                    # if failed then score will be subtracted by 2 and scolded 
                     scores[q]-=2
                     print(random.choice(list3))
                 else:
                     print('Sorry! you gave an invalid input. So, get a free -1 penalty')  # penalty negative 1 for the score
                     scores[q]-=1
            else:                              # can not continue as he has choosen truth 2 times in a row and will get a penalty
                print('You have already choosen truth 2 times in a row. Free dare penalty : ', random.choice(list2))
                i+=-1

        elif a=='dare':
            print(random.choice(list2))
            c=input('Did the player succeed to complete the dare ? (yes/no) : ')
            if c=='yes':
                scores[q]+=1
                print(' Congrats! You have gutts ')
            elif c=='no':
                scores[q]-=2
                print(random.choice(list3))
            else:
                print('Sorry! you gave an invalid answer. So, get a free -1 penalty')
                scores[q]-=1

            if names[q]==1:
                names[q]+=-1
            elif names[q]==2:
                names[q]+=-2

        else:
            print('please give a valid input')

            if i>0:    
                i=i-1
            else:
                i=-1
        
        
        print("Press ENTER to end the number ",i+1,"  round ")
        input()

        print('Truth SCORE :')
        print('---------------------')
        print(names,'\n')
        print('Total SCORE :')
        print('---------------------')
        print(scores,'\n')
        i+=1
    
    r = int(input(' Do you want to play again ? (Press 3 to continue or something else to end) : '))
    
    if r!=3:
        print('Thank you for playing this game - Joy Chowdhury')
        break
    else:
        j+=1
        print('-----',j,'no game Started -----\n')

