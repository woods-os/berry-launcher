#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk #, Gdk
from gi.repository.GdkPixbuf import Pixbuf

from os import system

import launcher

class LauncherWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Select Program")
        self.set_default_size(600, 500)
        
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        
        #self.outerbox = Gtk.Box(spacing=6)
        #self.add(self.outerbox)
        
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        #self.outerbox.pack_start(self.listbox, True, True, 0)
       
        scrolled.add(self.listbox)

        self.add(scrolled)
        
                

        
win = LauncherWindow()

btnList = []

def addBtn(name,icon,executable):
    row = Gtk.ListBoxRow()
    btnIcon = Gtk.IconView.new()
    
    liststore = Gtk.ListStore(Pixbuf, str)
    iconview = Gtk.IconView.new()
    iconview.set_model(liststore)
    iconview.set_pixbuf_column(0)
    iconview.set_text_column(1)
    
    pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
    liststore.append([pixbuf, name])
    
    btn = Gtk.Button()
    btn.add(iconview)

	
# IMPLEMENT THIS METHOD *ASAP*  --------------------------
#    def btnClick (event):
#        if event == "clicked":
#            print ("fired!")
#            system(executable)
#
#    btn.connect("clicked", btnClick)	
# --------------------------------------------------------
    row.add(btn)
    btnList.append(row)
    


for app in launcher.network:
    addBtn(app.name,app.icon,app.executable)
	
for app in launcher.development:
    addBtn(app.name,app.icon,app.executable)

for button in btnList:
    win.listbox.add(button)



win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()










































