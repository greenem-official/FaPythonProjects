# 100 revisor.txt

import sys

def getStats(fileName):
    d = {}
    try:
        f = open(fileName, "r")
        for line in f.readlines():
            for word in line.split():
                if word in d.keys():
                    d[word] += 1
                else:
                    d[word] = 1
        f.close()
        d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        return d, None
    except FileNotFoundError:
        return None, 'Файл "' + fileName + '" не найден!'

if len(sys.argv) != 3:
    print('Введите колличество выводимых слов и название файла')
else:
    try:
        amount = int(sys.argv[1])
        d, err = getStats(sys.argv[2])
        if err:
            print(err)
        else:
            c = 0
            for k, v in d:
                print(k + ': ' + str(v))
                c += 1
                if c == amount:
                    break
    except ValueError:
        print('Первый аргумент должен быть числом (выводимых слов)!')