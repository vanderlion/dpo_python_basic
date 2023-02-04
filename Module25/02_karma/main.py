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
    day_karma = random.randint(1, 7)

    if random.randint(1, 10) == 5:
        exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
        raise exception

    return day_karma

karma = 0
with open('karma.log', 'w', encoding='utf-8') as file:
    while karma < 500:
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
            file.write(f'Поймано исключение {error}\n')
        else:
            print("Просветление достигнуто")