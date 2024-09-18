from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class Calculator(App):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.can_add_point = True
        self.not_closed_brackets = 0
        self.text_input = None

    def fifth(self, start_x, start_y, screen, button_size):

        button_brackets = Button(text="(", font_size=30, size_hint=button_size,
                                 pos_hint={"x": start_x, "y": start_y - button_size[1] * 7.7})
        button_brackets.bind(on_press=self.tap_button)
        screen.add_widget(button_brackets)
        button_brackets_2 = Button(text=")", font_size=30, size_hint=button_size,
                                   pos_hint={"x": start_x + button_size[0], "y": start_y - button_size[1] * 7.7})
        button_brackets_2.bind(on_press=self.tap_button)
        screen.add_widget(button_brackets_2)
        button_dot = Button(text=".", font_size=30, size_hint=button_size,
                            pos_hint={"x": start_x + button_size[0] * 2, "y": start_y - button_size[1] * 7.7})
        button_dot.bind(on_press=self.tap_button)
        screen.add_widget(button_dot)
        button_delete_all = Button(text="с", font_size=30, size_hint=button_size,
                                   pos_hint={"x": start_x + button_size[0] * 3, "y": start_y - button_size[1] * 7.7})
        button_delete_all.bind(on_press=self.tap_button)
        screen.add_widget(button_delete_all)

    def fourth(self, start_x, start_y, screen, button_size):
        button_0 = Button(text="0", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x + button_size[0] * 2, "y": start_y - button_size[1] * 6.7})
        button_0.bind(on_press=self.tap_button)
        screen.add_widget(button_0)
        button_plus = Button(text="+", font_size=30, size_hint=button_size,
                             pos_hint={"x": start_x + button_size[0], "y": start_y - button_size[1] * 6.7})
        button_plus.bind(on_press=self.tap_button)
        screen.add_widget(button_plus)
        button_minus = Button(text="-", font_size=30, size_hint=button_size,
                              pos_hint={"x": start_x, "y": start_y - button_size[1] * 6.7})
        button_minus.bind(on_press=self.tap_button)
        screen.add_widget(button_minus)
        button_ok = Button(text="=", font_size=30, size_hint=button_size,
                           pos_hint={"x": start_x + button_size[0] * 3, "y": start_y - button_size[1] * 6.7})
        button_ok.bind(on_press=self.tap_button)
        screen.add_widget(button_ok)

    def third(self, start_x, start_y, screen, button_size):
        button_7 = Button(text="7", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x, "y": start_y - button_size[1] * 3})
        button_7.bind(on_press=self.tap_button)
        screen.add_widget(button_7)
        button_8 = Button(text="8", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x + button_size[0], "y": start_y - button_size[1] * 3})
        button_8.bind(on_press=self.tap_button)
        screen.add_widget(button_8)
        button_9 = Button(text="9", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x + button_size[0] * 2, "y": start_y - button_size[1] * 3})
        button_9.bind(on_press=self.tap_button)
        screen.add_widget(button_9)
        button_delete = Button(text="del", font_size=30, size_hint=button_size,
                               pos_hint={"x": start_x + button_size[0] * 3, "y": start_y - button_size[1] * 3})
        button_delete.bind(on_press=self.tap_button)
        screen.add_widget(button_delete)

    def second_row(self, start_x, start_y, screen, button_size):
        button_4 = Button(text="4", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x, "y": start_y - button_size[1] * 2})
        button_4.bind(on_press=self.tap_button)
        screen.add_widget(button_4)

        button_5 = Button(text="5", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x + button_size[0], "y": start_y - button_size[1] * 2})
        button_5.bind(on_press=self.tap_button)
        screen.add_widget(button_5)

        button_6 = Button(text="6", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x + button_size[0] * 2, "y": start_y - button_size[1] * 2})
        button_6.bind(on_press=self.tap_button)
        screen.add_widget(button_6)
        button_multiplication = Button(text="*", font_size=30, size_hint=button_size,
                                       pos_hint={"x": start_x + button_size[0] * 3, "y": start_y - button_size[1] * 2})
        button_multiplication.bind(on_press=self.tap_button)
        screen.add_widget(button_multiplication)

    def first_row(self, start_x, start_y, screen, button_size):
        # first row
        button_1 = Button(text="1", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x, "y": start_y - button_size[1]})
        button_1.bind(on_press=self.tap_button)
        screen.add_widget(button_1)

        button_2 = Button(text="2", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x + button_size[0], "y": start_y - button_size[1]})
        button_2.bind(on_press=self.tap_button)
        screen.add_widget(button_2)

        button_3 = Button(text="3", font_size=30, size_hint=button_size,
                          pos_hint={"x": start_x + button_size[0] * 2, "y": start_y - button_size[1]})
        button_3.bind(on_press=self.tap_button)
        screen.add_widget(button_3)

        button_divide = Button(text="/", font_size=30, size_hint=button_size,
                               pos_hint={"x": start_x + button_size[0] * 3, "y": start_y - button_size[1]})
        button_divide.bind(on_press=self.tap_button)
        screen.add_widget(button_divide)

    def calculate(self):
        try:
            self.text_input.text = str(eval(self.text_input.text))
        except ZeroDivisionError:
            self.text_input.text = "делить на ноль нельзя"
        except SyntaxError:
            pass

    def operations(self, button):
        if self.text_input.text != "" and (self.text_input.text[-1].isdigit() or self.text_input.text[-1] == ")"):
            self.can_add_point = True
            self.text_input.text += button.text

    def point(self, button):
        if self.text_input.text != "" and self.text_input.text[-1].isdigit() and self.can_add_point:
            self.can_add_point = False
            self.text_input.text += button.text

    def closing_bracket(self, button):
        if self.text_input.text != "" and self.text_input.text[-1].isdigit() and self.not_closed_brackets > 0:
            self.not_closed_brackets -= 1
            self.text_input.text += button.text

    def opening_bracket(self, button):
        if self.text_input.text == "" or self.text_input.text[-1] in "+-/*":
            # her
            self.not_closed_brackets += 1
            self.text_input.text += button.text

    def delete_all(self):
        self.text_input.text = ""
        self.can_add_point = True
        self.not_closed_brackets = 0

    def delete(self):
        if self.text_input.text != "":
            if self.text_input.text[-1] == "(":
                self.not_closed_brackets -= 1
            if self.text_input.text[-1] == ")":
                self.not_closed_brackets += 1

            if self.text_input.text[-1] == ".":
                self.can_add_point = True
        self.text_input.text = self.text_input.text[0:-1]

    def tap_button(self, *args):

        button = args[0]
        if self.text_input.text == "делить на ноль нельзя":
            self.text_input.text = ""
        if "del" == button.text:
            self.delete()
        elif "с" == button.text:
            self.delete_all()

        elif button.text == "(":
            self.opening_bracket(button)

        elif button.text == ")":
            self.closing_bracket(button)

        elif button.text == ".":
            self.point(button)

        elif button.text in "+-/*":
            self.operations(button)
        elif "=" == button.text:
            self.calculate()
        # numbers
        elif self.text_input.text == "" or self.text_input.text[-1] != ")":
            self.text_input.text += button.text

    def build(self):
        self.not_closed_brackets = 0
        self.can_add_point = True
        screen = Screen()
        start_x = 0.100
        start_y = 0.750
        self.text_input = TextInput(text="", font_size=30, size_hint=(0.800, 0.250),
                                    pos_hint={"x": start_x, "y": start_y}, readonly=True)
        screen.add_widget(self.text_input)
        button_size = (0.200, 0.190)
        self.first_row(start_x, start_y, screen, button_size)
        self.second_row(start_x, start_y, screen, button_size)
        self.third(start_x, start_y, screen, button_size)
        button_size = (0.200, 0.100)
        self.fourth(start_x, start_y, screen, button_size)
        self.fifth(start_x, start_y, screen, button_size)

        return screen


if __name__ == '__main__':
    app = Calculator()
    app.run()
