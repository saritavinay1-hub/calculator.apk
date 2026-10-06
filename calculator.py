from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class Calculator(App):

    def build(self):

        layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        # App title
        title = Label(
            text='MY CALCULATOR',
            font_size=25,
            size_hint_y=0.1
        )

        layout.add_widget(title)

        # Display
        self.display = TextInput(
            text='',
            font_size=40,
            readonly=True,
            halign='right',
            size_hint_y=0.2
        )

        layout.add_widget(self.display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['⌫', '=']
        ]

        for row in buttons:

            row_layout = BoxLayout(
                spacing=10
            )

            for text in row:

                button = Button(
                    text=text,
                    font_size=30
                )

                if text in ['/', '*', '-', '+', '=']:
                    button.background_normal = ''
                    button.background_color = (
                        0.2, 0.6, 0.9, 1
                    )

                elif text == 'C':
                    button.background_normal = ''
                    button.background_color = (
                        0.9, 0.2, 0.2, 1
                    )

                elif text == '⌫':
                    button.background_normal = ''
                    button.background_color = (
                        0.9, 0.6, 0.1, 1
                    )

                button.bind(
                    on_press=self.button_pressed
                )

                row_layout.add_widget(button)

            layout.add_widget(row_layout)

        return layout

    def button_pressed(self, instance):

        text = instance.text

        if text == 'C':
            self.display.text = ''

        elif text == '⌫':
            self.display.text = self.display.text[:-1]

        elif text == '=':
            try:
                self.display.text = str(
                    eval(self.display.text)
                )
            except:
                self.display.text = 'Error'

        else:
            self.display.text += text


Calculator().run()
