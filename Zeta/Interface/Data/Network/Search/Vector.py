import Zeta

from Zeta.Panel import *
import os
import subprocess

class Vector(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		left = 25 +5
		bottom = Zeta.System.Size.taskbar
		self.geometry(f'165x25+{left}-{bottom}')
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)

		self.imgvector=Zeta.Image.Icon.Load('line','neon', 'gif').image
		btnmain = Button2(self.frame, text=' Vector', image=self.imgvector, compound='left', width=11, anchor='w', side='top', fill='both', geometry='top', buffer=['Explore', 'Search', 'Proxy'], menucolor='green', textcolor='white')

		self.theme(self.frame, bg=self.hue, fg=self.neon)