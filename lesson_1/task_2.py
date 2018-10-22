# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
import binascii

strs = [b'class', b'function', b'method']

for s in strs:
    print(type(s), binascii.hexlify(s), len(s))
