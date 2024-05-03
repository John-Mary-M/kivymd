'''
3/05/2024
Kivymd. Learning to take text input from a user through the gui app i create.
In this script i also mess around with gridlayout and nested layouts.

'''

from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

# change window background color to white
Window.clearcolor = (1, 1, 1, 1)
# set fixed size for mobile screen
Window.size = (360, 600)

class GetText(App):
    def build(self):
        pass


GetText().run()