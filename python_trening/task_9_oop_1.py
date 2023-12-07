from task_9_checks import Checks
class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search = Input('input#search', 'text')
class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

home_button = Button('button#home','home button')
class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

home_title = Title('title#home','home title')
class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

home_link = Link('link#home','/home_link')

print(search.check_text(), home_button.check_text(), home_title.check_text(), home_link.check_text())


