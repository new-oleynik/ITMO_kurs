class Soda:
    def __init__(self, dob=None):
        self.dob=dob

    def show_my_drink(self):
        if self.dob:
            print(f'Газировка и {self.dob}')
        else:
            print('обычная газировка')

drink1 = Soda()
drink2 = Soda('Малина')
drink1.show_my_drink()
drink2.show_my_drink()