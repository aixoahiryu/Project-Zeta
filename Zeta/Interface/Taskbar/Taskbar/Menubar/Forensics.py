import Zeta
from Zeta.Panel import *

class ForensicsMenu(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.imgintercept=Zeta.Image.Icon.Load(icon='eye2w', icontype='bw').image
		self.imgrecon=Zeta.Image.Icon.Load(icon='systemw', icontype='bw').image
		self.imgexploit=Zeta.Image.Icon.Load(icon='debugw', icontype='bw').image

		Button2(self.frame, text=' Case', relief='flat', image=self.imghdd, compound='left', anchor='w', buffer=['maltego', 'encase'], side='top', fill='x')
		Button2(self.frame, text=' Framework', relief='flat', image=self.imghdd, compound='left', anchor='w', side='top', fill='x')
		Button2(self.frame, text=' Tools', relief='flat', image=self.imghdd, compound='left', anchor='w', buffer=['OS', 'Program', 'File[extract, recovery, steal]'], side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(self.frame, text=' Machine', relief='flat', image=self.imghdd, compound='left', anchor='w', side='top', fill='x')
		Button2(self.frame, text=' OSINT', relief='flat', image=self.imghdd, compound='left', anchor='w', side='top', fill='x')
		Button2(self.frame, text=' Biology', relief='flat', image=self.imghdd, compound='left', anchor='w', buffer=['phenotype', 'database', 'genetic', 'name'], side='top', fill='x')
		Button2(self.frame, text=' Psychology', relief='flat', image=self.imghdd, compound='left', anchor='w', side='top', fill='x')
		Button2(self.frame, text=' Technical', relief='flat', image=self.imghdd, compound='left', anchor='w', buffer=['electrical', 'material', 'lingustics', 'fire'], side='top', fill='x')
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
