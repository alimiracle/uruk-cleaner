# this file is part from uruk-cleaner
#    uruk-cleaner is free software: you can redistribute it and/or modify
#    it under the terms of the GNU  General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    uruk-cleaner is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
 #    You should have received a copy of the GNU General Public License
from gi.repository import Gtk
Gtk.init(None)
q=Gtk.MessageDialog(None, Gtk.DialogFlags.MODAL, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Cleaning Complete!")
q.format_secondary_text("All logs files was cleaning.")
q.run()
