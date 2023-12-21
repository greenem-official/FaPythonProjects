# Доп. задание 2 (сложность 3)

import re

patternOperation = r'(.*)(\()((.*?)\s(\+-\*/)\s(.*))(\))(.*)'
simplePatternOperation = r'(.*?)\s(\+-\*/)\s(.*)'
patternLeftBrackets = r'(\((.*)\))\s*([\+\-\*\/])\s*([^\(\)]*)'  # 2 brackets content, 3 operation, 4 right operand
patternRightBrackets = r'([^\(\)]*)\s*([\+\-\*\/])\s*(\((.*)\))'  # 1 left operand, 2 operation, 4 brackets content
patternJustTwoNumbers = r'([^\(\)]*)\s*([\+\-\*\/])\s*([^\(\)]*)'  # 1 left operand, 2 operation, 3 right operand
numbersPattern = r'([\(\)\+\-\*\/\s]*\s*)?([^\(\)\+\-\*\/]+)(\s*[\(\)\+\-\*\/\s]*)?'

debug = False

def _getNumHundreds(raw):
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

def _getNumTens(raw):
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

def _getNumOnes(raw):
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

def _getBasicNumber(s):
    s = s.strip()

    hundreds = 0
    tens = 0
    ones = 0

    p = s.split()
    if len(p) == 0:
        print('Встречено "пустое" число!')
        return None, None
    if len(p) >= 1:
        ones, err1 = _getNumOnes(p[len(p) - 1])
        if not ones:
            ones = 0
            tens, err2 = _getNumTens(p[len(p) - 1])
            if not tens:
                hundreds, err3 = _getNumHundreds(p[len(p) - 1])
                if not hundreds:
                    return None, err1
    if len(p) >= 2:
        tens, err2 = _getNumTens(p[len(p) - 2])
        if not tens:
            tens = 0
            hundreds, err3 = _getNumHundreds(p[len(p) - 2])
            if not hundreds:
                return None, err2
    if len(p) >= 3:
        hundreds, err3 = _getNumHundreds(p[len(p) - 3])
        if not hundreds:
            return None, err3

    return hundreds + tens + ones, None

def getNumPartWhole(s):
    s = str(s).strip()
    p1, err = _getBasicNumber(s)
    if not p1:
        return None, 'Неверное число: "' + s + '": ' + err

    return p1, None

def getNumber(s):
    if debug:
        print('number', s)
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

def surroundAll(s, obj):
    c = 0
    m = 1
    amount = 0
    for m in re.finditer(obj, s):
        amount += 1
    for i in range(amount):
        cc = 0
        for m in re.finditer(obj, s):
            if cc == c:
                if debug:
                    print('doing ' + obj + ' on ' + str(cc))
                s = surroundOperation(s, m.start())
            cc += 1
        c += 1

    return s

def performEverything(s):
    sOrig = s
    s = s.replace('скобка открывается', '(')
    s = s.replace('скобка закрывается', ')')

    s = s.replace('плюс', '+')
    s = s.replace('минус', '-')
    s = s.replace('умножить на', '*')
    s = s.replace('разделить на', '/')

    s = surroundAll(s, r'\*')
    s = surroundAll(s, r'/')
    s = surroundAll(s, r'\+')
    s = surroundAll(s, r'-')

    # for m in re.finditer('/', s):
    #     s = surroundOperation(s, m.start())
    # for m in re.finditer('\+', s):
    #     s = surroundOperation(s, m.start())
    # for m in re.finditer('-', s):
    #     s = surroundOperation(s, m.start())

    # for m in re.finditer(numbersPattern, s):
    #     orig = m.group(2).strip()
    #     s = s.replace(orig, "( " + orig + " )", 1)
    if debug:
        print(s)
    return getOperation(s, sOrig)
    # return s, None

def getOperation(s, sOrig):
    # print('operation', s)
    s = s.strip()
    while s.startswith('(') and s.endswith(')'):
        s = s[1:len(s)-1].strip()
        # print(s)

    bc1 = s.count('(')
    bc2 = s.count(')')
    if bc1 > bc2:
        return None, 'Отсутствует закрывающая скобка: ' + sOrig
    if bc2 > bc1:
        return None, 'Лишняя открывающая скобка: ' + sOrig

    number, err = getNumber(s)
    # print('aaaaa', err)
    if not err:
        return number, err

    noBrackets = False
    bracketsContent = None
    bracketsContentNumber = None
    usualOrder = True
    m = re.fullmatch(patternLeftBrackets, s)
    if m:
        bracketsContent = m.group(2)
        bracketsContentNumber, err = getOperation(bracketsContent, sOrig)
        if err:
            return None, err
        operation = m.group(3)
        operand = m.group(4)
        number1, err = getNumber(operand)
        if err:
            return None, err

        t = number1
        number1 = bracketsContentNumber
        bracketsContentNumber = t
    else:
        m = re.fullmatch(patternRightBrackets, s)
        if m:
            bracketsContent = m.group(4)
            bracketsContentNumber, err = getOperation(bracketsContent, sOrig)
            if err:
                return None, err
            operation = m.group(2)
            operand = m.group(1)
            number1, err = getNumber(operand)
            if err:
                return None, err
        else:
            m = re.fullmatch(patternJustTwoNumbers, s)
            if m:
                operand = m.group(1)
                number1, err = getNumber(operand)
                if err:
                    return None, err

                operation = m.group(2)
                bracketsContentNumber, err = getNumber(m.group(3))
                if err:
                    return None, err
            else:
                return None, 'Некорретный формат операции: ' + s

    # print(s)
    # print(s.find('('))
    # print(s.rfind(')'))
    # print("'" + s[s.find('(')+1:s.rfind(')')].strip())
    #
    # print("'" + s[0 : s.find('(')].strip() + "'")
    # print("'" + s[s.rfind(')') + 1 : len(s)].strip() + "'")
    ## s[s.find('(') + 1:s.rfind(')')].strip()


    if debug:
        print(number1, operation, + bracketsContentNumber)


    if operation == '+':
        return number1 + bracketsContentNumber, None
    elif operation == '-':
        return number1 - bracketsContentNumber, None
    elif operation == '*':
        return number1 * bracketsContentNumber, None
    elif operation == '/':
        return round(number1 / bracketsContentNumber, 3), None
    elif operation == '^' or operation == '**':
        return number1 ** bracketsContentNumber, None
    else:
        return None, 'Неизвестная операция: ' + s

def _surroundLeft(s, start, agressive=False):
    bc1 = 0
    bc2 = 0
    b = False
    for i in reversed(range(0, start)):
        a = s[i]
        # print('found ' + a)
        if not a.isspace():
            if a == ')':
                bc1 += 1
            elif a == '(':
                bc2 += 1
                if bc1 == 0:
                    s = s[0: i + 1] + " (" + s[i + 1: len(s)]
                    b = True
                    return s, b, False
            if a in '+-*/' or a == '(':
                if bc1 == bc2:
                    s = s[0: i + 1] + " (" + s[i + 1: len(s)]
                    b = True
                    break
            else:
                if bc1 == bc2 and bc1 > 0:
                    s = s[0: i + 1] + " (" + s[i + 1: len(s)]
                    b = True
                    break
    if not b:
        s = '( ' + s
        b = True
    return s, b, False

def _surroundRight(s, start, agressive=False):
    bc1 = 0
    bc2 = 0
    b = False
    # print(s[start+2])
    for i in range(start + 3, len(s)):
        a = s[i]
        # print('found ' + a + " in '" + s[max(0, min(len(s), i - 5)) : max(0, min(len(s), i + 5))] + "'")
        if not a.isspace():
            if a == '(':
                bc1 += 1
            elif a == ')':
                bc2 += 1
                # print(bc1)
                if bc1 == 0:
                    # if agressive:
                        s = s[0: i] + ") " + s[i: len(s)]
                        b = True
                        return s, b, False
                    # else:
                    #     return s, b, True
            if a in '+-*/' or a == ')':
                if bc1 == bc2:
                    s = s[0: i] + ") " + s[i: len(s)]
                    b = True
                    break
            else:
                if bc1 == bc2 and bc1 > 0:
                    s = s[0: i] + ") " + s[i: len(s)]
                    b = True
                    break
    if not b: # and agressive
        s = s + ' )'
        b = True
    return s, b, False

def surroundOperation(s, start):
    if debug:
        print('orig: ', s)
    # print(s[start-5:start+5])
    s, b1, stop1 = _surroundLeft(s, start)
    if debug:
        print('left: ', s)
    if stop1:
        print('stop')
        return s
    s, b2, stop2 = _surroundRight(s, start)
    if debug:
        print('right:', s)

    if debug:
        print(b1, b2, stop1, stop2)
    if stop1 or stop2:
        return s
    # if b1 and not b2:
    #     s, ba2, stop1_2 = _surroundRight(s, start, agressive=True)
    #     print(s)
    # if b2 and not b1:
    #     s, ba1, stop2_2 = _surroundLeft(s, start, agressive=True)
    #     print(s)

    if debug:
        print()
    return s.strip()

# s = "два + сто * ( ( пять + два ) + четыре ) * три - один"

# counter = 0
# s = "два + ( ( сорок + ( три * один ) + два - девять ) * три - один - семь"
# for i in re.finditer('\*', s):
#     counter += 1
#     if counter == 2:
#         print(surroundOperation(s, i.start()))
#         break


# Примеры:
#
# скобка открывается пять плюс два скобка закрывается умножить на три минус один
# два плюс скобка открывается скобка открывается сорок плюс три скобка закрывается плюс два скобка закрывается умножить на три минус один
# два плюс (три + пять)

if __name__ == "__main__":
    s = 'два плюс скобка открывается скобка открывается сорок плюс три умножить на один скобка закрывается плюс два минус девять скобка закрывается умножить на три минус один минус семь'
    result, err = performEverything(s)
    if result:
        print('Результат:')
        print(reverseGetNumber(result))
    else:
        print(err)
