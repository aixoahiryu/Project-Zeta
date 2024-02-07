import Zeta
from Zeta.Panel import *

class Resource(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.geometry(f"{Zeta.System.Size.Window.side[0]}x25-0-{Zeta.System.Size.taskbar}")
		self.overrideredirect(1)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image

		appframe = Frame(self)
		appframe.pack(side='right', fill='y')
		Button2(appframe, text='Ω[  ]', relief='raised', side='right', fill='y', geometry='top', listdir=True, path='<Resource>/Matter/Ω[  ]')
		Button2(appframe, text='Σ[  ]', relief='raised', side='right', fill='y', geometry='top', listdir=True, path='<Resource>/Matter/Σ[  ]')
		Button2(appframe, text='Δ[  ]', relief='raised', side='right', fill='y', geometry='top', listdir=True, path='<Resource>/Matter/Δ[  ]')
		Button2(appframe, text='Temp', relief='raised', image=self.imghdd, compound='left', side='right', fill='y', geometry='top', listdir=True, path='<Resource>/Matter/Temp')
		Button2(self, text='Resource', side='left', fill='both', width=55, anchor='center', relief='flat', geometry='top', listdir=True, path='<X>/Matter/Task/Resource')

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)
		self.color2 = 'white'