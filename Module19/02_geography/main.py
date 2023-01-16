catalog = dict()
number_countries = int(input('Количество стран: '))
for i_countries in range(number_countries):
    country_info = input('{0} страна : '.format(i_countries + 1)).title().split()
    country, cityes = country_info[0], country_info[1:]
for city in cityes:
    catalog[city] = country
print('\n')
for i_city in range(3):
    desired_city = input('{0} город: '.format(i_city + 1)).capitalize()
    if desired_city in catalog.keys():
        print('Город {0} расположен в стране {1}.'.format(desired_city, catalog[desired_city]))
    else:
        print('По городу {} данных нет.'.format(desired_city))