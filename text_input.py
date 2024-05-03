'''
3/05/2024
Kivymd. Learning to take text input from a user through the gui app i create.
In this script i also mess around with gridlayout.

'''

from kivy.app import App 
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

# change window background color to white
Window.clearcolor = (1, 1, 1, 1)
# set fixed size for mobile screen
Window.size = (360, 600)

class GetText(App):
    def build(self):

        layout = GridLayout(
           cols=2,
           row_force_default=True,
           row_default_height = 40,
           padding = 20,
           spacing = 10
        )

        self.weight=TextInput(text='Enter weight Here: ')
        self.height=TextInput(text='Enter height Here: ')

        submit = Button(
            text='Submit',
            on_press=self.submit
        )

        layout.add_widget(self.weight)
        layout.add_widget(self.height)
        layout.add_widget(submit)

        return layout

    def submit(self, obj):
        print(f'weight: {self.weight.text}')
        print(f'height: {self.height.text}')
        
        


GetText().run()