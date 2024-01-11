import Zeta
from Zeta.Panel import *

class Bridge(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		width = Zeta.System.Size.Screen.width
		height = 25
		self.geometry(f"{width}x{height}+0+1")
		self.overrideredirect(1)
		#self.configure(bg=colorbg, bd=1, relief='groove')
		Label(self, text=r'[ Workspace ]').place(relx=0.48, rely=0)

		appframe = Frame(self)
		appframe.pack(side='left', fill='y')
		#Button(appframe, text='1', relief='flat', background='#3c3c3c').grid(column=0, row=0, sticky='NW')
		Button(appframe, text='1', relief='flat', foreground='#6effbe').grid(column=0, row=0, sticky='NW')
		Button(appframe, text='2', relief='flat').grid(column=1, row=0, sticky='NW')
		Button(appframe, text='3', relief='flat').grid(column=2, row=0, sticky='NW')
		Button(appframe, text='4', relief='flat').grid(column=3, row=0, sticky='NW')
		Button(appframe, text='#', relief='flat').grid(column=4, row=0, sticky='NW')

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)