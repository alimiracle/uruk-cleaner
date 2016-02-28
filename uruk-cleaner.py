# uruk cleaner 
# to clean your system from cash files and logs

#    Copyright (c) 2016 ali abdul ghani <blade.vp2020@gmail.com>
#    This Program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU  General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This Program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
 #    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
from gi.repository import Gtk
window = Gtk.Window(title="Uruk Cleaner")
window.set_border_width(30)
hbox = Gtk.Box(spacing=6)
window.connect("destroy", lambda w: Gtk.main_quit())

window.add(hbox)
def clean(button1):
    os.system("./log-c.sh")
def ex(button3):
  exit()
def clean_deb(button2):
    os.system("./cash-c.sh")
button1 = Gtk.Button.new_with_label("Clean Logss")
button1.connect("clicked", clean)
hbox.pack_start(button1, True, True, 0)
button2 = Gtk.Button.new_with_label("Clean apt-get Cash")
button2.connect("clicked", clean_deb)
hbox.pack_start(button2, True, True, 0)
button3 = Gtk.Button.new_with_label("Exit")
button3.connect("clicked", ex)
hbox.pack_start(button3, True, True, 0)
window.show_all()
Gtk.main()
