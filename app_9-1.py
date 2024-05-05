'''
Scrpt name: app_9-1.py
3/05/2024
Impllementing everythng in script app_9.py but with the builder function

'''

from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem



# create multi-line string
list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container

"""

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)

        
        return screen
    
    def on_start(self):
        
        for i in range(1,21):
            item = OneLineListItem(
                text = 'Item ' + str(i)
            )
            # acess multiline string onelinelist item 
            self.root.ids.container.add_widget(item)

DemoApp().run()