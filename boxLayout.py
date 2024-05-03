'''
2/05/2024
Kivymd. Learning about Layouts specifically box-layout
Layouts as containers that contain widgets to organise our apps in a specifi way

'''

from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# change window background color to white
Window.clearcolor = (1, 1, 1, 1)
# set fixed size for mobile screen
Window.size = (360, 600)

class LayoutApp(App):
    def build(self):
        # initiate layout
        layout = BoxLayout(
            orientation='vertical', # arrange buttons vertically
            spacing='100', # spacing between the buttons
            padding=80, # add space between the button and the root window
        )
        # Add image
        img = AsyncImage(
            source='https://w7.pngwing.com/pngs/140/948/png-transparent-blue-and-yellow-logo-python-logo-programmer-fierce-python-s-cdr-angle-text-thumbnail.png'
        )
        # create buttons
        button = Button(
            text='Login',
            size_hint=(None, None), # control size of the button
            # Control button responsiveness across devices.
            # By declaring size_hint none, and using the width & height attributes
            # button size will stay the same regardless of screen szie
            width=100,
            height=50,
            pos_hint={'center_x':0.5} # position of the button on the screen
        )
        # add buttons to layout
        layout.add_widget(img)
        layout.add_widget(button)
        return layout



LayoutApp().run()