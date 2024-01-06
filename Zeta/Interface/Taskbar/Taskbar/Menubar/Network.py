import Zeta
from Zeta.Panel import *

class NetworkMenu(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.imgtab=Zeta.Image.Icon.Load(icon='tabw', icontype='bw').image
		self.imghis=Zeta.Image.Icon.Load(icon='historyw', icontype='bw').image
		self.imgsocial=Zeta.Image.Icon.Load(icon='socialw', icontype='bw').image
		self.imgprofile=Zeta.Image.Icon.Load(icon='profilew', icontype='bw').image
		self.imgtext=Zeta.Image.Icon.Load(icon='textw', icontype='bw').image

		Button(self.frame, text=' [ Tab ]', relief='flat', image=self.imgtab, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Network ]/[ Tab ]')).pack(side='top', fill='x')
		Button(self.frame, text=' [ History ]', relief='flat', image=self.imghis, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Network ]/[ History ]')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(self.frame, text=' [ Social ]', relief='flat', image=self.imgsocial, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Network ]/[ Social ]')).pack(side='top', fill='x')
		Button(self.frame, text=' [ Profile ]', relief='flat', image=self.imgprofile, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Network ]/[ Profile ]')).pack(side='top', fill='x')
		Button(self.frame, text=' [ Message ]', relief='flat', image=self.imgtext, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Network ]/[ Message ]')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(self.frame, text=' Ω[ ≡ Static ]', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Network ]/≡ Static')).pack(side='top', fill='x')
		Button(self.frame, text=' Ω[ † Public ]', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Network ]/† Public')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')

		self.theme(self.frame, bg=self.hue, fg='#ffffff')

class NetworkMenu2(Menu):
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
