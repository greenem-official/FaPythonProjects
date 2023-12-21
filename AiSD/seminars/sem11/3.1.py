import sys

s = 0
try:
    for i in range(1, len(sys.argv)):
        num = int(sys.argv[i])
        s += num
    print(s)
except ValueError:
    print('Передано не число')
