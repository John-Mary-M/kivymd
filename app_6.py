'''
Script name: app_6.py
3/05/2024
> binding buttons to user input
'''
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder

from helpers import username_helper


# boiler plate
class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        # set app theme
        self.theme_cls.primary_palette = 'Green'
        
        button = MDRectangleFlatButton(
            text='Show',
            pos_hint={'center_x':0.5, 'center_y': 0.4},
            on_release=self.show_data
        )

        # load helper string with attributes and functionality
        self.username = Builder.load_string(username_helper)
         
         # add username and button to screen
        screen.add_widget(self.username)
        screen.add_widget(button)
       
        return screen
    
    def show_data(self, obj):
        print(f'{self.username.text}')
    
DemoApp().run()