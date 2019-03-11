'''
Kivy Catalog
============

The Kivy Catalog viewer showcases widgets available in Kivy
and allows interactive editing of kivy language code to get immediate
feedback. You should see a two panel screen with a menu spinner button
(starting with 'Welcome') and other controls across the top.The left pane
contains kivy (.kv) code, and the right side is that code rendered. You can
edit the left pane, though changes will be lost when you use the menu
spinner button. The catalog will show you dozens of .kv examples controlling
different widgets and layouts.

The catalog's interface is set in the file kivycatalog.kv, while the
interfaces for each menu option are set in containers_kvs directory. To
add a new .kv file to the Kivy Catalog, add a .kv file into the container_kvs
directory and reference that file in the ScreenManager section of
kivycatalog.kv.

Known bugs include some issue with the drop
'''
import kivy
kivy.require('1.4.2')
import os
import sys
from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder, Parser, ParserException
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen, ScreenManager

class Catalog(BoxLayout):
    '''Catalog of widgets. This is the root widget of the app. It contains
    a tabbed pain of widgets that can be displayed and a textbox where .kv
    language files for widgets being demoed can be edited.

    The entire interface for the Catalog is defined in kivycatalog.kv,
    although individual containers are defined in the container_kvs
    directory.

    To add a container to the catalog,
    first create the .kv file in container_kvs
    The name of the file (sans .kv) will be the name of the widget available
    inside the kivycatalog.kv
    Finally modify kivycatalog.kv to add an AccordionItem
    to hold the new widget.
    Follow the examples in kivycatalog.kv to ensure the item
    has an appropriate id and the class has been referenced.

    You do not need to edit any python code, just .kv language files!
    '''

    def __init__(self, **kwargs):
        self._previously_parsed_text = ''
        super(Catalog, self).__init__(**kwargs)
        self.carousel = None

    def setting_items(self,value):
        print ('step to',value,'setting items:')
        app = App.get_running_app()
        print ('1',app.tmpsmwidget.current)
        self.parent.remove_widget(app.tmpsmwidget) 
        app.tmpsmwidget = Builder.load_file('kv/screen.kv')
        print ('2',app.tmpsmwidget.current)
        app.tmpsmwidget.current = value
        print ('3',app.tmpsmwidget.current)
        self.parent.add_widget(app.tmpsmwidget) 
    
    def set_audio_inputs(self):
        print ('step to',value,'setting items:')
        app = App.get_running_app()

class SettingsApp(App):
    '''The kivy App that runs the main root. All we do is build a catalog
    widget into the root.'''
    tmpsmwidget = ScreenManager();  
    def build(self):
        return Catalog()

    def on_pause(self):
        return True
    
    def set_audio_inputs(self):
        print ('step to setting items:')
        app = App.get_running_app()



if __name__ == "__main__":
    SettingsApp().run()
