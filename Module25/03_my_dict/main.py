class MyDict(dict):
     def get(self, key, default=0):
        return super().get(key, default)

new_dict = MyDict()
new_dict['Ikari'] = 1
new_dict['Asuka'] = 2
new_dict['Rei'] = 3
print(new_dict)
print(new_dict.get('Misato'))