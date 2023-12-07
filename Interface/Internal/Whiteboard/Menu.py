import Zeta
from Zeta.Panel import *

class Menu(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.geometry('-5+5')
		self.attributes('-topmost', True)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddb', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerb', icontype='bw').image
		self.imgex=Zeta.Image.Icon.Load(icon='mathb', icontype='bw').image
		self.imgplay=Zeta.Image.Icon.Load(icon='playb', icontype='bw').image
		self.imgtext=Zeta.Image.Icon.Load(icon='textb', icontype='bw').image
		self.InitWindow()

		Button2(self.frame, text=' [ Active ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Active, toggle=self._Active, geometry='left')
		Button2(self.frame, text=' [ Idea ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Idea, toggle=self._Idea, geometry='left')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(self.frame, text=' Experiment', image=self.imgex, compound='left', side='top', fill='x', hover=self._Experiment, toggle=self._Experiment, geometry='left')
		Button2(self.frame, text=' Read', image=self.imgtext, compound='left', side='top', fill='x', hover=self._Read, toggle=self._Read, geometry='left')
		Button2(self.frame, text=' Play', image=self.imgplay, compound='left', side='top', fill='x', hover=self._Play, toggle=self._Play, geometry='left')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(self.frame, text=' ¦ Temp', image=self.corner, compound='left', side='top', fill='x', hover=self._Temp, toggle=self._Temp, geometry='left')
		Button2(self.frame, text=' ¦ Trial', image=self.corner, compound='left', side='top', fill='x', hover=self._Trial, toggle=self._Trial, geometry='left')

		self.theme(self.frame, bg='#ffffff', fg='#000000')

	def InitWindow(self):
		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button(x.frame, text=' [ Generic ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Code ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Post', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Video', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Active = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button(x.frame, text=' # META', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Explore ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Tools ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' ¦ Paranormal', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ¦ Physical', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ¦ Politics', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ¦ Tech', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' ≡ E', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ≡ F', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Science', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Social', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Weird', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Idea = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button(x.frame, text=' # META', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Project ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Experiment = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button(x.frame, text=' # META', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Progress ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' [ Book ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Thread ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Read = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button(x.frame, text=' # META', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Topics ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Play = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button(x.frame, text=' # META', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Explore ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Tools ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' ¦ Paranormal', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ¦ Physical', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ¦ Politics', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ¦ Tech', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' ≡ E', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ≡ F', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Science', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Social', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Weird', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Temp = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button(x.frame, text=' # META', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' [ Tools ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' ≡ E', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ≡ F', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Project', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Text', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Trial = x