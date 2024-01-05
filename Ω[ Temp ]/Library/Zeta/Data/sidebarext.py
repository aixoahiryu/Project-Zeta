import Zeta
from Zeta.Panel import *
import os

class Sidebar(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', 0.1)
		self.title('1ext')
		height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25
		bottom = Zeta.System.Size.taskbar
		self.geometry(f"1x{height}-0-{bottom}")
		self.overrideredirect(1)
		self.configure(bg='#000000')