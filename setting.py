'''
Kivy OsdModule
============

THis is the Kivy Osd Module.It offers Osd interface for video/audio/network/status
checking and setting.
The subitems for video/audio/network/status are descriped in seperate kv files
under kv dir. While the image thumbnails are under img dir

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
import dbus
from traceback import print_exc

class Osdmain(BoxLayout):
    '''Catalog of widgets. This is the root widget of the app.
    '''
    def __init__(self, **kwargs):
        self._previously_parsed_text = ''
        super(Osdmain, self).__init__(**kwargs)
        self.carousel = None
    '''Manager screen button for sub-items'''
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
    '''Dbus exception'''    
    def Dbus_exp():
        print_exc()
        sys.exit(1)
    '''set audio input '''    
    def set_audio_inputs(self):
        print ('step to set items:')

        audioin_reply_list = SettingsApp.remote_object.Set_audio_params("set param from setting.py!",
            dbus_interface = "com.example.AudioInterface")

        print (audioin_reply_list)
    
    def get_audio_outputs(self):
        print ('step to get items:')

        audioin_reply_list = SettingsApp.remote_object.Get_audio_params("get param from setting.py!",
            dbus_interface = "com.example.AudioInterface")

        print (audioin_reply_list)
    
    def get_audio_status(self):
        print ('step to get audio status:')

        audioin_reply_list = SettingsApp.remote_object.Get_Status("get status from setting.py!",
            dbus_interface = "com.example.AudioInterface")

        print (audioin_reply_list)
    
    def set_video_inputs(self):
        print ('step to set video inputs:')

        videoin_reply_list = SettingsApp.remote_object.Set_video_params("set param from setting.py!",
            dbus_interface = "com.example.VideoInterface")

        print (videoin_reply_list)
    
    def get_video_outputs(self):
        print ('step to set video outputs:')

        videoin_reply_list = SettingsApp.remote_object.Get_video_params("set param from setting.py!",
            dbus_interface = "com.example.VideoInterface")

        print (videoin_reply_list)

class SettingsApp(App):
    '''The kivy App that runs the main root. All we do is build a catalog
    widget into the root.'''
    tmpsmwidget = ScreenManager();
    
    bus = dbus.SessionBus()
    try:
        remote_object = bus.get_object("com.example.OSDService",
                                   "/OsdObject")
    except dbus.DBusException:
            Osdmain.Dbus_exp()
    
    def build(self):
        return Osdmain()

    def on_pause(self):
        return True
    
    def set_audio_inputs(self):
        Osdmain.set_audio_inputs(self)
    
    def get_audio_outputs(self):
        Osdmain.get_audio_outputs(self)
    
    def set_video_inputs(self):
        Osdmain.set_video_inputs(self)
    
    def get_video_outputs(self):
        Osdmain.get_video_outputs(self)


if __name__ == "__main__":
    SettingsApp().run()
