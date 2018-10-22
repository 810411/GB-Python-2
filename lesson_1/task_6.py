# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

import locale
import chardet

print(locale.getpreferredencoding())

# cp1251

with open('test_file.txt', 'rb') as fl:
    s = fl.read()
    print(s)
    print(chardet.detect(s))

# b'\xf1\xe5\xf2\xe5\xe2\xee\xe5 \xef\xf0\xee\xe3\xf0\xe0\xec\xec\xe8\xf0\xee\xe2\xe0\xed\xe8\xe5\r\n\xf1\xee\xea\xe5
# \xf2\r\n\xe4\xe5\xea\xee\xf0\xe0\xf2\xee\xf0'
# {'encoding': 'windows-1251', 'confidence': 0.9929305516756276, 'language': 'Russian'}

with open('test_file.txt', encoding='utf-8', errors='replace') as fl:
    print(fl.read())

# ������� ����������������
# �����
# ���������
