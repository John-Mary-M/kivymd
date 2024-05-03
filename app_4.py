'''
Script name: app_4.py
3/05/2024
> Themes for the entire app
'''
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

# boiler plate
class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Amber' # Choosing a color for the app
        self.theme_cls.primary_hue='A700' # Adjust lightness of darkness of theme
        self.theme_cls.theme_style='Dark' # backgrond theme for entire app
        screen = Screen()
        btn_flat = MDRectangleFlatButton(
            text='Hello',
            pos_hint={'center_x': 0.5,
                      'center_y': 0.5}
        )

        screen.add_widget(btn_flat)
        return screen
    
DemoApp().run()