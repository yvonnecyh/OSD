#!/usr/bin/env python

usage = """Usage:
python testosd.py &
python settings.py
"""

# Copyright (C) 2004-2006 Red Hat Inc. <http://www.redhat.com/>
# Copyright (C) 2005-2007 Collabora Ltd. <http://www.collabora.co.uk/>
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from gi.repository import GLib

import dbus
import dbus.service
import dbus.mainloop.glib

class DemoException(dbus.DBusException):
    _dbus_error_name = 'com.example.DemoException'

class OsdObject(dbus.service.Object):

    @dbus.service.method("com.example.VideoInterface",
                         in_signature='s', out_signature='as')

    def Set_video_params(self, params):
        print (str(params))
        return ["Set ok", " from testosd.py", "with unique name",
                session_bus.get_unique_name()]
    
    @dbus.service.method("com.example.VideoInterface",
                         in_signature='s', out_signature='as')

    def Get_video_params(self, params):
        print (str(params))
        fps="25.0"
        video_w="1920"
        video_h="1080"
        video_format= "h265"
        return ["Get", " from testosd.py", "fps:", fps, "video_w:",
                video_w, "video_h:", video_h, "video format:", video_format]

    @dbus.service.method("com.example.AudioInterface",
                         in_signature='s', out_signature='as')
    
    def Set_audio_params(self, params):
        print (str(params))
        return ["Set", " from testosd.py", "with unique name",
                session_bus.get_unique_name()]
    
    @dbus.service.method("com.example.AudioInterface",
                         in_signature='s', out_signature='as')
    
    def Get_audio_params(self, params):
        print (str(params))
        audio_format = "mp3"
        sample_rate = "44.1kz"
        bit_depth = "16"
        return ["audio_format:%s"%audio_format, "sample_rate:%s"%sample_rate, "bit_depth:%s"%bit_depth]


    def RaiseException(self):
        raise DemoException('The RaiseException method does what you might '
                            'expect')

    def Exit(self):
        print('loop quit')
        mainloop.quit()


if __name__ == '__main__':
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

    session_bus = dbus.SessionBus()
    name = dbus.service.BusName("com.example.OSDService", session_bus)
    object = OsdObject(session_bus, '/OsdObject')

    mainloop = GLib.MainLoop()
    print ("Running example service.")
    print (usage)
    mainloop.run()

