import Zeta
from Zeta.Panel import *

class CodeMenu(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image

		Button(self.frame, text=' Zeta', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.ZETA)).pack(side='top', fill='x')
		Button(self.frame, text=' X', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X)).pack(side='top', fill='x')
		Button(self.frame, text=' ZL-Core', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<Downstream>')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(self.frame, text=' Project', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Project ]')).pack(side='top', fill='x')
		Button(self.frame, text=' Sandbox', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Sandbox ]')).pack(side='top', fill='x')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')

		self.theme(self.frame, bg=self.hue, fg='#ffffff')