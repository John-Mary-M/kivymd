'''
Script name: app_2.py
3/05/2024
After completing the basics from tutorials 17 - 22 in the scripts named app_#.py i start to learn about developing a full app

> Add labels (Text): We import from `from kivymd.uix.label import MDLabel` otherwise vanilla kivy syntax doesnt work.
> kviymd also has several theme colors we can apply
> font styles are also available in kivymd
> There are a number of icons to choose from, just search the page [https://github.com/HeaTTheatR/KivyMD/blob/master/kivymd/icon_definitions.py] try out several, find the one you like.
'''
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

# boiler plate
class DemoApp(MDApp):
    def build(self):
        label = MDLabel(
            text='Hello world',  # text/ label to be displayed
            halign='center', # center the text on the screen
            theme_text_color='Custom', # change text color
            text_color=(238/255.0, 99/255.0, 80/255.0, 1), # creating custom colors with rgb. Kivymd uses a 0 -1 scale thus the division
            font_style='H1', # applying a font style

        )
        # icons from Kivy MD
        icon_label = MDIcon(
            icon='youtube', # adding an icon from kivymd. You can find other options in the link got from the class notes.
            pos_hint={"center_x": 0.5, "center_y": 0.5} # center the icon on the screen
        )
        return icon_label
    
DemoApp().run()