'''
Script name: app_7.py
3/05/2024
> Building dialog boxes
'''

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder

from helpers import username_helper

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
        if self.username.text is '':
            check_string = 'Please Enter USername'
        else:
            check_string = self.username.text + ' Does not exist'
        # add close button
        close_button = MDFlatButton(
            text='Close',
            on_release=self.close_dialog
        )
        #
        more_button = MDFlatButton(
            text='More'
        )
        #make dialog box in method
        self.dialog = MDDialog(
            text=check_string,
            title='User name check',
            size_hint=(0.7, 1),
            buttons=[close_button, more_button]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
        
    
DemoApp().run()