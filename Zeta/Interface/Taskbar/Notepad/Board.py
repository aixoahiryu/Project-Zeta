import Zeta
from Zeta.Panel import *

class Board(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.geometry(f"{Zeta.System.Size.Window.side[0]}x20-0+0")
		self.overrideredirect(1)
		self.imgbrain=Zeta.Image.Icon.Load(icon='brainw', icontype='bw').image
		self.imgram=Zeta.Image.Icon.Load(icon='ramw', icontype='bw').image
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image

		appframe = Frame(self)
		appframe.pack(side='right', fill='y')
		Button2(appframe, text='Mind', relief='flat', image=self.imgbrain, compound='left', side='left', fill='y', geometry='bottom', listdir=True, path='<Scraps>/filter/[ Mind ]')
		Button2(appframe, text='File', relief='flat', image=self.imghdd, compound='left', side='left', fill='y', geometry='bottom', listdir=True, path='<Scraps>/filter/[ File ]')
		Button2(appframe, text='Network', relief='flat', image=self.imgram, compound='left', side='left', fill='y', geometry='bottom', listdir=True, path='<Scraps>/filter/[ Network ]')
		Frame2(self, side='right', fill='y', highlightthickness=1, highlightcolor='#c9c9c9')
		Label2(self, text='Board', side='right', fill='both', width=33).bind("<Button-3>", lambda event: Workspace.notepadmenu.post(event.x_root, event.y_root))

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)
		self.color2 = 'white'