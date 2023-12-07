import Zeta
from Zeta.Panel import *

import time

class Switcher(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.title('Task bar')
		width = 25
		height = Zeta.System.Size.Screen.height - 25 - Zeta.System.Size.taskbar
		self.geometry(f"{width}x{height}+1+25")
		self.overrideredirect(1)

		self.imgmenu=Zeta.Image.Icon.Load(icon='menuw', icontype='bw').image
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerw', icontype='bw').image
		self.imgnetwork=Zeta.Image.Icon.Load(icon='networkw', icontype='bw').image
		self.imglounge=Zeta.Image.Icon.Load(icon='volumew', icontype='bw').image
		self.imgexplore=Zeta.Image.Icon.Load(icon='tabw', icontype='bw').image
		self.imgplay=Zeta.Image.Icon.Load(icon='playw', icontype='bw').image
		self.imgtext=Zeta.Image.Icon.Load(icon='textw', icontype='bw').image
		self.imgterm=Zeta.Image.Icon.Load(icon='termbw', icontype='bw').image
		self.imglink=Zeta.Image.Icon.Load(icon='linkw', icontype='bw').image
		self.imgsearch=Zeta.Image.Icon.Load(icon='searchw', icontype='bw').image
		self.imggear=Zeta.Image.Icon.Load(icon='gearw', icontype='bw').image

		self.frame1 = Frame(self.frame)
		self.frame1.pack(side='top', fill='both', pady=5)
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		self.frame2 = Frame(self.frame)
		self.frame2.pack(side='top', fill='both', pady=5)
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')		
		self.frame3 = Frame(self.frame)
		self.frame3.pack(side='bottom', fill='both', pady=5)

		Button(self.frame1, image=self.imghdd, relief='flat').pack(side='top', fill='x')
		Button(self.frame1, image=self.imgnetwork, relief='flat').pack(side='top', fill='x')
		Button(self.frame1, image=self.imglounge, relief='flat').pack(side='top', fill='x')

		Button(self.frame2, image=self.imgexplore, relief='flat', command=lambda: Zeta.Utility.Launch.Explorer(home=Zeta.System.Path.Scraps.path, geometry=f"+{25+333+10}+25", transient=Workspace.panel[Workspace.active]['root'])).pack(side='top', fill='x')
		Button(self.frame2, image=self.imgtext, relief='flat', command=lambda: Zeta.Utility.Launch.Editor(path=f'<Scraps>/workspace/void/{Workspace.active}/{str(round(time.time()))}.txt', geometry=f"+{25+333+10}+25", transient=Workspace.panel[Workspace.active]['root'])).pack(side='top', fill='x')
		Button(self.frame2, image=self.imgterm, relief='flat', command=lambda: Zeta.System.OS.terminal(Zeta.System.Path.Scraps.path)).pack(side='top', fill='x')
		Button(self.frame2, image=self.imglink, relief='flat').pack(side='top', fill='x')
		Button(self.frame2, image=self.imgplay, relief='flat').pack(side='top', fill='x')

		Button(self.frame3, image=self.imggear, relief='flat').pack(side='bottom', fill='x')
		Button(self.frame3, image=self.imgsearch, relief='flat').pack(side='bottom', fill='x')

		self.theme(self.frame, bg=self.hue, fg=self.neon)
