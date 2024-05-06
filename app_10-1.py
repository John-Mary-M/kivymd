'''
Scrpt name: app_10.py
6/05/2024
> Binding datatables to a method

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
            rows_num = 10, # Number of rows to be displayed on the screen
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
                ('3', 'Oats', '150'),
                ('4', 'Oats', '150'),
                ('5', 'Oats', '150'),
                ('6', 'Oats', '150'),
                ('7', 'Oats', '150'),
                ('8', 'Oats', '150'),
                ('9', 'Oats', '150'),
                
            ]
            
        )
        # bind table to a method 
        table.bind(on_check_press=self.check_press) # called whenever the checkboex is clicked
        table.bind(on_row_press=self.row_press) # called when row is clicked
        # add table on screen
        screen.add_widget(table)

        return screen
    def check_press(self, instance_table, current_row):
        '''Instance_table has the table data where the click happened, current_row has values of the row that has been pressed '''
        print(instance_table, current_row)

    def row_press(self, instance_row, current_row):
        print(instance_row, current_row)

DemoApp().run()