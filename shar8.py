from random import choice
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError
from time import sleep
v = [ # варианты ответа брал с википедии https://ru.wikipedia.org/wiki/Magic_8_ball
    # ----- Положительные -----
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определённо да",
    "Можешь быть уверен в этом",
    # ----- Нерешительно положительные -----
    "Мне кажется - да",
    "Вероятнее всего",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    # ----- Нейтральные -----
    "Пока не ясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    # ----- Отрицательные -----
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно"
]
def end():
    input("Нажмите Enter, чтобы выйти.")
    exit()
r = Recognizer()
m = Microphone(1)
print("Говорите...")
with m:
    audio = r.listen(m)
try:
    recognized = r.recognize_google(audio, language="ru-RU")
    print("Распознано: %s" % recognized)
except UnknownValueError:
    print("Говорите чётче, пожалуйста")
    end()
except RequestError:
    print("Произошла ошибка распознавания, проверьте подключение к интернету")
    end()
finally:
    sleep(1)
print("Шар думает...")
sleep(3)
print(choice(v))
sleep(0.5)
end()