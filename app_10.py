'''
Scrpt name: app_10.py
6/05/2024
> Displaying data in tables

'''

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

from kivy.core.window import Window

# set fixed size for mobile screen
Window.size = (360, 600)

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        # create the table
        table = MDDataTable(
            pos_hint = {
                'center_x': 0.5,
                'center_y': 0.5
            },
            size_hint = (0.9,0.6),
            check = True, # add checkbox
            column_data = [
                ('No.', # Name of column
                 dp(18) # Display pixels
                 ),
                ('Food', # Name of column
                 dp(20) # Display pixels/ gaps between columns
                 ),
                 ('Calories', dp(20)), # Second column in the table
            ],
            # add rows
            row_data = [
                ('1', 'Burger', '300'),
                ('2', 'Oats', '150'),
            ]
        )
        # add table on screen
        screen.add_widget(table)

        return screen
    

DemoApp().run()