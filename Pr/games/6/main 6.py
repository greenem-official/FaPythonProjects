b = []
player = 1
sizeX = 10
sizeY = 10
defaultItem = ' '
usedItem = 'X'
winAfter = 3

def toStr(num):
    if num < 10:
        return ' ' + str(num)
    else:
        return str(num)

def draw():
    print('   X ', end='')
    for i in range(len(b[0])):
        print((i + 1), '', end='')
    print()
    print(' Y   ', (len(b[0])) * '— ', sep='')
    for i in range(len(b)):
        print(toStr(i+1), ' | ', sep='', end='')
        for j in range(len(b[i])):
            if b[i][j] == '':
                print('0 ', end='')
            else:
                print(str(b[i][j]) + ' ', end='')
        print()
    print()

def setElem(x, y):
    if b[x][y] == defaultItem:
        b[x][y] = usedItem
        return True
    else:
        return False

def checkItem(x, y, alreadyChecked, found):
    s = str(x) + ' ' + str(y)
    if s in alreadyChecked or s in found:
        return 0
    c = 0
    if b[y][x] == usedItem:
        c += 1
        found.add(s)
        c += getRelative(x, y, alreadyChecked, found)
    else:
        alreadyChecked.add(s)
    return c

def getRelative(x, y, alreadyChecked, found):
    if len(found) >= winAfter:
        return 0
    c = 0
    if x > 0 and y > 0: # bottom left
        c += checkItem(x-1, y-1, alreadyChecked, found)
    if len(found) >= winAfter:
        return 0
    if x > 0: # left
        c += checkItem(x - 1, y, alreadyChecked, found)
    if len(found) >= winAfter:
        return 0
    if x > 0 and y < sizeY-1: # top left
        c += checkItem(x - 1, y + 1, alreadyChecked, found)
    if len(found) >= winAfter:
        return 0
    if y > 0: # bottom
        c += checkItem(x, y - 1, alreadyChecked, found)
    if len(found) >= winAfter:
        return 0
    if y < sizeY-1: # top
        c += checkItem(x, y + 1, alreadyChecked, found)
    if len(found) >= winAfter:
        return 0
    if x < sizeX-1 and y < sizeY-1: # top right
        c += checkItem(x + 1, y + 1, alreadyChecked, found)
    if len(found) >= winAfter:
        return 0
    if x < sizeX-1: # right
        c += checkItem(x + 1, y, alreadyChecked, found)
    if len(found) >= winAfter:
        return 0
    if x < sizeX-1 and y > 0: # bottom right
        c += checkItem(x + 1, y - 1, alreadyChecked, found)
    if len(found) >= winAfter:
        return 0
    return c

def decideResults(arr):
    if arr[1] < arr[2] and arr[1] < arr[3]:
        print('Первый игрок победил!')
    elif arr[2] < arr[1] and arr[2] < arr[3]:
        print('Второй игрок победил!')
    elif arr[3] < arr[1] and arr[3] < arr[2]:
        print('Третий игрок победил!')
    else:
        print('Нет единого победителя')

def validate():
    done = False
    for i in range(len(b)):
        if done:
            break
        for j in range(len(b[i])):
            if b[i][j] == usedItem:
                alreadyChecked = set()
                found = set()
                relative = getRelative(i, j, alreadyChecked, found)
                # print(str(i) + ':' + str(j) + ' ' + str(relative) + ' ' + str(alreadyChecked) + ' ' + str(found))
                if len(found) >= winAfter:
                    done = True
                    break

    if not done:
        return

    if player == 1:
        print('Второй игрок победил!')
    elif player == 2:
        print('Первый игрок победил!')
    return True

def playerNumText():
    plText = 'Первый'
    if player == 2:
        plText = 'Второй'
    elif player == 3:
        plText = 'Третий'
    return plText

if __name__ == '__main__':
    for i in range(sizeY):
        c = []
        for j in range(sizeX):
            c.append(defaultItem)
        b.append(c)

    draw()
    while True:
        try:
            y, x = input(playerNumText() + ' игрок: Введите координаты x и y: ').split()
            if not x.isdigit() or not y.isdigit():
                print("Координаты должны быть двумя числами!")
                continue
            x = int(x)
            y = int(y)
            if x < 1 or x > sizeX or y < 1 or y > sizeY:
                print("Номер должен быть в диапазоне 1-10 и 1-10!", sep='')
                continue
            if not setElem(x-1, y-1):
                print("Данная ячейка уже занята!")
                continue
            draw()
            if validate():
                break

            player += 1
            if player > 2:
                player = 1
        except ValueError:
            print("Координаты должны быть двумя числами!")
        except KeyboardInterrupt:
            pass