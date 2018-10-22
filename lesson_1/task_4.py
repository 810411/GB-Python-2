# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
# и выполнить обратное преобразование (используя методы encode и decode).
import chardet

strs = ['разработка', 'сокет', 'декоратор']
strs_in_bytes = []

for s in strs:
    s = s.encode('utf-8', errors='namereplace')
    strs_in_bytes.append(s)
    print(s)

for s in strs_in_bytes:
    print(s.decode('ascii', errors='replace'))
    print(s.decode(chardet.detect(s)['encoding']))
