from random import *

def generate():
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    num = 0
    for i in range(4):
        d = digits[randint(0, len(digits)-1)]
        num = num * 10 + d
        digits.remove(d)
    return num

def addZeros(num):
    if num < 10:
        return "000" + str(num)
    if num < 100:
        return "00" + str(num)
    if num < 1000:
        return "0" + str(num)
    return str(num)

def process(cor, inp):
    partially = 0
    fully = 0
    for i in range(len(inp)):
        if inp[i] == cor[i]:
            fully += 1
        if inp[i] in cor:
            partially += 1
    return partially, fully

if __name__ == '__main__':
    num = generate()
    # print(addZeros(num))
    while True:
        inp = input('Введите предполагаемое число: ')
        if not inp.isdigit():
            print("Ввод должен быть числом!")
            continue
        if int(inp) < 0 or int(inp) > 9999:
            print("Ввод должен быть в диапазоне 0000-9999!")
            continue
        partially, fully = process(addZeros(num), addZeros(int(inp)))
        if fully == 4:
            print("Вы угадали число!")
            break
        print(partially, 'коров,', fully, 'быков')