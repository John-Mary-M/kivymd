'''
Scrpt name: app_10.py
6/05/2024
> Creating tool bars
> Before app is deployed into production always remeber to remove the window.size() its only for development and testing
'''
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Demo '
            left_action_items: [['menu', lambda x: app.navigation_draw()]]
            right_action_items: [['clock', lambda x: app.navigation_draw()]]
            elevation: 5
            
        MDLabel:
            text: 'Hello World'
            halign: 'center'

        MDBottomAppBar:
            title: 'Help'
            left_action_items: [['coffee', lambda x: app.navigation_draw()]]
            mode: 'end'
            type: 'bottom'
            icon: 'language-python'
            
"""
# set fixed size for mobile screen
Window.size = (360, 600)

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Red'
        #.theme_cls.material_style = "M2"
        # use the builder function to make the screen from the multiline string.
        screen = Builder.load_string(screen_helper)
        return screen
    
    def navigation_draw(self):
        print('Navigating . . .')
DemoApp().run()