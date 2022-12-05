import random

class Car:
    """
    Класс автомобиль:
    args:
        direction_of_movement - словарь, направление движения
        __x - точка х
        __y - точка у
        direction - куда направлена машина.
    """
    direction_of_movement = {1: 'Вперед', 2: 'Назад', 3: 'Вверх', 4: 'Вниз'}

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.direction = 1

    def choice_movement(self, numb_direction, lengt):
        """Выбор направления движения"""
        if numb_direction == 1:
            self.movement(numb_direction, self.__x, lengt, '+')
            self.set_coordinate(numb_direction=numb_direction, lengt=lengt)
        elif numb_direction == 2:
            self.movement(numb_direction, self.__x, lengt, '-')
            self.set_coordinate(numb_direction=numb_direction, lengt=lengt)
        elif numb_direction == 3:
            self.movement(numb_direction, self.__y, lengt, '+')
            self.set_coordinate(numb_direction=numb_direction, lengt=lengt)
        elif numb_direction == 4:
            self.movement(numb_direction, self.__y, lengt, '-')
            self.set_coordinate(numb_direction=numb_direction, lengt=lengt)
        else:
            print('Введено некорректное направление.')

    def movement(self, numb_direction, direction, lengt, action):
        """Движение"""
        if action == '+':
            direction += lengt
            print('Проезжаем {dir} на {lengt} км'.format(
                dir=self.direction_of_movement[numb_direction], lengt=lengt)
            )
        elif action == '-':
            direction -= lengt
            print('Проезжаем {dir} на {lengt} км'.format(
                dir=self.direction_of_movement[numb_direction], lengt=lengt)
            )
        else:
            print('Ошибка! Ввод должен быть - или +')

    def route(self):
        """
        Маршрут
        args:
            turn - количество поворотов
            numb_direction - номер направления движения
            lengt - пройденный путь
            way - пройденный путь (км)

        """
        print('Двигатель заведен. Мы начинаем движение с координат x={}, y={}'.format(self.__x, self.__y))
        turn = random.randint(1, 5)
        way = 0
        for turn_n in range(1, turn + 1):
            print('{}-поворот.'.format(turn_n))
            numb_direction = random.randint(1, 4)
            lengt = random.randint(1, 15)
            self.choice_movement(numb_direction=numb_direction, lengt=lengt)
            way += lengt
        print('Мы приехали {way} км и {turn} поворотов.\nДвигатель остановлен.\n\n'.format(way=way, turn=turn))

    def set_coordinate(self, numb_direction, lengt):
        """Сохраняем координаты при остановке"""
        if numb_direction == 1:
            self.__x += lengt
        elif numb_direction == 2:
            self.__x -= lengt
        elif numb_direction == 3:
            self.__y += lengt
        elif numb_direction == 4:
            self.__y -= lengt


class Bus(Car):
    """
    Класс автобус:
        passenger - количество поссажиров = 0
        max_passenger - максимальное количество поссажиров
        money - количество денег = 0
        price -  стоимость проезда
        count_passenger - сколько перевезено пассажиров.
    method:
        - вошло в автобус
        - вышло из автобуса
        - количество денег.
    """
    def __init__(self):
        super().__init__()
        self.__x = 0
        self.__y = 0
        self.passenger = 0
        self.__max_passenger = 40
        self.count_passenger = 0
        self.money = 0
        self.price = 50

    def entered(self):
        """
        Посадка пассажиров
        passenger - рандомное количество пассажиров
        available_seats - свободные места
        no_passenger - остались на остановке
        """

        passenger = random.randint(0, 10)
        if self.__max_passenger > self.passenger:
            available_seats = self.__max_passenger - self.passenger
            if available_seats > passenger:
                self.passenger += passenger
                self.payment_travel(passenger)
                print('На остановке зашло {passenger} пассажиров, в автобусе стало {total_pass} пассажиров.'.format(
                passenger=passenger, total_pass=self.passenger))
            else:
                no_passenger = passenger - available_seats
                self.passenger += passenger - no_passenger
                self.payment_travel(passenger - no_passenger)
                print('На остановке зашло {passenger} пассажиров, в автобусе стало {total_pass} пассажиров.\n'
                      'На остановке осталось ждать следующий автобус {no_pass} пассажиров'.format(
                    passenger=passenger, total_pass=self.passenger, no_pass=no_passenger))
        else:
            print('Автобус полный. Посадка невозможна.')

    def disembarkation(self):
        """
        Высадка пассажиров
        passenger - пассажиров вышло на остановке.
        """
        if self.passenger > 0:
            passenger = random.randint(0, self.passenger + 1)
            self.passenger -= passenger
            print('На остановке вышло {passenger} пассажиров, в автобусе осталось {total_pass} пассажиров.'.format(
                    passenger=passenger, total_pass=self.passenger))
        else:
            print('Автобус пустой.')

    def payment_travel(self, passenger):
        """
        Оплата проезда  и подсчет пассажиров
        """
        self.money += passenger * self.price
        self.count_passenger += passenger

    def route(self):

        self.type_action_travel = {1: 'Посадка', 2: 'Высадка', 3: 'Посадка, Высадка'}
        """
        Маршрут
        args:
            turn - количество остановок
            numb_direction - номер направления движения
            lengt - пройденный путь
            way - пройденный путь (км)

        """
        print('Двигатель заведен. Мы начинаем движение с координат x={}, y={}'.format(self.__x, self.__y))
        turn = random.randint(1, 25)
        way = 0
        for turn_n in range(1, turn + 1):
            action_travel = random.randint(1, 3)
            if action_travel == 1:
                print('Автобус остановился выходить никто не будет. Будет {}'.format(self.type_action_travel[action_travel]))
                self.entered()
            elif action_travel == 2:
                print('Автобус остановился на остановке никого нет. Будет {}'.format(self.type_action_travel[action_travel]))
                self.disembarkation()
            elif action_travel == 3:
                print('Автобус остановился. Будет {}'.format(self.type_action_travel[action_travel]))
                self.disembarkation()
                self.entered()
            print('{}-остановка.'.format(turn_n))
            numb_direction = random.randint(1, 4)
            lengt = random.randint(1, 15)
            self.choice_movement(numb_direction=numb_direction, lengt=lengt)
            way += lengt
        print('Мы приехали {way} км и {turn} остановок, перевезли {count} пассажиров и заработали {money} рублей. '
              '\nДвигатель остановлен.\n\n'.format(way=way, turn=turn, count=self.count_passenger, money=self.money))


my_car = Car()
my_car.route()
my_bus = Bus()
my_bus.route()
