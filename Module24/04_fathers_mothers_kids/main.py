class Child:
    calm_states = {0: 'спокоен ', 1: 'плачет '}
    hungry_states = {0: 'накормлен ', 1: 'голоден '}

    def __init__(self, child_name, child_age):
        self.name = child_name
        self.age = child_age
        self.calm_state = 0
        self.hungry_state = 0

    def child_info(self):
        if self.age == 1:
            print(f'Ребенку {self.name} {self.age} год')
        elif self.age == 2 or self.age == 3:
            print(f'Ребенку {self.name} {self.age} года')
        else:
            print(f'Ребенку {self.name} {self.age} лет')

    def print_state(self):
        print('Ребенок {} сейчас {}'.format(self.name, Child.calm_states[self.calm_state]))
        print('Ребенок {} сейчас {}'.format(self.name, Child.hungry_states[self.hungry_state]))


class Parent:

    def __init__(self, parent_name, parent_age, children, children_count):
        self.name = parent_name
        self.age = parent_age
        self.children = []
        self.children_count = 0

    def parent_info(self):
        if (self.age % 10) == 1:
            print(f'Меня зовут {self.name}, мне {self.age} год, у меня {self.children_count} детей:')
        elif (self.age % 10) == 2 or (self.age % 10) == 3:
            print(f'Меня зовут {self.name}, мне {self.age} года, у меня {self.children_count} детей:')
        else:
            print(f'Меня зовут {self.name}, мне {self.age} лет, у меня {self.children_count} детей:')
        for i_child in self.children:
            i_child.child_info()
        print()

    def soothe_the_child(self, child):
        if child.calm_state == 1:
            print(f'Папа {self.name} спешит утешить {child.name}! ')
            child.calm_state = 0
        else:
            print(f'Папа {self.name} рад, что {child.name} спокоен! ')

    def feed_the_child(self, child):
        if child.hungry_state == 1:
            print(f'Папа {self.name} спешит накормить {child.name}! ')
            child.hungry_state = 0
        else:
            print(f'Папа {self.name} рад, что {child.name} накормлен! ')


import random

parentName = input('Как зовут родителя? ')
parentAge = int(input(f'Сколько {parentName} лет? '))
parent = Parent(parentName, parentAge, children=[], children_count=0)

child_1Name = input('Как зовут ребенка? ')
child_1Age = int(input(f'Сколько {child_1Name} лет? '))
child_1 = Child(child_1Name, child_1Age)
parent.children.append(child_1)
parent.children_count += 1

child_2Name = input('Как зовут ребенка? ')
child_2Age = int(input(f'Сколько {child_2Name} лет? '))
child_2 = Child(child_2Name, child_2Age)
parent.children.append(child_2)
parent.children_count += 1

parent.parent_info()

for i_child in parent.children:
    i_child.calm_state = random.randint(0, 1)
    i_child.hungry_state = random.randint(0, 1)
    i_child.print_state()
    parent.soothe_the_child(i_child)
    parent.feed_the_child(i_child)