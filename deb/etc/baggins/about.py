#!/usr/bin/env python3
import gi
gi.require_version("Gtk","4.0")
gi.require_version("Adw","1")
from gi.repository import Gtk, Adw, Gdk
css_provider = Gtk.CssProvider()
css_provider.load_from_data(b"""
.about {
	padding: 5px;
	min-height: 400px;
	border-radius: 20px;
}
""")
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
def onactivate(application):
	dialogue=Adw.AboutWindow()
	dialogue.set_application(application)
	dialogue.set_application_name("Baggins")
	dialogue.set_version("2.3")
	dialogue.set_developer_name("Zalán Hári")
	dialogue.set_application_icon("web-browser")
	dialogue.set_license_type(Gtk.License(Gtk.License.GPL_3_0))
	dialogue.set_website("https://github.com/HariZalan/Baggins")
	dialogue.set_issue_url("https://github.com/HariZalan/Baggins/issues")
	dialogue.set_valign(Gtk.Align.FILL)
	dialogue.set_visible(True)
application=Gtk.Application()
application.connect("activate",onactivate)
application.run(None)
