from random import *

a = []
first = True

def toStr(num):
    if num < 10:
        return ' ' + str(num)
    else:
        return str(num)

def draw():
    for i in range(len(a)):
        print(toStr(i+1), ' | ', sep='', end='')
        for j in range(len(a[i])):
            if a[i][j]:
                print('o ', end='')
            else:
                print('_ ', end='')
        print()
    print('     ', (len(a) * 2) * '—', sep='')
    print('     ', end='')
    for i in range(len(a)):
        print((i+1), '', end='')
    print()

def remove(t, x):
    hadAny = False
    if t == 'г':
        i = x
        for j in range(len(a)):
            if a[i][j]:
                hadAny = True
            a[i][j] = False
    elif t == 'в':
        j = x
        for i in range(len(a)):
            if a[i][j]:
                hadAny = True
            a[i][j] = False
    return hadAny

def validate():
    global first
    hasAny = False
    for i in range(len(a)):
        if not hasAny:
            for j in range(len(a[i])):
                if not hasAny:
                    if a[i][j]:
                        hasAny = True

    if not hasAny:
        if first:
            print('Первый игрок победил!')
            return True
        else:
            print('Второй игрок победил!')
            return True
    return False

if __name__ == '__main__':
    size = 10
    chance = 4
    for i in range(size):
        b = []
        for j in range(size):
            r = randint(0, chance-1)
            b.append(r == 0)
        a.append(b)

    draw()
    # global first
    while True:
        try:
            if first:
                t, x, = input('Первый игрок: Введите тип (горизонталь - г, вертикаль - в) и номер: ').split()
            else:
                t, x = input('Второй игрок: Введите тип (горизонталь - г, вертикаль - в) и номер: ').split()
            if not x.isdigit():
                print("Ввод должен быть двумя числом!")
                continue
            if t != 'г' and t != 'в':
                print('Тип должен быть "г" (горизонталь) или "в" (вертикаль)!')
                continue
            x = int(x)
            if x < 1 or x > size:
                print("Номер должен быть в диапазоне 1-", size, "!", sep='')
                continue
            if not remove(t, x-1):
                print("Данная линия пуста!")
                continue
            draw()
            if validate():
                break
            first = not first
        except ValueError:
            print("Ввод должен быть двумя числами!")