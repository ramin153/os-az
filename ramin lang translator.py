dictt = {'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع', 'i': 'ه', 'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'چ',
         'a': 'ش', 's': 'س', 'd': 'ی', 'f': 'ب', 'g': 'ل', 'h': 'ا', 'j': 'ت', 'k': 'ن', 'l': 'م', ';': 'ک', "'": 'گ',
         'z': 'ظ', 'x': 'ط', 'c': 'ز', 'v': 'ر', 'b': 'ذ', 'n': 'د', 'm': 'ئ', ',': 'و', '.': '.', '/': '/',
         '\\': 'پ', ' ': ' '}

if input('code/decode?! ') == 'code':
    for i in input('text:\n'):
        print(list(dictt.keys())[list(dictt.values()).index(i)], end='')
else:
    for i in input('text:\n').lower():
        if i in dictt:
            print(dictt[i], end='')
        else:
            print(i, end='')