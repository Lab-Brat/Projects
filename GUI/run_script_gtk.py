import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class gui(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='THIS IS A WINDOW!')

        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Click Me!")
        self.button1.connect("clicked", self.button_clicked1)
        self.box.pack_start(self.button1, True, True, 0)
        # self.add(self.button)

        self.button2 = Gtk.Button(label="Click Me!")
        self.button2.connect("clicked", self.button_clicked2)
        self.box.pack_start(self.button2, True, True, 0)

    def button_clicked1(self, widget):
        print("Great Success.")

    def button_clicked2(self, widget):
        print("Great Success, Again.")


window = gui()
window.connect("delete-event", Gtk.main_quit)
window.show_all()

# main loop
Gtk.main()
