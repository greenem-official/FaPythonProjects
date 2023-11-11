# Доп. задание 1 (сложность 2), имеет частичный функционал задания 2 (сложность 3)

import re

patternOperation = r'(.*)\s(плюс|минус|умножить\sна|разделить\sна)\s(.*)'
patternNumberFullFraction = r'((.+?)\sсот(ая|ые|ых))?(\s?(.+?)\sтысячн(ая|ые|ых))?(\s?(.+?)\sмиллионн(ая|ые|ых))?'

debug = False

def getNumHundreds(raw):
    if not raw:
        return 0
    raw = raw.strip()

    if raw == 'сто':
        return 100
    elif raw == 'двести':
        return 200
    elif raw == 'триста':
        return 300
    elif raw == 'четыреста':
        return 400
    elif raw == 'пятьсот':
        return 500
    elif raw == 'шестьсот':
        return 600
    elif raw == 'семьсот':
        return 700
    elif raw == 'восемьсот':
        return 800
    elif raw == 'девятьсот':
        return 900

    print('Неверный формат сотен: "' + raw + '"')
    return None


def getNumTens(raw):
    if not raw:
        return 0
    raw = raw.strip()

    if raw == 'двадцать':
        return 20
    elif raw == 'тридцать':
        return 30
    elif raw == 'сорок':
        return 40
    elif raw == 'пятьдесят':
        return 50
    elif raw == 'шестьдесят':
        return 60
    elif raw == 'семьдесят':
        return 70
    elif raw == 'восемьдесят':
        return 80
    elif raw == 'девяносто':
        return 90

    print('Неверный формат десятков: "' + raw + '"')
    return None


def getNumOnes(raw):
    if not raw:
        return 0
    raw = raw.strip()

    if raw == 'один' or raw == 'одна':
        return 1
    elif raw == 'два' or raw == 'две':
        return 2
    elif raw == 'три':
        return 3
    elif raw == 'четыре':
        return 4
    elif raw == 'пять':
        return 5
    elif raw == 'шесть':
        return 6
    elif raw == 'семь':
        return 7
    elif raw == 'восемь':
        return 8
    elif raw == 'девять':
        return 9
    elif raw == 'десять':
        return 10
    elif raw == 'одиннадцать':
        return 11
    elif raw == 'двенадцать':
        return 12
    elif raw == 'тринадцать':
        return 13
    elif raw == 'четырнадцать':
        return 14
    elif raw == 'пятнадцать':
        return 15
    elif raw == 'шестнадцать':
        return 16
    elif raw == 'семнадцать':
        return 17
    elif raw == 'восемнадцать':
        return 18
    elif raw == 'девятнадцать':
        return 19

    print('Неверный формат единиц: "' + raw + '"')
    return None


def getBasicNumber(s):
    hundreds = 0
    tens = 0
    ones = 0

    p = s.split()
    if len(p) == 0:
        print('Встречено "пустое" число!')
        return None
    if len(p) >= 1:
        ones = getNumOnes(p[len(p) - 1])
        if not ones:
            return None
    if len(p) >= 2:
        tens = getNumTens(p[len(p) - 2])
        if not tens:
            return None
    if len(p) >= 3:
        hundreds = getNumHundreds(p[len(p) - 3])
        if not hundreds:
            return None

    return hundreds + tens + ones


def getNumPartWhole(s):
    p1 = getBasicNumber(s)
    if not p1:
        print('Неверное целое число: "' + s + '"')
        return None

    if debug:
        print('Целая часть |', p1)
    return p1


def getNumPartFraction(s):
    m = re.fullmatch(patternNumberFullFraction, s)
    if m:
        hundredths = 0
        thousandths = 0
        millionths = 0

        hundredthsRaw = m.group(2)
        thousandthsRaw = m.group(5)
        millionthsRaw = m.group(8)

        # print(hundredthsRaw, thousandthsRaw, millionthsRaw)

        if hundredthsRaw:
            if thousandthsRaw or millionthsRaw:
                print('Нельзя задавать дробь с сотыми, тысячными и миллионными вместе: "' + s + '"')
                return None
            hundredths = getBasicNumber(hundredthsRaw)
        if thousandthsRaw:
            if hundredthsRaw or millionthsRaw:
                print('Нельзя задавать дробь с сотыми, тысячными и миллионными вместе: "' + s + '"')
                return None
            thousandths = getBasicNumber(thousandthsRaw)
        if millionthsRaw:
            if hundredthsRaw or thousandthsRaw:
                print('Нельзя задавать дробь с сотыми, тысячными и миллионными вместе: "' + s + '"')
                return None
            millionths = getBasicNumber(millionthsRaw)

        result = hundredths / 100 + thousandths / 1000 + millionths / 1000000
        if debug:
            print('Дробь |', hundredths, 'сотых,', thousandths, 'тысячных,', millionths, 'миллионных, результат:',
                  result)
        return result
    else:
        print('Неверная дробь: "' + s + '"')
        return None


def getNumber(s):
    # maybeOperation = getOperation(s)
    # if maybeOperation:
    #     return maybeOperation

    p = s.split(' и ')

    if len(p) == 0:
        print('Неверный формат числа: "' + s + '"')
        return None
    if len(p) == 1:
        if 'сотых' in p[0] or 'сотые' in p[0] or 'сотая' in p[0] or 'тысячных' in p[0] or 'тысячные' in p[
            0] or 'тысячная' in p[0] or 'миллионных' in p[0] or 'миллионные' in p[0] or 'миллионная' in p[0]:
            return getNumPartFraction(p[0])
        else:
            return getNumPartWhole(p[0])
    elif len(p) == 2:
        p1 = getNumPartWhole(p[0])
        p2 = getNumPartFraction(p[1])
        if p1 and p2:
            return p1 + p2
        else:
            return None
    else:
        print('Неверный формат числа: "' + s + '" (встречено более одного "и", требуется писать с одним)')
        return None


def reverseGetNumber(n):
    if n == 0:
        return 'ноль'

    fr = n - int(n)
    s = ''
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

    if fr == 0:
        return s
    frOrig = fr

    fr *= 100
    if int(fr) != 0 and int(fr) * 10 == int(frOrig * 1000):
        s += ' и' + reverseGetNumber(int(fr)).strip() + ' сот'
        a = int(fr)
        if a % 10 == 1:
            s += 'ая'
        if 2 <= a % 10 <= 4:
            s += 'ые'
        else:
            s += 'ых'
        return s

    fr = frOrig
    fr *= 1000
    if int(fr) != 0:
        s += 'и ' + reverseGetNumber(int(fr)).strip() + ' тысячн'
        a = int(fr)
        if a % 10 == 1:
            s += 'ая'
        if 2 <= a % 10 <= 4:
            s += 'ые'
        else:
            s += 'ых'
        return s

    return s
def getOperation(s):
    m = re.fullmatch(patternOperation, s)
    if not m:
        return None
    num1 = getNumber(m.group(1))
    num2 = getNumber(m.group(3))
    if not num1 or not num2:
        return None
    operation = m.group(2)
    if operation == 'плюс':
        return num1 + num2
    elif operation == 'минус':
        return num1 - num2
    elif operation == 'умножить на':
        return num1 * num2
    elif operation == 'разделить на':
        return round(num1 / num2, 3)
    else:
        print('Неизвестная операция: "' + operation + '"')
        return None


s = 'сорок один и тридцать одна сотая разделить на двести сорок семь миллионных'
result = getOperation(s)
if not result:
    print('Неверный формат операций: "' + s + '"')
else:
    print('Результат:', reverseGetNumber(result))
