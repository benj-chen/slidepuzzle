#This is a slide puzzle aka the 15 puzzle. The idea is that you move the empty
#space around to arrange the randomized board to a solved board (see main, line
#10. It is still in the works. There are bugs involving the switching of the
#tiles. Work in progress but hope it works!
#Bugs: None!

#creating the randomized board
import random
from random import randint
from random import choice
main=('''|----|----|----|----|
| 01 | 02 | 03 | 04 |
|----|----|----|----|
| 05 | 06 | 07 | 08 |
|----|----|----|----|
| 09 | 10 | 11 | 12 |
|----|----|----|----|
| 13 | 14 | 15 |    |
|----|----|----|----|''')

solved=main
num=[24,29,34,39,68,73,78,83,112,117,122,127,156,161,166,171]
numbas=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16"]

#Add correct shuffling code here
for q in range(10000):

    
    loca = numbas.index("16")
    if loca==0: #top left
        randmv=random.choice([1,4])
    elif loca==1 or loca==2: #top middle
        randmv=random.choice([-1,1,4])
    elif loca==3: #top right
        randmv=random.choice([-1,4])
    elif loca==4 or loca==8: #middle left
        randmv=random.choice([-4,1,4])
    elif loca==7 or loca==11: #middle right
        randmv=random.choice([-4,-1,4])
    elif loca==12: #bottom left
        randmv=random.choice([-4,1])
    elif loca==13 or loca==14: #bottom middle
        randmv=random.choice([-4,-1,1])
    elif loca==15: #bottom right
        randmv=random.choice([-4,-1])
    else:
        randmv=random.choice([-4,-1,1,4])
    temp=numbas[loca]
    numbas[loca]=numbas[loca+randmv]
    numbas[loca+randmv]=temp
#end

for y in range(16):
    main1=main[0:num[y]]
    main2=main[num[y]+2:]
    main=main1+numbas[y]+main2
main=main.replace("16","  ")
print(main, "\n\n\n\n\n\nYou're trying to get from that to this:\n\n\n\n\n\n"+ solved)   #essentially I split up the string, added the random thing, and put the whole thing back together. String.replace() wouldn't work, and this is much better anyways

#Actual gameplay (work in progress)
#Will be using WASD, not arrow keys, difficult to program, maybe will go back later and mod.
#recalibrate list every time......

print("Type whatever characters are up, down, left, or right of the empty space.")
while main!=solved:
    while True: #get move
        move=input("Move: ")
        while move not in numbas:
            move=input("Move: ")
        for x in range(16): #-1 right, 1 left, -4 down, 4 up
            numbas[x]=main[num[x]:num[x]+2]
        numba = numbas.index("  ")-numbas.index(move)
        if main.find(move)==num[7] or num[11]: #right edge
            if numba==1 or numba == 4 or numba ==-4:
                break
        if main.find(move)==num[4] or num[8]:#left edge
            if numba == -1 or numba == 4 or numba == -4:
                break
        if main.find(move)==num[1] or num[2]: #upper edge
            if numba==-1 or numba == 1 or numba == -4:
                break
        if main.find(move)==num[13] or num[14]: #lower edge
            if numba==-1 or numba== 1 or numba == 4:
                break

        if main.find(move) == num[0]:#up lf corner
            if numba==-4 or numba==-1:
                break
        if main.find(move) == num[3]: # up rt corner
            if numba==-4 or numba==1:
                break
        if main.find(move) == num[12]: #lo lf corner
            if numba==4 or numba==-1:
                break
        if main.find(move) == num[15]: #lo rt corner
            if numba==4 or numba==1:
                break
        elif numba == 1 or numba == 4 or numba ==-1 or numba ==-4 or numba==0: #other
            break
    find=main.find(" " + move)
    space=main.find("   ")
    space1=find
    main=main[:find] + "   " + main[find+3:]
    main=main[:space+1] + move + main[space+3:]
    print(main)
print("Solved! Yay!")





""" Used parts
if y==3 and (z==1 or z==2): #bottom middle
        randmv=randint(1,3)
    if y==3 and z==0: #bottom left
        randmv=randint(1,2)
        if randmv==1:
            randmv=3
    if y==3 and z==3: #bottom right
        randmv=randint(1,2)
    if (y==1 or y==2) and x==3: #right middle
        randmv=randint(1,3)
        if randmv==3:
            randmv=4
    if y==0 and z==3: #right top
        randmv=randint(1,2)
        if randmv==2:
            randmv=4
    if y==0 and (z==1 or z==2): #top middle
        randmv=randint(1,3)
        if randmv==2:
            randmv=4
    if y==0 and z==0: #top left
        randmv=randint(1,2)
        if randmv==1:
            randmv=3
        if randmv==2:
            randmv==4
    if (y==1 or y==2) and z==0: #left middle
        randmv=randint(1,3)
        randmv+=1
    print(randmv)

    
    if randmv==1: #move left
        temp = numbasmut[y][z]
        numbasmut[y][z] = numbasmut[y][z-1]
        numbasmut[y][z-1] = temp
        
    elif randmv==2: #move up
        temp = numbasmut[y][z]
        numbasmut[y][z] = numbasmut[y-1][z]
        numbasmut[y-1][z] = temp
        
    elif randmv==3: #move right
        temp = numbasmut[y][z]
        numbasmut[y][z] = numbasmut[y][z+1]
        numbasmut[y][z-1] = temp
        
    elif randmv==4: #move down
        temp=numbasmut[y][z]
        numbasmut[y][z] = numbasmut[y+1][z]
        numbasmut[y+1][z] = temp
"""
