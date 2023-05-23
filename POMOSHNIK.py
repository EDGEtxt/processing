import time
import random
import pyautogui
import subprocess
import webbrowser

note1 = ''
note2 = ''
note3 = ''

print('здравствуйте, я бот-помощник. советую сначала обратиться к команде "помощь"')
time.sleep(1)
comand = input("введите команду: ")

#списки
anekdot = ["колобок повесился","ты алмаз в моей жизни... такой же глупый непробиваемый","ты мой ангел. типа с небес спустился? типа парашют не раскрылся",'открывает как то мужик ящик а там армяне в нарды рубятся',"Здоровье - это отсутствие знаний про свои заболевания.","man im dead"]
skazka = ["неа, мне лень","жили как то рак щука и осёл. рак был синий, щука зелёный а олень бесцветным...","спи и завтра я дам тебе конфету","бабайка...","жили как то были а вот и не были и не жили, конец","аяаяаяаяй баллада эта для бессоницы твоеееей"]

#действия
while comand != 'выход':
    if comand == 'помощь':
        print('"анекдот" - рассказывает анекдот')
        print('"сказка на ночь" - я думаю понятно')
        print('"важная новость" - рассказывает важные и свежие новости')
        print('"записки" - показывает написанные заметки')
        print('"создание заметки" - пиши чё хош')
        print('"запомнить контакт" - ФИО + номер телефона (без плюса)p')
        print('"выход" - закрывает меня')
        print('"prize" - kaboom (ломает всё, не советую)')
        comand = input("введите команду: ")
    elif comand == 'анекдот':
        print(random.choice(anekdot))
        comand = input('введите следующую команду: ')
    elif comand == 'сказка на ночь':
        print(random.choice(skazka))
        comand = input('введите следующую команду: ')
    elif comand == 'важная новость':
        confirm = pyautogui.confirm(text = "вы точно хотите посмотреть новости?", title = "важные новости", buttons = ["да", "нет"])
        if confirm == "да":
            webbrowser.open('https://ria.ru')
            comand = input('введите следующую команду: ')
        else:
            print('ok')
            comand = input('введите следующую команду: ')
    elif comand == 'записки':
        hmm = int(input('какую заметку хотите прочитать: 1 2 или 3? '))
        if hmm == 1:
            print(note1)
        elif hmm == 2:
            print(note2)
        elif hmm == 3:
            print(note3)
        else:
            print('это не число либо не 1 2 или 3')
        comand = input('введите следующую команду: ')
    elif comand == 'создание заметки':
        print('вам можно написать 3 заметки')
        hmmm = int(input('в какую хотите записать: 1 2 или 3? '))
        if hmmm == 1:
            note1 = input('')
        elif hmmm == 2:
            note2 = input('')
        elif hmmm == 3:
            note3 = input('')
        else:
            print('это не число либо не 1 2 или 3')
        comand = input('введите следующую команду: ')
    elif comand == 'запомнить контакт':
        name = input('ваше имя: ')
        secondname = input('ваша фамилия: ')
        noname = input('ваше отчество: ')
        number = int(input('ваш номер телевона: '))
        comand = input('введите следующую команду: ')
        
        #это кстати вирус который можно убрать только выключением программы
    elif comand == 'prize':
        while True:
            time.sleep(0.5)
            pyautogui.confirm(text = "IS'S TIME TO BE A [[BIG SHOT!]]", title = "SPAMTON G. SPAMTON", buttons = ["DEAL", "DEAL"])
            time.sleep(3.5)
            webbrowser.open('https://knowyourmeme.com/photos/2203919-spamton-g-spamton')
    else:
        comand = input('повторите команду: ')

#после выхода
print('удачи')
exit
