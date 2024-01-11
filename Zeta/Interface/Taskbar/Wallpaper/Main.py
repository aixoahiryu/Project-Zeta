import Zeta
from Zeta.Panel import *

import os


class Wallpaper(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-alpha', Zeta.Setting.opacity)
		width = Zeta.System.Size.Screen.width
		height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
		self.geometry(f"{width}x{height}+0+0")
		self.overrideredirect(1)

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)