# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начала движение')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction):
        print(f'Поворот {self.name} в сторону {direction}')

    def show_speed(self, speed):
        print(f'Текущая скорость: {speed}')


class TownCar(Car):
    _max_speed = 60

    def show_speed(self, speed):
        print(f'Текущая скорость: {speed}')
        if speed > self._max_speed:
            print(f'Внимание! Превышена маскимально допустимая скорость на {speed - self._max_speed}!')


class SportCar(Car):
    def __init__(self, speed, name, color='Red'):
        super().__init__(speed, name, color)


class WorkCar(TownCar, Car):
    _max_speed = 40


class PoliceCar(Car):
    def __init__(self, speed, name, color, is_police=True):
        super().__init__(speed=speed, name=name, color=color, is_police=is_police)


town_car = TownCar(70, 'green', 'Mini', )
sport_car = SportCar(180, 'Ferrari')
work_car = WorkCar(55, 'yellow', 'Gazel')
polce_car = PoliceCar(110, 'Lada Sedan', 'medium blue', )

town_car.go()
town_car.turn('Лево')
town_car.stop()
town_car.show_speed(85)

sport_car.go()
sport_car.turn('Лево')
sport_car.stop()
sport_car.show_speed(180)
print(sport_car.is_police)

work_car.go()
work_car.turn('Лево')
work_car.stop()
work_car.show_speed(85)

polce_car.go()
polce_car.turn('Лево')
polce_car.stop()
polce_car.show_speed(160)
