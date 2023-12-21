# + 2 6 4
# * 2 6 4

import sys

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

s = 0
if len(sys.argv) < 2:
    print('Введите в аргументах операцию и числа')
else:
    oper = sys.argv[1]
    func = None
    if oper == '+' or oper == 'сложить' or oper == 'плюс':
        func = add
    elif oper == '*' or oper == 'умножить' or oper == 'умножить на' or oper == 'умножение':
        func = multiply
        s = 1
    else:
        print('Неизвестная операция:', oper)

    if func:
        try:
            for i in range(2, len(sys.argv)):
                num = int(sys.argv[i])
                s = func(s, num)
            print(s)
        except ValueError:
            print('Передано не число')
