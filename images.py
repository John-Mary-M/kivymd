'''
2/05/2024
Adding images to the app
If image in the same directory as app use `from kivy.uix.image import Image` if image is from a url use `from kivy.uix.image import AsyncImage`
'''

from kivy.app import App
from kivy.uix.image import Image, AsyncImage


class MyApp(App):
    def build(self):
        # img = Image(source='python.jpg')
        # How to use AsyncImage to use an image from a URL
        img = AsyncImage(source='https://w7.pngwing.com/pngs/140/948/png-transparent-blue-and-yellow-logo-python-logo-programmer-fierce-python-s-cdr-angle-text-thumbnail.png')
        return img


MyApp().run()