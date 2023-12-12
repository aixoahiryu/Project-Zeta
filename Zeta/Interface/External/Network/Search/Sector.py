import Zeta

from Zeta.Panel import *
import os
import subprocess

class Sector(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		left = 25 + 165 +5 +3
		bottom = Zeta.System.Size.taskbar
		self.geometry(f'165x25+{left}-{bottom}')
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)

		self.imgsector=Zeta.Image.Icon.Load('table','neon', 'gif').image
		btnmain = Button2(self.frame, text=' Sector', image=self.imgsector, compound='left', width=11, anchor='w', side='top', fill='both', geometry='top', buffer=['Region: chinese, russian, ...', 'Density: mainstream, ...', 'Community: '], menucolor='green', textcolor='white')

		self.theme(self.frame, bg=self.hue, fg=self.neon)