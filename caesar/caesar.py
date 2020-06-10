lower_alphabet = list('abcdefghijklmnopqrstuvwxyz')
upper_alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
ln = len(lower_alphabet)
print('''Choose mode:
1. Encode (зашифровать)
2. Decode (расшифровать)''')
mode = int(input())
print('Enter key:')
key = int(input())
if mode == 1: 
    moded = 'encode'
    key = key - (key * 2)
elif mode == 2:
    moded = 'decode'
print(f'Enter text to {moded}:')
text = list(input())
out = []
for i in text:
    if i in lower_alphabet:
        index = lower_alphabet.index(i)
        enter = (index + key) % ln
        out.append(lower_alphabet[enter])
    elif i in upper_alphabet:
        index = upper_alphabet.index(i)
        enter = (index + key) % ln
        out.append(upper_alphabet[enter])
    else:
        out.append(i)
print(f'''Your text {moded}d:
''',*out, sep='')
