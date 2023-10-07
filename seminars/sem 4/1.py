s1 = input('Введите первую строку: ')
s2 = input('Введите вторую строку: ')
both = ""
for i in range(len(s1)):
    if s1[i] == s2[i]:
        both += s1[i]
print("Строка из общих символов:", both)
