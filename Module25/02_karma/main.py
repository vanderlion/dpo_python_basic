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


def one_day(count):
    day_karma = random.randint(1, 7)
    if random.randint(1, 10) == 1:
        with open('karma.log', 'w') as karma_log:
            exception = random.choice([KillError(), DrunkError(), CarCrashError(), GluttonyError(), DepressionError()])
            karma_log.write(f'день {count}: {exception}\n')
            raise exception
    return day_karma

karma = 0
day = 0
while karma < 500:
    day += 1
    if one_day(day):
        pass
    else:
        print("Просветление достигнуто")