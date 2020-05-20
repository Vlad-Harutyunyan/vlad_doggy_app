from data_parser import Parse_to_list , List_of_breeds , search


from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.label import MDLabel
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine,MDExpansionPanelOneLine
        

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

KV = '''
# Menu item in the DrawerList list.


    
<ItemDrawer>:

    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
    
<MainContent>:
    spacing: "8dp"
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)
   
    ScrollView:
        DrawerList:
            id:main_item_wrapp
    
    
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"
    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "76dp", "76dp"
            source: "images/doggy1.png"

    MDLabel:
        text: "Doggy App"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: "developer  - vlad.har.yan@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list
            

             
Screen:
    ScrollView:
        DrawerList:
            id: main_content

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Doggy App"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer() ]]
                        

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
                
                
                
'''


parsed_date = Parse_to_list()
clicked_content = ''

class ContentNavigationDrawer(BoxLayout):
    pass


class Content(ThemableBehavior, MDList):
    
    def __init__(self):
        super().__init__()

    def update(self,item):
        self.add_widget(item)
    def set_color_item(self,instance_item):
        pass

class MainContent(BoxLayout):
    def __init__(self):
        super().__init__()
    def on_start(self):
        print(self)

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class DrawerList(ThemableBehavior, MDList):
    global clicked_content
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        # Set the color of the icon and text for the menu item.

        for item in self.children:
            
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                 
                break
            clicked_content = item.text

        instance_item.text_color = self.theme_cls.primary_color
        # print(clicked_content)

class DoggyApp(MDApp):
    def build(self):

        return Builder.load_string(KV)


    # def item_callback(self,instance, value):
    #     self.root.ids.main_content.clear_widgets()

    #     self.root.ids.main_content.add_widget(
    #             MDLabel(text=value)
    #     )
    
    def menu_item_callback(self,instance, value):

        returned_list = search(value,parsed_date)
        self.root.ids.main_content.clear_widgets()
        for doggy in returned_list:
            cont = Content()
            cont.update(ItemDrawer(icon='images/id.png' , text=f" Id - {doggy.id}"))
            cont.update(ItemDrawer(icon='images/tem3.png' , text=f" Temperament - {doggy.temperament}"))
            self.root.ids.main_content.add_widget(
                    MDExpansionPanel(
                    icon=f"images/doggy2.png",
                    content= cont ,
                    panel_cls=MDExpansionPanelThreeLine( 
                        text=doggy.name,
                        secondary_text=f"Life span - {doggy.life_span}",
                        tertiary_text=f"Weight - {doggy.weight} kg",
                    )
                    
                 )
                )
        
    def on_start(self):
        dogs = parsed_date
        breeds = List_of_breeds(dogs)
        
        for breed in breeds:

            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon='images/dog_icon1.png', text=breed,on_release=lambda x, y=breed: self.menu_item_callback(x, y) )
            )
        


DoggyApp().run()