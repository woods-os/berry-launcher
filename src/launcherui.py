#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk #, Gdk
from gi.repository.GdkPixbuf import Pixbuf

from os import system

import launcher

class LauncherWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Launch")
        self.set_default_size(600, 500)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        self.create_flowbox(flowbox)

        scrolled.add(flowbox)

        #self.add(vbox)
        self.add(scrolled)
        self.show_all()





    def addBtn(self, name, icon, executable):
        row = Gtk.ListBoxRow()
        btnIcon = Gtk.IconView.new()

        liststore = Gtk.ListStore(Pixbuf, str)
        iconview = Gtk.IconView.new()
        iconview.set_model(liststore)
        iconview.set_pixbuf_column(0)
        iconview.set_text_column(1)

        pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 48, 0)
        liststore.append([pixbuf, name])

        btn = Gtk.Button()
        btn.connect("clicked", self.btnclicked, executable)
        btn.add(iconview)
        return btn



    def btnclicked(self,button,executable):
        print ("Running:", executable)
        system(executable)

    def create_flowbox (self, flowbox):
        for app in launcher.development:
            button = self.addBtn(app.name,app.icon,app.executable)
            flowbox.add(button)
        for app in launcher.network:
            button = self.addBtn(app.name,app.icon,app.executable)
            flowbox.add(button)


win = LauncherWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
