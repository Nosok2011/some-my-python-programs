from random import shuffle
from pyperclip import copy
chars = " ".join("1234567890qwertyuiop[]asdfghjlzxcvbnm,.!$^)(QWERTYUIOP}{SDFGHJKL:ZXCVBNM><").split()
shuffle(chars)
lng = int(input("длина пароля: "))
pswd = "".join(chars[:lng])
print("ваш пароль", pswd)
copy(pswd)
print("пароль скопирован")
input()