import Zeta
from Zeta.Panel import *

downstream = Zeta.System.Path.Core.downstream

class Toolbar(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.attributes('-topmost', True)
		self.title('Tool bar')
		width = Zeta.System.Size.Screen.width - 10 - 10
		height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 10 -10
		self.geometry(f"{width}x{height}+10+10")

		frame1 = Frame(self.frame)
		frame1.pack(side='left', fill='both', expand=True)
		frame2 = Frame(self.frame)
		frame2.pack(side='left', fill='both', expand=True)
		frame3 = Frame(self.frame)
		frame3.pack(side='left', fill='both', expand=True)

		File1 = FileBox(frame1, home=downstream+r'/Toolbar/F', color2='black')
		File2 = FileBox(frame2, home=downstream+r'/Toolbar/N', color2='black')
		File3 = FileBox(frame3, home=downstream+r'/Toolbar/_', color2='black')
		# File1 = FileBox(frame1, home=downstream+r'/Toolbar/F', darkmode=False)
		# File2 = FileBox(frame2, home=downstream+r'/Toolbar/N', darkmode=False)
		# File3 = FileBox(frame3, home=downstream+r'/Toolbar/_', darkmode=False)

		self.theme(self.frame, bg='#ffffff', fg='#000000')