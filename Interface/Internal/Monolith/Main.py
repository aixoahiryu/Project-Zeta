import Zeta
from Zeta.Panel import *
from .Pattern.Main import Pattern

class Monolith(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.geometry('-5+5')
		self.attributes('-topmost', True)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddb', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerb', icontype='bw').image
		self.InitWindow()

		Button2(self.frame, text=' # META', image=self.imghdd, compound='left', side='top', fill='x', hover=self._META, toggle=self._META, geometry='left')
		Button2(self.frame, text=' [ Program ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Program, toggle=self._Program, geometry='left')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')

		Pattern().transient(self)
		self.theme(self.frame, bg=self.hue, fg=self.neon)

	def InitWindow(self):
		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' [ Agenda ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button2(x.frame, text=' [ World ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button2(x.frame, text=' [ Vector ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text=' Backup', relief='flat', image=self.corner, compound='left', anchor='w', geometry='left', menucolor='black', listdir=True, path=Zeta.Utility.Format.Path(r'<Downstream>/X/Null/# META/Backup')).pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._META = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' [ Package ]', relief='flat', image=self.corner, compound='left', anchor='w', geometry='left', menucolor='black', listdir=True, path=Zeta.Utility.Format.Path(r'<Downstream>/X/Null/[ Program ]/[ Package ]')).pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Program = x