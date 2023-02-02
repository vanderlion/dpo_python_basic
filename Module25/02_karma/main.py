import random

class KillError(Exception):
    def __str__(self):
        return 'Строка с ошибкой'

class DrunkError(Exception):
    def __str__(self):
        return 'Строка с ошибкой'

class CarCrashError(Exception):
    def __str__(self):
        return 'Строка с ошибкой'

class GluttonyError(Exception):
    def __str__(self):
        return 'Строка с ошибкой'

class DepressionError(Exception):
    def __str__(self):
        return 'Строка с ошибкой'


def one_day():
    en_karma_level = 0

    with open('karma.log', 'w'):
        pass

    while en_karma_level < 500:
        dice = random.randint(1,10)
        with open('karma.log', 'a+', encoding='utf-8') as karma:
            try:
                if dice == 1:
                    en_karma_level += 1
                    raise KillError('KillError')
            except KillError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 2:
                    en_karma_level += 2
                    raise DrunkError('DrunkError')
            except DrunkError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 3:
                    en_karma_level += 3
                    raise CarCrashError('CarCrashError')
            except CarCrashError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 4:
                    en_karma_level += 4
                    raise GluttonyError('GluttonyError')
            except GluttonyError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            try:
                if dice == 5:
                    en_karma_level += 5
                    raise DepressionError('DepressionError')
            except DepressionError as exc:
                karma.write(f'Поймано исключение {exc}\n')
            else:
                if dice > 5:
                    en_karma_level += 6
                    karma.close()
    else:
        print('Просветление достигнуто')

one_day()