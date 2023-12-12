import Zeta
from Zeta.Panel import *

from .Menu import Menu

class Whiteboard(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)

		self.title('===[ Sidebar: File ]===')
		self.attributes('-topmost', True)
		height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 5 - 5
		self.geometry(f"333x{height}+5+5")
		File1 = FileBox(self.frame, home=Zeta.System.Path.Core.Planner, color2='black')
		# File1 = FileBox(self.frame, home=Zeta.System.Path.Core.Planner, darkmode=False)

		Menu().transient(self)
		self.theme(self.frame, bg='#ffffff', fg='#000000')