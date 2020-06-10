print('''
Введите номер метода, который использовался для встраивания слова 
в контейнер result.txt:
1 - метод прямой замены символов
2 - метод использования дополнительных пробелов
3 - метод добавления специальных символов
Извлеченное слово будет выведено в командную строку.
''')
method = str(input())
word = list()
# открываем файл и читаем посимвольно
fin = open('result.txt', 'r')
stroki = list(fin.read())
if method == '1':
    # формируем битовую последовательность
    for row in stroki:
        if row == 'o':
            word.append('0')
        elif row == 'e':
            word.append('1')
        elif row == 'a':
            word.append(' ')
elif method == '2':
    rowcnt = 0
    # формируем битовую последовательность
    for row in stroki:
        if row == '\n':
            if (stroki[rowcnt - 3] + stroki[rowcnt - 2] + stroki[rowcnt - 1]) == '   ':
                word.append(' ') 
            elif (stroki[rowcnt - 2] + stroki[rowcnt - 1]) == '  ':
                word.append('1')
            elif stroki[rowcnt- 1] == ' ':
                word.append('0')
        rowcnt += 1
elif method == '3':
    # формируем битовую последовательность
    for row in stroki:
        if row == '!':
            word.append('0')
        elif row == '?':
            word.append('1')
        elif row == '.':
            word.append(' ')
newstr = ''.join(word)
lst = newstr.split()
newlist = list()
# переводим бинарную последовательность в слово
for binary in lst:
    a = int(binary, 2)
    newlist.append(chr(a))
# выводим извлеченное слово
print(*newlist, sep='')
fin.close()
