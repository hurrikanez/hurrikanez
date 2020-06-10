print('''
Для встраивания слова в стегоконтейнер введите:
1 - для метода прямой замены символов
2 - для метода использования дополнительных пробелов
3 - для добавления специальных символов
После этого введите слово для встраивания.
Результат работы будет выведен в result.txt
''')
method = str(input())
word = str(input())
# перевод принятой буквенной строки в битовый список
binword = ' '.join(format(ord(x), 'b') for x in word)
binary = list(binword)
# открываем файлы и читаем посимвольно из контейнера
fin = open('container.txt', 'r')
fout = open('result.txt', 'w+')
stroki = list(fin.read())
if method == '1':
    oldlist = list()
    newlist = list()
    bitcnt = 0
    binlen = len(binary)
    # заменяем необходимые буквы латиницы на русские
    # для избежания ошибок из-за вставок французских или английских отрывков
    for row in stroki:
        if row == 'a':
            oldlist.append('а')
        elif row == 'o':
            oldlist.append('о')
        elif row == 'e':
            oldlist.append('е')
        else:
            oldlist.append(row)
    # формируем итоговый текст на основе замены символов
    for row in oldlist:
        if bitcnt == binlen:
            newlist.append(row)
        elif binary[bitcnt] == '0' and row == 'о' and bitcnt < binlen:
            newlist.append('o')
            bitcnt += 1
        elif binary[bitcnt] == '1' and row == 'е' and bitcnt < binlen:
            newlist.append('e')
            bitcnt += 1
        elif binary[bitcnt] == ' ' and row == 'а' and bitcnt < binlen:
            newlist.append('a')
            bitcnt += 1
        else:
            newlist.append(row)
elif method == '2':
    newlist = list()
    bitcnt = 0
    rowcnt = 0
    binlen = len(binary)
    rowlen = len(stroki)
    # вставляем пробелы и формируем итоговый текст
    for row in stroki:
        if bitcnt == binlen or rowlen == rowcnt or rowlen == (rowcnt + 1):
            newlist.append(row)
        elif binary[bitcnt] == '0' and row == '\n' and bitcnt < binlen:
            newlist.append(' ')
            newlist.append('\n')
            bitcnt += 1
        elif binary[bitcnt] == '1' and row == '\n' and bitcnt < binlen:
            newlist.append('  ')
            newlist.append('\n')
            bitcnt += 1
        elif binary[bitcnt] == ' ' and row == '\n' and bitcnt < binlen:
            newlist.append('   ')
            newlist.append('\n')
            bitcnt += 1
        else:
            newlist.append(row)
        rowcnt += 1
elif method == '3':
    oldlist = list()
    newlist = list()
    bitcnt = 0
    binlen = len(binary)
    # заменяем все нужные символы для избежания ошибок при вытаскивании слова
    for row in stroki:
        if row == '!' or row == '?' or row == '.':
            oldlist.append('…')
        else:
            oldlist.append(row)
    # заменяем символы для формирования итогового текста
    for row in oldlist:
        if bitcnt == binlen:
            newlist.append(row)
        elif binary[bitcnt] == '0' and row == '…' and bitcnt < binlen:
            newlist.append('!')
            bitcnt += 1
        elif binary[bitcnt] == '1' and row == '…' and bitcnt < binlen:
            newlist.append('?')
            bitcnt += 1
        elif binary[bitcnt] == ' ' and row == '…' and bitcnt < binlen:
            newlist.append('.')
            bitcnt += 1
        else:
            newlist.append(row)
# Вывод текста в файл
outtext = ''.join(newlist)
fout.write(outtext)
fin.close()
fout.close()
