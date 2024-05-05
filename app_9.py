'''
Script name: app_9.py
3/05/2024
> Lists: one line list items, two-line list items, 3-line list items, and avatar lists.
> Scroll view enables us to scroll through the list. 
> Scroll view is from the kivy library.
> avatar list and icon list

To implement scroll view the MDList has to get added to the scrollview and then the scroll view onto the screen
>NOTE: ImageRightWidget has not been properly implemented in Kivy md so its use always reasults into an error
'''

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import ThreeLineListItem, MDList
from kivymd.uix.list import ThreeLineAvatarListItem, ImageLeftWidget
from kivy.uix.scrollview import ScrollView


class DemoApp(MDApp):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view = MDList()
        # add MDList to scroll view
        scroll.add_widget(list_view)

        # create the OneLineListItem
        # item_1 = OneLineListItem(
        #     text='Item 1'
        # )
        # item_2 = OneLineListItem(
        #     text='Item 2'
        # )
        # Using a for loop to create list items
        for i in range(20):
            # add icons to the list
            image = ImageLeftWidget(source='imageAvatar.png')
            items = ThreeLineAvatarListItem(text='Item ' + str(i), 
                                    secondary_text='Hello world',
                                    tertiary_text='some more text')
            
            # add the icons in the items
            items.add_widget(image)
            # add items to mdlist
            list_view.add_widget(items)

        # add scroll view to screen
        screen.add_widget(scroll)
        
        return screen
    
DemoApp().run()