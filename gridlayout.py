'''
2/05/2024
Kivymd. Learning about Layouts specifically grid-layout (rows and columns)
Layouts as containers that contain widgets to organise our apps in a specific way.

Gridlayout fills up the first row with all its column ins=tersections befor going to the secound row.

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

class GridoutApp(App):
    def build(self):
        layout = GridLayout(
            cols=2,
            row_force_default=True, # overide the default height of buttons/ any widgets that will be added to this layout.
            padding=20,
            spacing=10,
            row_default_height=40 # set the desired height for buttons and widgets in the layout
        )
        btn_1 = Button(
            text='Hello 1',
            size_hint=(None, None),
            height=40,
            width=100
        )
        btn_2 = Button(
            text='Hello 2'
        )

        btn_3 = Button(
            text='Hello 3',
            size_hint=(None, None),
            height=40,
            width=100
        )
        btn_4 = Button(
            text='Hello 4',
            # color=(0,0,0,1)
        )
        layout.add_widget(btn_1)
        layout.add_widget(btn_2)
        layout.add_widget(btn_3)
        layout.add_widget(btn_4)

        return layout
    
GridoutApp().run()