class MyDict(dict):
    def __init__(self, *args, **kw):
        super(MyDict, self).__init__(*args, **kw)

    def __get__(self, instance, owner):
        return 0

new_dict = MyDict()
new_dict['Ikari'] = 1
new_dict['Asuka'] = 2
new_dict['Rei'] = 3
print(new_dict)
print(new_dict.get('Misato'))