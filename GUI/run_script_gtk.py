import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class gui(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='THIS IS A WINDOW!')

        self.set_border_width(10)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        # Checkbox
        row1 = Gtk.ListBoxRow()
        box1 = Gtk.Box(spacing=100)
        row1.add(box1)
        label = Gtk.Label("Check it: ")
        check = Gtk.CheckButton()
        box1.pack_start(label, True, True, 0)
        box1.pack_start(check, True, True, 0)
        listbox.add(row1)

        # self.box = Gtk.Box(spacing=20)
        # self.add(self.box)

        self.button1 = Gtk.Button(label="Click Me!")
        self.button1.connect("clicked", self.button_clicked1)
        # self.box.pack_start(self.button1, True, True, 0)
        # self.add(self.button)

        self.button2 = Gtk.Button(label="Click Me!")
        self.button2.connect("clicked", self.button_clicked2)
        # self.box.pack_start(self.button2, True, True, 0)


    def button_clicked1(self, widget):
        print("Great Success.")

    def button_clicked2(self, widget):
        print("Great Success, Again.")


window = gui()
window.connect("delete-event", Gtk.main_quit)
window.show_all()

# main loop
Gtk.main()
