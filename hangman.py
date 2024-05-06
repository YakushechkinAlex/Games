from random import choice

hangman = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
| 
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  /
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  / \\
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  / \\
|  | 
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\ 
|   | 
|   | 
|  / \\
|  | | 
|
--------
"""
)

max_wrong = len(hangman) - 1  # Уменьшаем количество попыток на одну

# Чтение слов из файла
try:
    with open('russian.txt', 'r', encoding='cp1251') as f:
        words = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print("Файл 'words.txt' не найден. Используется стандартный список слов.")
    words = ('питон', 'игра', 'енот')  # Запасной список слов

word = choice(words)  # Случайный выбор слова
so_far = '_' * len(word)  # Состояние слова для отображения
wrong = 0  # Счетчик неверных попыток
used = []  # Список уже использованных букв

while wrong < max_wrong and so_far != word:
    print(hangman[wrong])
    print('\n Вы использовали следующие буквы:\n', used)
    print('\n На данный момент слово выглядит вот так:\n', so_far)

    guess = input('\nВведите своё предположение:').lower()

    while guess in used or len(guess) != 1 or not guess.isalpha():
        if guess in used:
            print('Вы уже ввели букву', guess)
        else:
            print('Пожалуйста, введите одну букву русского алфавита.')
        guess = input('Введите своё предположение:').lower()

    used.append(guess)

    if guess in word:
        print('Да,', guess, 'есть в слове!')
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('Данной буквы нет в слове:', guess)
        wrong += 1

if wrong == max_wrong:
    print('Вы проиграли')
    print(hangman[wrong])
else:
    print('Вы угадали слово!')

print('Загаданное слово было:', word)
