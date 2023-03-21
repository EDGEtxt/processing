import keyboard as kb
import time as t
import random as rnd

place = [['','','','','',''],
         ['','','','','',''],
         ['','','','','',''],
         ['','','','','',''],
         ['','','','','',''],
         ['','','','_','','']]

lockedPoint = 0
ying = 0
xP = 4
point = [0,1,2,3,4,5]

l = input()
while l != 'выход':
    while True:
        # player [5][3]
        x0 = xP
        
        # очки
        if '*' not in place[0] and '*' not in place[1] and '*' not in place[2] and '*' not in place[3] and '*' not in place[4] and '*' not in place[5]:
            # спускается
            place[ying + 1][lockedPoint] = '*'
        if '*' in place[5][xP]:
            # попадает
            ying = 0
            lockedPoint = rnd.choice(point)
            place[5][xP] = '_'
            print("расава")
        else:
            # не попадает
            print('бывает')
            ying = 0
            rnd.choice(point)
                
                
        # управление
        if kb.press_and_release('A'):
            xP -= 1
        elif kb.press_and_release('D'):
            xP += 1
        
        
        # "стены"
        if xP == -1:
            xP += 1
        elif xP == 6:
            xP -= 1
        else:
            # движения игрока
            place[5][xP] = '_'
            place[5][x0] = ''
            
        for i in place:
            for y in i:
                print(y, end='')
            print()
            
        ying += 1
        t.sleep(1)
              
exit()
