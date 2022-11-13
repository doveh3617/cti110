#CTI-110
#P4HW1 - Score List
#Hayley Dove
#November 12, 2022
#
#Program gets number of grades from user
numofscores = int(input('How many scores do you want to enter? '))
print()
#empty list to store input scores
scoreslist=[]
#for loop to take the input
for i in range (1,numofscores+1):
#while loop to take input until it is correct by program's standards
    while True:
        try:
            score=float(input('Enter score #{}: '.format(i)))

            if score>=0 and score<=100:
                scoreslist.append(score)
                break
            else:
                print('INVALID Score entered!!!!')
                print('Score should be between 0 and 100')
                print('Enter score{} again: ')
        except:
            continue

print()
print()
print('------------------------Results------------------------')

#printing lowest score
lowestscore=min(scoreslist)
print(f'Lowest score  : {lowestscore:.1f}')

#printing modified list after dropping lowest score
scoreslist.remove(lowestscore)
print('Modified List :', scoreslist)

#printing average of modified list
avgofscoreslist=sum(scoreslist)/len(scoreslist)
print(f'Scores Average: {avgofscoreslist:.1f}')

#printing letter grade
if avgofscoreslist>=90 and avgofscoreslist<=100:
    print('Grade         : A')
elif avgofscoreslist>=80 and avgofscoreslist<=90:
    print('Grade         : B') 
elif avgofscoreslist>70 and avgofscoreslist<=80:
    print('Grade         : C')
elif avgofscoreslist>60 and avgofscoreslist>=70:
    print('Grade         : D')
else:
    print('Grade         : F')

print('-------------------------------------------------------')

    
        






    
                          
