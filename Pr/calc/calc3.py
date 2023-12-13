import re
numbersPattern = r'([\(\)\+\-\*\/\s]*\s*)?([^\(\)\+\-\*\/]+)(\s*[\(\)\+\-\*\/\s]*)?'

def getNumHundreds(raw):
    if not raw:
        return 0
    raw = raw.strip()

    if raw == 'сто':
        return 100, None
    elif raw == 'двести':
        return 200, None
    elif raw == 'триста':
        return 300, None
    elif raw == 'четыреста':
        return 400, None
    elif raw == 'пятьсот':
        return 500, None
    elif raw == 'шестьсот':
        return 600, None
    elif raw == 'семьсот':
        return 700, None
    elif raw == 'восемьсот':
        return 800, None
    elif raw == 'девятьсот':
        return 900, None

    return None, 'Неверный формат сотен: "' + raw + '"'

def getNumTens(raw):
    if not raw:
        return 0
    raw = raw.strip()

    if raw == 'двадцать':
        return 20, None
    elif raw == 'тридцать':
        return 30, None
    elif raw == 'сорок':
        return 40, None
    elif raw == 'пятьдесят':
        return 50, None
    elif raw == 'шестьдесят':
        return 60, None
    elif raw == 'семьдесят':
        return 70, None
    elif raw == 'восемьдесят':
        return 80, None
    elif raw == 'девяносто':
        return 90, None

    return None, 'Неверный формат десятков: "' + raw + '"'

def getNumOnes(raw):
    if not raw:
        return 0
    raw = raw.strip()

    if raw == 'один' or raw == 'одна':
        return 1, None
    elif raw == 'два' or raw == 'две':
        return 2, None
    elif raw == 'три':
        return 3, None
    elif raw == 'четыре':
        return 4, None
    elif raw == 'пять':
        return 5, None
    elif raw == 'шесть':
        return 6, None
    elif raw == 'семь':
        return 7, None
    elif raw == 'восемь':
        return 8, None
    elif raw == 'девять':
        return 9, None
    elif raw == 'десять':
        return 10, None
    elif raw == 'одиннадцать':
        return 11, None
    elif raw == 'двенадцать':
        return 12, None
    elif raw == 'тринадцать':
        return 13, None
    elif raw == 'четырнадцать':
        return 14, None
    elif raw == 'пятнадцать':
        return 15, None
    elif raw == 'шестнадцать':
        return 16, None
    elif raw == 'семнадцать':
        return 17, None
    elif raw == 'восемнадцать':
        return 18, None
    elif raw == 'девятнадцать':
        return 19, None

    return None, 'Неверный формат единиц: "' + raw + '"'

def getBasicNumber(s):
    hundreds = 0
    tens = 0
    ones = 0

    p = s.split()
    if len(p) == 0:
        print('Встречено "пустое" число!')
        return None, None
    if len(p) >= 1:
        ones, err1 = getNumOnes(p[len(p) - 1])
        if not ones:
            ones = 0
            tens, err2 = getNumTens(p[len(p) - 1])
            if not tens:
                hundreds, err3 = getNumHundreds(p[len(p) - 1])
                if not hundreds:
                    return None, err1
    if len(p) >= 2:
        tens, err2 = getNumTens(p[len(p) - 2])
        if not tens:
            tens = 0
            hundreds, err3 = getNumHundreds(p[len(p) - 2])
            if not hundreds:
                return None, err1
    if len(p) >= 3:
        hundreds, err3 = getNumHundreds(p[len(p) - 3])
        if not hundreds:
            return None, err3

    return hundreds + tens + ones, None

def getNumPartWhole(s):
    p1, err = getBasicNumber(s)
    if not p1:
        return None, err

    return p1, None

def getNumber(s):
    # maybeOperation, err1 = getOperation(s, sOrig)
    # print(maybeOperation, err1)
    # if maybeOperation:
    #     return maybeOperation, None

    sign = 1
    if s.startswith('минус '):
        sign = -1
        s = s[6:]

    a, err2 = getNumPartWhole(s)
    if a:
        return sign * a, None
    else:
        return None, err2

def reverseGetNumber(n):
    # print('Original:', '{0:.3f}'.format(n))
    n = int(n)
    if n == 0:
        return 'ноль'
    s = ''
    if n < 0:
        s += "минус "
        n *= -1

    if n >= 1000000:
        amount = int(n // 1000000)
        s += reverseGetNumber(amount).strip() + ' миллион'
        if 2 <= amount % 10 <= 4:
            s += 'а '
        elif amount % 10 >= 5 or amount % 10 == 0:
            s += 'ов '
        else:
            s += ' '
        n -= amount * 1000000
    if n >= 1000:
        amount = int(n // 1000)
        s += reverseGetNumber(amount).strip() + ' тысяч'
        if amount % 10 == 1:
            s += 'а '
        elif 2 <= amount % 10 <= 4:
            s += 'и '
        else:
            s += ' '
        n -= amount * 1000
    if n >= 100:
        amount = int(n // 100)
        space = True
        if amount == 1:
            s += 'сто'
        elif amount == 2:
            s += 'двести'
        elif amount == 3:
            s += 'триста'
        elif amount == 4:
            s += 'четыреста'
        elif amount == 5:
            s += 'пятьсот'
        elif amount == 6:
            s += 'шестьсот'
        elif amount == 7:
            s += 'семьсот'
        elif amount == 8:
            s += 'восемьсот'
        elif amount == 9:
            s += 'девятьсот'
        else:
            space = False
        if space:
            s += ' '
        n -= amount * 100
    if n >= 10:
        amount = int(n // 10)
        space = True
        if n == 10:
            s += 'десять'
        elif n == 11:
            s += 'одиннадцать'
            n -= 1
        elif n == 12:
            s += 'двенадцать'
            n -= 2
        elif n == 13:
            s += 'тринадцать'
            n -= 3
        elif n == 14:
            s += 'четырнадцать'
            n -= 4
        elif n == 15:
            s += 'пятнадцать'
            n -= 5
        elif n == 16:
            s += 'шестнадцать'
            n -= 6
        elif n == 17:
            s += 'семнадцать'
            n -= 7
        elif n == 18:
            s += 'восемнадцать'
            n -= 8
        elif n == 19:
            s += 'девятнадцать'
            n -= 9
        elif amount == 2:
            s += 'двадцать'
        elif amount == 3:
            s += 'тридцать'
        elif amount == 4:
            s += 'сорок'
        elif amount == 5:
            s += 'пятьдесят'
        elif amount == 6:
            s += 'шестьдесят'
        elif amount == 7:
            s += 'семьдесят'
        elif amount == 8:
            s += 'восемьдесят'
        elif amount == 9:
            s += 'девяносто'
        else:
            space = False
        if space:
            s += ' '
        n -= amount * 10
    if n > 0:
        space = True
        if n == 1:
            s += 'один'
        elif n == 2:
            s += 'два'
        elif n == 3:
            s += 'три'
        elif n == 4:
            s += 'четыре'
        elif n == 5:
            s += 'пять'
        elif n == 6:
            s += 'шесть'
        elif n == 7:
            s += 'семь'
        elif n == 8:
            s += 'восемь'
        elif n == 9:
            s += 'девять'
        else:
            space = False
        if space:
            s += ' '

    return s

def performEverything(s):
    s = s.replace('скобка открывается', '(')
    s = s.replace('скобка закрывается', ')')

    s = s.replace('плюс', '+')
    s = s.replace('минус', '-')
    s = s.replace('умножить на', '*')
    s = s.replace('разделить на', '/')

    s = s.replace('возвести в степень', '**')
    s = s.replace('^', '**')

    # print(s)
    for m in re.finditer(numbersPattern, s):
        orig = m.group(2).strip()
        num, err = getNumber(orig)
        # print(orig, num)
        if err:
            return None, err
        # newS = s[0 : m.start()] + str(num) + s[m.end() + 1 : len(s)]
        # s = newS
        # print(m.start(), m.end())
        s = s.replace(orig, str(num), 1)

    try:
        res = eval(s)
    except SyntaxError as e:
        return None, e

    return res, None

# Примеры:
#
# скобка открывается пять плюс два скобка закрывается умножить на три минус один
# два плюс скобка открывается скобка открывается сорок плюс три скобка закрывается плюс два скобка закрывается умножить на три минус один

s = 'два плюс скобка открывается скобка открывается сорок два плюс три скобка закрывается плюс два скобка закрывается умножить на три минус один'
result, err = performEverything(s)
if result:
    print('Результат (тест):\n' + reverseGetNumber(result))
else:
    print(err)

# print(getNumber('сорок'))