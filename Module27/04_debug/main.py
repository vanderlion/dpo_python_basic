def debug(func):
    def wrapper(name, age=None):
        print(func.__name__, name, age)
        return func(name, age)
    return wrapper


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


print(greeting("Том"))
print(greeting("Миша", age=100))
print(greeting(name="Катя", age=16))
