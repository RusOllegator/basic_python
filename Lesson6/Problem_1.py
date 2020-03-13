# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный мет
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
from time import sleep


class TrafficLight:
    def __init__(self, start_color):
        self.color = start_color
        if self.color not in self.l_colors:
            print('Инициализация сфетофора завершилась ошибкой')

    l_colors = ['red', 'yellow', 'green']

    def light_pause(self):
        d_colors_pause = {'red': 5, 'yellow': 2, 'green': 10}
        sleep(d_colors_pause[self.color])

    def _running(self):
        print(self.color)
        self.light_pause()
        i = self.l_colors.index(self.color)
        while self.color in self.l_colors:  # Выходим аварийно, реализовать выход дорого и не обсуждалось
            i += 1
            if i == len(self.l_colors):
                i = 0
            self.color = self.l_colors[i]
            print(self.color)
            self.light_pause()


svetofor = TrafficLight('red')
svetofor._running()
