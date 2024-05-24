from base64 import b64decode
start = "https://wordle.belousov.one/word/?id=ru_"
print("Решатель слов Wordle")
while True:
    word = input("Введите ссылку на слово: ")
    if not word.startswith(start):
        print(f"Неверная ссылка на слово. Слово должно начинаться с: {start}")
    else:
        word = word.split(start)[1]
        word = b64decode(word.encode()).decode()
        print(f"Загаданное слово: {word}")