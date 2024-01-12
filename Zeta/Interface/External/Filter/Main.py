import Zeta
from Zeta.Panel import *
from .Debug import Debug

class Filter(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='white', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacity)
		height = Zeta.System.Size.Screen.height - 25 -Zeta.System.Size.taskbar -Zeta.System.Size.Window.mpv[1] -5
		self.geometry(f"333x{height}+30+25")

		self.File1 = FileBox(self.frame, home='<X>/Void/[ Workspace ]/Filter', color2='white', controller=Workspace.controller, workspace=Workspace)

		Debug().transient(self)
		self.theme(self.frame, bg='#000000', fg='#ffffff')