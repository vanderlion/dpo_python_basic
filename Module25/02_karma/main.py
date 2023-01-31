import random


class Buddhist:
    def __init__(self, karma=0):
        self.__karma = karma

    def get_karma(self):
        return self.__karma

    def set_karma(self, enlightenment_closer):
        self.__karma += enlightenment_closer


def one_day(count):
    if random.randint(1, 10) == 1:
        with open('karma.log', 'a', encoding='utf-8') as karma_log:
            misconduct = random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
            karma_log.write(f'день {count}: проступок - {misconduct}\n')
            return False
    else:
        return random.randint(1, 7)


buddhist = Buddhist()
day = 0
while buddhist.get_karma() < 500:
    day += 1
    if one_day(day):
        pass
    else:
        buddhist.set_karma(one_day(day))
print(('Просветление достигнуто'))