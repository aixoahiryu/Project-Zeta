import Zeta
from Zeta.Panel import *

class REMenu(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.imgintercept=Zeta.Image.Icon.Load(icon='eye2w', icontype='bw').image
		self.imgrecon=Zeta.Image.Icon.Load(icon='systemw', icontype='bw').image
		self.imgexploit=Zeta.Image.Icon.Load(icon='debugw', icontype='bw').image

		Button(self.frame, text=' # List', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.ZETA)).pack(side='top', fill='x')
		Button(self.frame, text=' # Data', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X)).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(self.frame, text=' [ Intercept ]', relief='flat', image=self.imgintercept, compound='left', anchor='w').pack(side='top', fill='x')
		Button(self.frame, text=' [ Recon ]', relief='flat', image=self.imgrecon, compound='left', anchor='w').pack(side='top', fill='x')
		Button(self.frame, text=' [ Exploit ]', relief='flat', image=self.imgexploit, compound='left', anchor='w').pack(side='top', fill='x')
		Button(self.frame, text=' [ Tools ]', relief='flat', image=self.imghdd, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(self.frame, text='Terminal', relief='flat', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X+r'/Void/Upload')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		
		self.theme(self.frame, bg=self.hue, fg='#ffffff')

class HackingMenu2(Menu):
	def __init__(self, *args, **kwargs):
		Menu.__init__(self, tearoff=0, *args, **kwargs)

		self.add_command(label="Zeta")
		self.add_command(label="X")
		self.add_separator()
		self.add_command(label="# Scraps")
		self.add_separator()
		#subedit = Menu(self, tearoff=0)
		#self.add_cascade(label="Edit", menu=subedit, command=menu_edit)
		# self.imgterm = Zeta.Image.Icon.Load('termbw', 'bw').image
		# self.add_command(label="Terminal", image=self.imgterm, compound='left', command=lambda: (self.controller.toggle_sidebar(), Zeta.System.OS.terminal(self.fullpath)))
		# self.imgdetach = Zeta.Image.Icon.Load('windowbw', 'bw').image
		# self.add_command(label="Detach", image=self.imgdetach, compound='left', command=self.menu_detach)
		# self.tree.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))
