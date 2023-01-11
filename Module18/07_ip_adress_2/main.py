from string import punctuation
from string import whitespace
def check_IP(s):
    p = set(s) & set(punctuation) - set('-')
    if p != set('.'):
        return 'Адрес — это числа, разделенные точками.'
    lis = s.split('.')
    lis_n = []
    for e in lis:
        try:
            lis_n.append( int(e) )
        except:
            if e in whitespace:
                return f'Пробельный символ - это не целое число.'
            return f'{e} - это не целое число.'
    if len( lis_n ) != 4:
        return f'Здесь чисел { len( lis_n ) }, а должно быть четыре.'
    for n in lis_n:
        if n < 0:
            return f'{n} меньше нуля.'
        if n > 255:
            return f'{n} превышает 255.'
    return 'IP-адрес корректен.'

s = input('Введите IP: ')
print( check_IP(s) )