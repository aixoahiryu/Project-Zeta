import Zeta
from Zeta.Panel import *

class CodeMenu(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image

		btnzeta = Button2(self.frame, text=' Zeta', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.ZETA), side='top', fill='x')
		Button2(self.frame, text=' X', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X), side='top', fill='x')
		Frame2(self.frame, highlightbackground=self.neon, highlightthickness=1, side='top', fill='x')
		Button2(self.frame, text=' ZL-Core', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<Downstream>'), side='top', fill='x')
		Frame2(self.frame, highlightbackground=self.neon, highlightthickness=1, side='top', fill='x')
		Button2(self.frame, text=' Project', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Project ]'), side='top', fill='x')
		Button2(self.frame, text=' Sandbox', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.Utility.Launch.Explorer(geometry=Workspace.geometry['sidebar'], transient=Workspace.panel[Workspace.active]['root'], path='<X>/Void/[ Sandbox ]'), side='top', fill='x')
		Frame2(self.frame, highlightbackground=self.neon, highlightthickness=1, side='top', fill='x')

		self.theme(self.frame, bg=self.hue, fg='#ffffff')

		btnzeta.bind('<Button-3>', lambda e: Zeta.System.OS.edit('<Zeta>'))