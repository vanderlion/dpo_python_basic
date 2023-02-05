def how_are_you(func):
    def wrapper():
        print("Как твои дела? Хорошо")
        func()
        print("А у меня не очень. Ладно держи свою функцию")

    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()