'''
Script name: app_5.py
3/05/2024
> Getting user input
Using the builder method to add elements to the app window. This method uses multi-line strings.
'''
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

# from helpers import username_helpers

username_helper = """
MDTextField:
    hint_text: 'Enter User Name'
    helper_text: 'or click on forgot username'
    helper_text_mode: 'on_focus'
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x':0.5, 'center_y': 0.5}
    size_hint_x: None
    width : 300
"""

# boiler plate
class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = 'DeepPurple'
        # username = MDTextField(
        #     text='Enter username',
        #     pos_hint={'center_x':0.5,
        #               'center_y': 0.5},
        #     size_hint_x =None,
        #     width = 300
        # )
        username = Builder.load_string(username_helper)
         
        screen.add_widget(username)
        # username = Builder.load_string(username_helpers)
        return screen
    
DemoApp().run()