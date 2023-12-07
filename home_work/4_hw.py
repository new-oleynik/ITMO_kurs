class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def S(self):
        return self.width * self.height

    def P(self):
        return (self.width + self.height) * 2

rectangle1 = rectangle(5,8)
rectangle2 = rectangle(24,98)
rectangle3 = rectangle(1,1)

print('Площадь -', rectangle1.S(), 'Периметр -', rectangle1.P())
print('Площадь -', rectangle2.S(), 'Периметр -', rectangle2.P())
print('Площадь -', rectangle3.S(), 'Периметр -', rectangle3.P())

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        if self.a > self.b:
            return self.a / self.b
        else:
            return self.b / self.a

    def subtraction(self):
        return self.a - self.b

answer = Math(5, 6)
print('Результат сложения -', answer.addition(), 'Результат умножения -', answer.multiplication(), 'Результат деления -', answer.division(), 'Результат вычитания -', answer.subtraction())

class Button:
    def __init__(self, text, type='button', loc=None):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return print(f'{self.text}', f'Клик по кнопке {self.text}')

text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_links_img = Button('Broken Links - Images')
upload_download = Button('Upload and Download')
dynamic_prop = Button('Dynamic Propeties')

text_box.click()
check_box.click()
radio_button.click()
web_tables.click()
buttons.click()
links.click()
broken_links_img.click()
upload_download.click()
dynamic_prop.click()