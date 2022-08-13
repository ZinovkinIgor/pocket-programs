class UserInfo:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.city = args[2]
        self.season = args[3]
        self.favorit_color = args[4]
        self.favorit_fruit = args[5]

    def generator_travel(self):
        print(f'{self.name} решил путешествовать в свои {self.age} года. Он выехал из города {self.city}. '
              f'На улице была отличная погода, ведь идет{self.season}. Завел свой {self.favorit_color} автомобиль и поехал на море. '
              f'Заехал в магазин чтобы купить {self.favorit_fruit} и отправится в хорошую дорогу.')

    def generator_bussines(self):
        print(f'{self.name} в свои {self.age}. Решил открыть в городе {self.city} магазин с фруктами. '
              f'Сейчас отличное время для бизнеса {self.season}. Магазин окрасил в {self.favorit_color} цвет.'
              f'Повесил большую вывеску в виде {self.favorit_fruit}.')

def choise():
    ansver = input('Выберите что будем читать. 1 - путешествие, 2 - бизнес-план: ')
    return ansver

def data_input():
    name = input('Введите ваше имя: ')
    age = input('Введите ваш возраст: ')
    city = input('Введите ваш город: ')
    season = input('Введите время года: ')
    favorit_color = input('Введите любимый цвет: ')
    favorit_fruit = input('Введите любимый фрукт: ')
    return [name, age, city, season, favorit_color, favorit_fruit]



data = data_input()
numb = choise()
madlibs = UserInfo(data[0], data[1], data[2], data[3], data[4], data[5])
if numb == '1':
    madlibs.generator_travel()
elif numb == '2':
    madlibs.generator_bussines()
else:
    print('Введите корректные данные.')
    numb = choise()