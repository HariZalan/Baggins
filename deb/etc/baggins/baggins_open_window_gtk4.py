#!/usr/bin/env python3
import os
bilbospath=os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
bagpath=os.path.expanduser("~")+"/.baggins"
import gi
gi.require_version("Gtk","4.0")
gi.require_version("WebKit","6.0")
from gi.repository import Gtk, Gdk, Gio, GLib
from gi.repository import WebKit as WebKit2

