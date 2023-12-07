import Zeta

from Zeta.Panel import *
import os
import subprocess

class Entertain(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.geometry(f'+{25+10}+{25}')
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerw', icontype='bw').image
		self.imgsocial=Zeta.Image.Icon.Load(icon='socialw', icontype='bw').image
		self.InitWindow()

		Button2(self.frame, text=' Social', image=self.imgsocial, compound='left', side='top', fill='x', hover=self._Social, toggle=self._Social, geometry='right')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(self.frame, text=' E ', image=self.imghdd, compound='left', side='top', fill='x', hover=self._E, toggle=self._E, geometry='right')
		Button2(self.frame, text=' F ', image=self.imghdd, compound='left', side='top', fill='x', hover=self._F, toggle=self._F, geometry='right')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')

		self.theme(self.frame, bg=self.hue, fg='#ffffff')

	def InitWindow(self):
		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Chan', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Forums', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Social', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Profile', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Social = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' [ Channel ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Anime', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Book', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Game', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Music', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' TV', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Webcomic', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Lore', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Horror', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._E = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' # MAIN', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' # Archive', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' # Watch', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' [ Explore ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Art', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Audio', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Book', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Comic', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Game', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Story', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Video', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' SFW', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._F = x