import Zeta
from Zeta.Panel import *

class FileMenu(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.imglink=Zeta.Image.Icon.Load(icon='linkw', icontype='bw').image
		self.imgblock=Zeta.Image.Icon.Load(icon='blockw', icontype='bw').image
		self.imglock=Zeta.Image.Icon.Load(icon='lockw', icontype='bw').image

		Button(self.frame, text=' # Scraps', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/# Scraps')).pack(side='top', fill='x')
		Button(self.frame, text=' [ Case ]', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ File ]/[ Case ]')).pack(side='top', fill='x')
		Button(self.frame, text=' [ Note ]', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ File ]/[ Note ]')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(self.frame, text=' [ Directory ]', relief='flat', image=self.imglink, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ File ]/[ Directory ]')).pack(side='top', fill='x')
		Button(self.frame, text=' [ Cluster ]', relief='flat', image=self.imgblock, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Cluster ]')).pack(side='top', fill='x')
		Button(self.frame, text=' [ Encrypt ]', relief='flat', image=self.imglock, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Encrypt ]')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(self.frame, text='bk', relief='flat', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X+r'/Void/Upload')).pack(side='top', fill='x')
		Button(self.frame, text='Git', relief='flat', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X+r'/Void/Upload')).pack(side='top', fill='x')
		Button(self.frame, text='Raw', relief='flat', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X+r'/Void/Upload')).pack(side='top', fill='x')
		Button(self.frame, text='Scraps', relief='flat', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<Scraps>')).pack(side='top', fill='x')
		Button(self.frame, text='tree', relief='flat', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/# Scraps/# Raw/╬ Void/tree')).pack(side='top', fill='x')
		Button(self.frame, text='Upload', relief='flat', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Network ]/Upload')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		
		self.theme(self.frame, bg=self.hue, fg='#ffffff')

class FileMenu2(Menu):
	def __init__(self, *args, **kwargs):
		Menu.__init__(self, tearoff=0, *args, **kwargs)

		self.add_command(label="Zeta", command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.ZETA))
		self.add_command(label="X", command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X))
		self.add_separator()
		self.add_command(label="# Scraps")
		self.add_separator()
		#subedit = Menu(self, tearoff=0)
		#self.add_cascade(label="Edit", menu=subedit, command=menu_edit)
		# self.imgterm = Zeta.Image.Icon.Load('termbw', 'bw').image
		# self.add_command(label="Terminal", image=self.imgterm, compound='left', anchor='w', command=lambda: (self.controller.toggle_sidebar(), Zeta.System.OS.terminal(self.fullpath)))
		# self.imgdetach = Zeta.Image.Icon.Load('windowbw', 'bw').image
		# self.add_command(label="Detach", image=self.imgdetach, compound='left', anchor='w', command=self.menu_detach)
		# self.tree.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))
