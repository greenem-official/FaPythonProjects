import sys

def _add(a, b):
    return a + b

def _multiply(a, b):
    return a * b

def performOperations():
    s = 0
    if len(sys.argv) < 2:
        print('Введите в аргументах операцию и числа')
    else:
        oper = sys.argv[1]
        func = None
        if oper == '+' or oper == 'сложить' or oper == 'плюс':
            func = _add
        elif oper == '*' or oper == 'умножить' or oper == 'умножить на' or oper == 'умножение':
            func = _multiply
            s = 1
        else:
            print('Неизвестная операция:', oper)

        if func:
            try:
                for i in range(2, len(sys.argv)):
                    num = int(sys.argv[i])
                    s = func(s, num)
                return s
            except ValueError:
                print('Передано не число')
