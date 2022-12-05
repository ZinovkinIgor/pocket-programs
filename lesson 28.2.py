"""
Задача 1. Снова роботы
На военную базу привезли очередную партию роботов. И в этот раз не абы каких, а летающих:
разведывательного дрона и военного робота.

Разведывательный дрон просто летает в поиске противника. При команде operate он выводит сообщение
«Веду разведку с воздуха» и передвигается немного вперёд.

У летающего военного робота есть оружие, и при команде operate он выводит сообщение о защите военного
объекта с воздуха с помощью этого оружия.

Напишите программу, которая реализует все необходимые классы роботов. Сущности «Робот» и
«Может летать» должны быть вынесены в отдельные классы. Обычный робот имеет модель и может вывести сообщение
«Я — Робот». Объект, который умеет летать, дополнительно имеет атрибуты «Высота» и «Скорость»,
а также может взлетать, летать и приземляться.
"""
import time


class Flight:
    """
    Класс полета
    Атрибуты:
        speed - скорость
        hight - высота
    Методы:
        включение двигателя, отключение двигателя
        набор скорости
        снижение скорости
        взлет
        приземление
        набор высоты
        снижение
    """

    def __init__(self):
        self.hight = 0
        self.speed = 0

    def start_engine(self):
        """Метод полной работы самолета"""
        print('Запущен двигатель.')
        self.takeoff()
        while True:
            ansver = int(input('Выберите действие: 1 - производим действие, 2 - летим на базу: '))
            if ansver == 1:
                self.operate()
            elif ansver == 2:
                self.landing()
                break
            else:
                print('Плохая связь повторите команду.')
        print('Остановлен двигатель.')


    def speed_dial(self):
        """Набор скорости."""
        self.speed += 20
        time.sleep(0.5)
        print('Скорость: {}'.format(self.speed))


    def height_gain(self, height=50):
        """Набор высоты."""
        self.hight += height
        time.sleep(0.5)
        print('Скорость: {}, Высота полета: {}'.format(self.speed, self.hight))


    def takeoff(self):
        """Набор скорости взлет и набор высоты."""
        while self.speed < 550:
            self.speed_dial()
            if self.speed > 250 and self.hight == 0:
                print('Взлет')
                self.hight += 20
            elif self.speed > 250 and self.hight > 0:
                self.speed_dial()
                self.height_gain()
        print('Вышли на крейсерскую скорость. \nНачинаем набор высоты.')
        while self.hight < 11000:
            self.height_gain(200)

    def deceleration(self):
        """Снижение скорости."""
        self.speed -= 20
        if self.speed < 0:
            self.speed = 0
        time.sleep(0.5)
        print('Снижаем скорость: {} км/ч'.format(self.speed))



    def altitude_reduction(self, height=50):
        """Снижение высоты."""
        self.hight -= height
        if self.hight < 0:
            self.hight = 0
        print('Снижаемся, высота: {} метров'.format(self.hight))
        time.sleep(0.5)


    def landing(self):
        """Метод посадки."""
        while self.hight != 0 or self.speed != 0:
            if self.hight > 5500:
                self.altitude_reduction(200)
            elif self.speed > 250 and self.hight < 5500:
                self.deceleration()
                self.altitude_reduction()
            elif self.hight > 0:
                self.altitude_reduction()
            elif self.hight == 0 and self.speed > 0:
                self.deceleration()
        print('Самолет совершил посадку.')

    def operate(self):
        print('Просто летит самолет.')


class Robot(Flight):
    """Класс робот"""
    def __init__(self, name):
        super().__init__()
        self.name = name

class RobotIntelligens(Robot):
    """Робот разведки"""
    def __init__(self, name):
        super().__init__(name=name)

    def operate(self):
        print('{name} Производится разведка местности.'.format(name=self.name))

class RobotCombat(Robot):
    """Робот боевой"""
    def __init__(self, name, rus):
        super().__init__(name=name)
        self.rus = rus

    def operate(self):
        print('{name} Защищает объект при помощи {rus}'.format(name=self.name, rus=self.rus))

aerobus = RobotIntelligens('a-9')
aerobus.operate()
wardron = RobotCombat('uy-45', 'Пушка')
wardron.start_engine()