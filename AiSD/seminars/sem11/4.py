# to_numbers numbers.txt
# to_words numbers.txt

import calc_local as c
import calc3 as calc_other
import sys

def processFile(fileName, wordsOnOutput):
    l = []
    try:
        f = open(fileName, "r")
        for line in f.readlines():
            result, err = c.getOperation(line)
            print(result, err)
            if not err:
                if wordsOnOutput:
                    l.append(c.reverseGetNumber(result))
                else:
                    l.append(result)
            else:
                result, err = calc_other.performEverything(line)
                print(result, err)
                if result:
                    if wordsOnOutput:
                        l.append(c.reverseGetNumber(result))
                    else:
                        l.append(result)
        f.close()
        return l, None
    except FileNotFoundError:
        return None, 'Файл "' + fileName + '" не найден!'

if len(sys.argv) != 3:
    print('Введите название операции и название файла!')
else:
    mode = sys.argv[1]
    file = sys.argv[2]
    result = None
    err = None
    if mode == 'to_numbers':
        result, err = processFile(file, False)
    elif mode == 'to_words':
        result, err = processFile(file, True)
    else:
        print('Допустимая операция')

    if err:
        print(err)
    elif result:
        for a in result:
            print(a)