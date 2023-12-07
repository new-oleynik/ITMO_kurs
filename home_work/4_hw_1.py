class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def start(self):
        print('Автомобиль заведён')
    def stall(self):
        print('Автомобиль заглушен')
    def year_of_release(self, new_year):
        self.year = new_year
        print(f'Присвоенный автомобилю год выпуска - {self.year}')
    def car_type(self, new_type):
        self.type = new_type
        print(f'Присвоенный автомобилю тип - {self.type}')
    def car_color(self, new_color):
        self.color = new_color
        print(f'Присвоенный автомобилю цвет - {self.color}')

car1 = Car('grey', 'bentley', '2005')
print('Цвет автомобиля - ', car1.color, 'Тип автомобиля - ', car1.type, 'Год выпуска автомобиля - ', car1.year)
car1.start()
car1.stall()
car1.year_of_release('2015')
car1.car_type('chevrolet')
car1.car_color('red')
