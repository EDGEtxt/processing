import time
import random
import pyautogui
import subprocess
import keyboard as kb
import webbrowser as web
import subprocess as sub

def saper():
    # массив поля, * — пустое поле, # — стена
    pole = [["*","*","*","#","*","*","*","*","*","*","*","*"],
            ["*","*","*","#","*","*","*","*","*","*","*","*"],
            ["*","*","*","#","*","*","*","*","*","*","*","*"],
            ["*","*","*","#","*","*","*","#","#","#","#","#"],
            ["*","*","*","#","#","#","#","#","*","#","*","*"],
            ["*","*","*","#","*","*","*","*","*","#","*","*"],
            ["#","#","#","#","*","*","*","*","*","#","#","#"],
            ["*","*","*","#","*","*","*","*","*","#","*","*"],
            ["*","*","*","#","*","*","*","*","*","#","*","*"],
            ["*","*","*","#","*","*","*","*","*","#","*","*"],
            ["*","*","*","#","*","*","*","*","*","#","*","*"],
            ["*","*","*","#","*","*","*","*","*","#","*","*"]]

    # то, что будет выводиться на экран
    vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"],
                    ["•","•","•","•","•","•","•","•","•","•","•","•"]]

    # вывод поля на экран, для любого, абстрактного списка будет работать


    def vyvodPolya(spisok):
        for stroka in spisok:
            for kletka in stroka:
                print(kletka,end='')
            print()
        
        
    # проверка поля на то, что внутри него
    # если поле пустое, проверяются все клетки вокруг него
    # если стена — не проверяются
    # если поле уже было открыто — оно не проверяется

    def check(stroka,stolb):
        # если клетка ещё не открыта
        if vidimost_polya[stroka][stolb] == "•":
            # открываем
            vidimost_polya[stroka][stolb] = pole[stroka][stolb]
            # если оно оказалось пустым
            if pole[stroka][stolb] == "*":
                # проверяем все соседние, только если они существуют
                # а то выйдем за пределы поля, Python ругать будет
                if stroka-1 >= 0:
                    check(stroka-1,stolb)
                    if stolb-1 >= 0:
                        check(stroka-1,stolb-1)
                    if stolb+1 < len(pole[stroka]):
                        check(stroka-1,stolb+1)
                    
                if stroka+1 < len(pole):
                    check(stroka+1,stolb)
                    if stolb-1 >= 0:
                        check(stroka+1,stolb-1)
                    if stolb+1 < len(pole[stroka]):
                        check(stroka+1,stolb+1)
                    
                if stolb-1 >= 0:
                        check(stroka,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka,stolb+1)
                
                
                
    # добавим проверку, остались ли ещё неоткрытые элементы поля
    # функция будет возвращать True, если больше нет
    # и False, если ещё остались

    def isOpen():
        # считаем, что поле открыто всё
        opened = True
        #для каждой строки в видимости поля
        for stroka in vidimost_polya:
            # если хотя бы в одной нашлось закрытое поле
            if "•" in stroka:
                # значит неправда, поле ещё не всё открыто
                opened = False
        return opened

#def shipwar():
    
    
def catcher():
    place = [[' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ',' ',' ',' '],
             [' ',' ',' ','_',' ',' ']]

    lockedPoint = 0
    ying0 = 0
    ying = -1
    xP = 3
    point = [0,1,2,3,4,5]
    
    print("что бы закончить нажмите на R")
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)
    
    while True:
        # player [5][3]
            
        # для удаления палок
        x0 = xP
        
        
        # управление
        if kb.is_pressed('A'):
            xP -= 1
        elif kb.is_pressed('D'):
            xP += 1
        elif kb.is_pressed('R'):
            break
        else:
            xP = xP
            
        # "стены"
        if xP == -1:
            xP += 1
        elif xP == 6:
            xP -= 1

        # движения игрока
        else:
            place[5][x0] = ' '
            place[5][xP] = '_'
            
            
        ying0 = ying
                    
        # очки спускаются
        ying += 1
        place[ying][lockedPoint] = '*'
        place[ying0][lockedPoint] = ' '   
        
        # попадает
        if '*' in place[5] and '*' in place[5][xP]:
            ying = -1
            lockedPoint = random.choice(point)
            place[5][xP] = '_'
            print("красава")
            
        # не попадает
        elif '*' in place[5] and '*' not in place[5][xP]:
            print('бывает')
            ying = -1
            place[5][lockedPoint] = ' '
            lockedPoint = random.choice(point)            
            
            
        # вывод таблицы через 1 секунду
        for i in place:
            for y in i:
                print(y, end='')
            print()
        time.sleep(1)
        print("______")
              
def ShipWar():
    place = [['O','T','O','O','O','O'],
             ['O','O','O','O','T','O',],
             ['T','O','T','O','O','O',],
             ['O','O','O','O','O','O',],
             ['O','O','O','T','O','O',],
             ['O','O','O','O','O','T',]]

    place2 = [['I','O','I','O','O','O'],
              ['O','O','O','O','O','I',],
              ['I','O','I','O','O','O',],
              ['I','O','O','O','O','O',],
              ['O','O','O','I','O','O',],
              ['O','O','O','O','O','O',]]

    bot_choice = [0,1,2,3,4,5]

    X1 = 0
    Y1 = 0

    X2 = 0
    Y2 = 0

    type_start = input()
    
    while ('T' in place[0] or 'T' in place[1] or 'T' in place[2] or 'T' in place[3] or 'T' in place[4] or 'T' in place[5]) and ('I' in place2[0] or 'I' in place2[1] or 'I' in place2[2] or 'I' in place2[3] or 'I' in place2[4] or 'I' in place2[5]):
    
        print('у каждого по x кораблей')

        Y2 = input()
        X2 = input()
        
        if Y2 == 'таблица' or X2 == 'таблица':
            for i in place:
                for y in i:
                    print(y,end='')
                print()
            Y2 = int(input())
            X2 = int(input())
            
        else:
            if X2 >= 6 or Y2 >= 6:
                print('не братан, за полем ставить незя')
        
            elif X2 <= -1 or Y2 <= -1:
                print('не братан, за поле не выходи то')
            else:
                if place2[Y2][X2] == 'I':
                    print('поподание!')
                    place2[Y2][X2] = 'X'
                    print(place2)
                else:
                    place2[Y2][X2] = '0'
                
        time.sleep(1)      
        print('следующий игрок')
        time.sleep(2)
        
        Y1 = random.choice(bot_choice)
        print(Y1)
        time.sleep(0.5)
        X1 = random.choice(bot_choice)
        print(X1)
        time.sleep(0.5)
        
        time.sleep(1)
    
        if X1 >= 6 or Y1 >= 6:
            print('не братан, за полем ставить незя')
        
        elif X1 <= -1 or Y1 <= -1:
            print('не братан, за поле не выходи то')
        else:
            if place[Y1][X1] == 'T':
                place[Y1][X1] = 'X'
                print("поподание!")
            else:
                place[Y1][X1] = '0'
    
        X1 = 0
        Y1 = 0
        X2 = 0
        Y2 = 0
        
        time.sleep(1)
        print("следующий игрок")
        time.sleep(2)


questions1 = ['крепастное право отменил Александр II?', 'крепостное право отменили в 1869 году?', 'первый телефон появился в 1876?']
answer1 = ['R', 'L', 'R']
questions2 = ['люди начали делать музыку в эпоху Античности?', 'первые компьютерные игры созданны в 1930 годах?', 'официально доказали что земля круглая в 1543 году?']
answer2 = ['L', 'L', 'R']
questions3 = ['Юрий Гагарин полетел в космос в 1967 году?', 'NASA основали в 1958 году?', 'последний открытый бозон "Хиггса" был открыт в 2005 году?']
answer3 = ['L', 'R', 'L']
questions4 = ['лампочку создал Томас Эдисон в 1879 году?', 'человек попал на луну в 1966 году?', 'я сделал этоу игру по приколу?']
answer4 = ['R', 'L', 'R']
q1 = False
q2 = False
q3 = False
q4 = False

print("Здравствуйте, я бот для игр, записей и поиска")
time.sleep(1)
print('прошу, если вы открываете меня первый раз то ознакомьтесь с функциями при помощи команды "help"')
time.sleep(1)
lst1 = ['"saper" - игра в сапёра', '"catcher" - игра в поймай звезду', '"R or L" - игра в правду или лож', '"ShipWar" - морской бой', '"write" - записать в саписки', '"read" - прочитать записки', '"SawIt" - просмотр названий созданных записок', '"search" - поиск в интернете', '"open" - открыть приложение на компьютере (ТРЕБУЕТСЯ ССЫЛКА НА РАСПОЛОЖЕНИЕ)']
d = dict()
read = list()


Enter = input('впишите команду: ')
while Enter != 'quit':
    if Enter == 'help':
        for i in range(len(lst1)):
            print(lst1[i])
        Enter = input('впишите команду: ')
        
    if Enter == 'saper':
        saper()
        Enter = input('впишите команду: ')
    
    if Enter == 'catcher':
        catcher()
        Enter = input("хорошая игра. что дальше?: ")
    
    if Enter == 'write':
        a = input("назовите записку: ")
        read.append(a)
        print(" ")
        print("записка создана")
        print(" ")
        b = input()
        d[a] = list()
        d[a].append(b)
        Enter = input('впишите команду: ')
        
    if Enter == 'read':
        reed = input("какую записку вы хотите посмотреть: ")
        for i in range(len(d[reed])):
            print(d[reed][i])
        Enter = input('впишите команду: ')
    
    if Enter == "SawIt":
        for i in range(len(read)):
            print(read[i])
        Enter = input('впишите команду: ')
        
    if Enter == "R or L":
        print("в ответ писать R или L")
        time.sleep(1)
        choicer1 = random.choice(question1)
        x1 = input()
        if x1 == answer1[choicer1]:
            q1 = True
        else:
            q1 = False
        
        choicer2 = random.choice(question2)
        x2 = input()
        if x2 == answer2[choicer2]:
            q2 = True
        else:
            q2 = False
        
        choicer3 = random.choice(question3)
        x3 = input()
        if x3 == answer3[choicer3]:
            q3 = True
        else:
            q3 = False
        
        choicer4 = random.choice(question4)
        x4 = input()
        if x4 == answer4[choicer4]:
            q4 = True
        else:
            q4 = False
        
        if q1 and q2 and q3 and q4 == True:
            print("молодец всё правельно!")
        elif q1 or q2 or q3 or q4 == False:
            print("правельно не всё, постарайся лучше в следующий раз")
        Enter = input("что дальше?: ")
        
    if Enter == "search":
        url = input("впишите ссылку: ")
        web.open_new_tab(url)
        #https://youtu.be/Yn-ZhiLrQZc
        Enter = input("что дальше?: ")
        
    if Enter == "open":
        app = input("впишите ссылку на расположение приложения: ")
        sub.Popen = (app)
        #D:\OSU\osu!.exe
        Enter = input("что дальше?: ")
        
    if Enter == "ShipWar":
        ShipWar()
        print("игра окончена")
        time.sleep(1)
        Enter = input("что дальше?: ")
        
print("приходите снова!")
