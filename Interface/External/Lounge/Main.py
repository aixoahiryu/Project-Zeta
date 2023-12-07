import Zeta
from Zeta.Panel import *
from .Playing import Playing
from .Entertain import Entertain
from .Camp import Camp

import os
import subprocess

class Lounge(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		bottom = Zeta.System.Size.taskbar +10
		self.geometry(f'-10-{bottom}')
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerw', icontype='bw').image
		self.imgplay=Zeta.Image.Icon.Load(icon='playw', icontype='bw').image
		self.imgmusic=Zeta.Image.Icon.Load(icon='volumew', icontype='bw').image
		# self.InitWindow()

		Button2(self.frame, text=' Video', image=self.imgplay, compound='left', side='right', fill='y', path='<Scraps>/shortcut/E/video', buffer=['MV', 'Temp', '|', 'Backup'], menucolor='green', textcolor='white', geometry='top')
		Button2(self.frame, text=' Audio', image=self.imgmusic, compound='left', side='right', fill='y', path='<Scraps>/shortcut/E/audio', buffer=['MP3'], menucolor='green', textcolor='white', geometry='top')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='right', fill='y')
		Button2(self.frame, text=' Explore', image=self.imghdd, compound='left', side='right', fill='y', path='<Scraps>/shortcut/E/explore', listdir=True, menucolor='green', textcolor='white', geometry='top')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='right', fill='y')

		Playing().transient(self)
		Entertain().transient(self)
		Camp().transient(self)

		self.theme(self.frame, bg=self.hue, fg='#ffffff')

	# def InitWindow(self):
	# 	x = Window(mode='border', color2='green')
	# 	x.attributes('-topmost', True)
	# 	x.attributes('-alpha', Zeta.Setting.opacityneon)
	# 	Button(x.frame, text=' MV', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
	# 	Button(x.frame, text=' Temp', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
	# 	Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
	# 	Button(x.frame, text=' Backup', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
	# 	x.theme(x.frame, fg='#ffffff', bg=x.hue)
	# 	self._Video = x

	# 	x = Window(mode='border', color2='green')
	# 	x.attributes('-topmost', True)
	# 	x.attributes('-alpha', Zeta.Setting.opacityneon)
	# 	Button(x.frame, text=' MP3', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
	# 	Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
	# 	x.theme(x.frame, fg='#ffffff', bg=x.hue)
	# 	self._Audio = x