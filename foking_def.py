import random
list1 = list()

def func1():
    
    a, b, c = 0, 0, 0
    
    while a == b or b == c or c == a:
        a = random.randint(0,9)
        b = random.randint(0,9)
        c = random.randint(0,9)
    
    list1 = [a, b, c]
    return list1

numbers = func1()
z = numbers

y = list()

while not (numbers[0] == "*" and numbers[1] == "*" and numbers[2] == "*"):

    num = int(input())
    pos = int(input())
    
    if num in numbers:
        
        if numbers[pos] == num:
            print("горячо НАЙДЕНО")
            y.append(num)
            numbers[pos] = "*"
        else:
            print("тепло")
            
    else:
        print("холодно")
        
print(y)



#if a[0] == b[0]:
#    print(a[0] + " и " + b[0] + " одинаковы")
#else:
#    if a[1] == b[1]:
#        print(a[1] + " и " + b[1] + " одинаковы")
#    else:
#        if a[2] == b[2]:
#            print(a[2] + " и " + b[2] + " одинаковы")
#        else:
#            print('всё уникально')

#for i in range(len(a)):
#    for p in range(len(b)):
#        if a[i] == b[p]:
#            print(a[i] + ' и ' + b[p] + " одинаковы в 2 трёхзначных числах")
#        else:
#            print(a[i] + " и " + b[p] + " не совпадают")




