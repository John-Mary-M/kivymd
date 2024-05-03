'''
2/05/2024
Creating mobile apps with Kivy. Back to basics with kivymd (Material design) emphasing google design best practices and already made elements i can use to design my app.
'''

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window

# change background color for entire screen
Window.clearcolor = (1, 1, 1, 1)

class MainApp(App):
    def build(self):
        # adding a label to the screen
        text_to_display = Label(
            text='This is me in Kvy',
            font_size='30',
            bold=True,
            # font_color='255,0,0',
            color=(102, 128, 100, 1),
            italic=True
        )
        return text_to_display
    
# running the app
MainApp().run()