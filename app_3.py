'''
Script name: app_3.py
3/05/2024
> In this script i learn to add different elements

'''
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton

# boiler plate
class DemoApp(MDApp):
    
    def build(self):
        # Application window
        screen = Screen()
        btn_flat = MDRectangleFlatButton(
                text='Hello', 
                pos_hint={'center_x':0.5,
                          'center_y':0.5},
        )

        icon_btn = MDFloatingActionButton(
            icon='language-python',
            #text='Hello Android', 
            pos_hint={'center_x':0.5,
                      'center_y':0.5}
        )
        # add btn_flat to the window
        screen.add_widget(icon_btn)
        return screen
    
DemoApp().run()