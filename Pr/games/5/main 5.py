b = []
player = 1
sizeX = 5
sizeY = 4

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

# def draw():
#     for i in range(len(b)):
#         print(toStr(i+1), ' | ', sep='', end='')
#         for j in range(len(b[i])):
#             if b[i][j] == '':
#                 print('_ ', end='')
#             else:
#                 print(str(b[i][j]) + ' ', end='')
#         print()
#     print(' Y   ', (len(b[0]) * 2 - 1) * '—', sep='')
#     print('   X ', end='')
#     for i in range(len(b[0])):
#         print((i+1), '', end='')
#     print()

def setElem(x, y):
    if b[x][y] == '':
        b[x][y] = player
        return True
    else:
        return False

def getNearAmount(x, y, playerNum):
    c = 0
    if x > 0 and y > 0: # bottom left
        if b[y - 1][x - 1] == playerNum:
            c += 1
    if x > 0: # left
        if b[y][x - 1] == playerNum:
            c += 1
    if x > 0 and y < sizeY-1: # top left
        if b[y+1][x-1] == playerNum:
            c += 1
    if y > 0: # bottom
        if b[y-1][x] == playerNum:
            c += 1
    if y < sizeY-1: # top
        if b[y+1][x] == playerNum:
            c += 1
    if x < sizeX-1 and y < sizeY-1: # top right
        if b[y + 1][x + 1] == playerNum:
            c += 1
    if x < sizeX-1: # right
        if b[y][x + 1] == playerNum:
            c += 1
    if x < sizeX-1 and y > 0: # bottom right
        if b[y-1][x+1] == playerNum:
            c += 1
    return c

def toActualPoints(n):
    return max(0, n // 2 - 1)

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
    done = True
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j] == '':
                pass
                return False

    minusPoints = {}
    for p in range(1, 4):
        counter = 0
        for i in range(len(b)):
            for j in range(len(b[i])):
                if b[i][j] == p:
                    counter += getNearAmount(j, i, p)
        minusPoints[p] = counter
        counter = 0

    # print(minusPoints)
    print('Штрафные очки: ', toActualPoints(minusPoints[1]), ', ', toActualPoints(minusPoints[2]), ', ', toActualPoints(minusPoints[3]), sep='')

    decideResults(minusPoints)
    return True

def playerNumText():
    plText = 'Первый'
    if player == 2:
        plText = 'Второй'
    elif player == 3:
        plText = 'Третий'
    return plText

if __name__ == '__main__':
    size = 10
    chance = 4
    for i in range(sizeY):
        c = []
        for j in range(sizeX):
            c.append('')
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
            if x < 1 or x > 4 or y < 1 or y > 5:
                print("Номер должен быть в диапазоне 1-5 и 1-4!", sep='')
                continue
            if not setElem(x-1, y-1):
                print("Данная ячейка уже занята!")
                continue
            draw()
            if validate():
                break

            player += 1
            if player == 4:
                player = 1
        except ValueError:
            print("Координаты должны быть двумя числами!")
        except KeyboardInterrupt:
            pass