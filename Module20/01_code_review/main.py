students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def foo(d: dict) -> tuple:
    return set(sum([d[i]['interests'] for i in d], [])), sum(map(len, [d[i]['surname'] for i in d]))

interests, total_len = foo(students)
print(', '.join(interests))
print(total_len)
