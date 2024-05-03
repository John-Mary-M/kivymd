'''
Script name: app_1.py
3/05/2024
After completing the basics from tutorials 17 - 22 in the scripts named app_#.py i start to learn about developing a full app

> In this script i learn to setup the boiler plate code for the start of a project and the different import we use instead of kivy we use kivymd and import MDApp

> this app returns just an empty window.
'''
from kivymd.app import MDApp

# boiler plate
class DemoApp(MDApp):
    def build(self):
        return 
    
DemoApp().run()