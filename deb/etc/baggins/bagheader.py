import gi
gi.require_version("Gtk","3.0")
from gi.repository import Gtk
def dialogdisplay(caption="Bug",text="The program has a bug, methinks."):
    ourdialog=Gtk.MessageDialog(flags=0,message_type=Gtk.MessageType.INFO,buttons=Gtk.ButtonsType.OK,text=caption)
    ourdialog.format_secondary_text(text)
    ourdialog.run()
    ourdialog.destroy()
