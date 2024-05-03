'''
2/05/2024
Putting buttons into my kivy app, centering them and handling press and release events

'''

from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        button = Button(
            text='Something', # text to be displayed inside the button
            size_hint=(0.2,0.2), # ratio of x to y axis of the screen
            font_size='20sp', # font size of the text in the button
            # setting position of the button on the screen. 0 - 1 scale both in the x and y axis
            pos_hint={
                'center_x': 0.5,
                'center_y': 0.5
            },
            # Handling events when the button is clicked and when it is released
            on_press=self.printpress,
            on_release=self.print_release,
        )
        return button
    
    def printpress(self, obj):
        # displays text in the terminal when button is clicked/ pressed down
        print('Button has been preesed')

    def print_release(self, obj):
        # displays text in the terminal when button is released
        print('Button has been released')
MyApp().run()