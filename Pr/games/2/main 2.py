a = []

def draw():
    print(a[0][0], '|', a[1][0], '|', a[2][0], sep = '')
    print('—————', sep = '')
    print(a[0][1], '|', a[1][1], '|', a[2][1], sep = '')
    print('—————', sep = '')
    print(a[0][2], '|', a[1][2], '|', a[2][2], sep = '')
    print()

def validate():
    if a[0][0] != ' ' and a[0][0] == a[0][1] == a[0][2]\
            or a[1][0] != ' ' and a[1][0] == a[1][1] == a[1][2]\
            or a[2][0] != ' ' and a[2][0] == a[2][1] == a[2][2]\
            \
            or a[0][0] != ' ' and a[0][0] == a[1][0] == a[2][0]\
            or a[0][1] != ' ' and a[0][1] == a[1][1] == a[2][1]\
            or a[0][2] != ' ' and a[0][2] == a[1][2] == a[2][2]\
            \
            or a[0][0] != ' ' and a[0][0] == a[1][1] == a[2][2]\
            or a[0][2] != ' ' and a[0][2] == a[1][1] == a[2][0]:
        if a[0][0] == 'x':
            print('Первый игрок (x) победил!')
            return True
        else:
            print('Второй игрок (o) победил!')
            return True
    return False

if __name__ == '__main__':
    for i in range(3):
        b = []
        for j in range(3):
            b.append(' ')
        a.append(b)

    first = True
    while True:
        try:
            if first:
                x, y = input('Первый игрок (x): Введите x и y координаты: ').split()
            else:
                x, y = input('Второй игрок (o): Введите x и y координаты: ').split()
            # print(x)
            # print(y)
            if not x.isdigit() or not y.isdigit():
                print("Ввод должен быть двумя числами!")
                continue
            x = int(x)
            y = int(y)
            if x < 1 or x > 3 or y < 1 or y > 3:
                print("Числа должны быть в диапазоне 1-3!")
                continue
            if a[x-1][y-1] != ' ':
                print("Это ячейка уже занята!")
                continue
            if first:
                a[x-1][y-1] = 'x'
            else:
                a[x-1][y-1] = 'o'
            first = not first
            draw()
            if validate():
                break
        except ValueError:
            print("Ввод должен быть двумя числами!")