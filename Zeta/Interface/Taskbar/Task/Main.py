import Zeta
from Zeta.Panel import *

class Task(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.geometry(f"+0-{Zeta.System.Size.taskbar}")
		self.overrideredirect(1)
		self.imgbrain=Zeta.Image.Icon.Load(icon='brainw', icontype='bw').image
		self.imgram=Zeta.Image.Icon.Load(icon='ramw', icontype='bw').image
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image

		appframe = Frame(self)
		appframe.pack(side='left', fill='y')
		Button2(appframe, text='Mind', relief='flat', image=self.imgbrain, compound='left', side='left', fill='y', geometry='top', listdir=True, path='<Scraps>/filter/[ Mind ]')
		Button2(appframe, text='File', relief='flat', image=self.imghdd, compound='left', side='left', fill='y', geometry='top', listdir=True, path='<Scraps>/filter/[ File ]')
		Button2(appframe, text='Network', relief='flat', image=self.imgram, compound='left', side='left', fill='y', geometry='top', listdir=True, path='<Scraps>/filter/[ Network ]')
		Frame2(appframe, side='left', fill='y', highlightthickness=1, highlightcolor='#c9c9c9')
		Label(appframe, text='Filter', width=33).pack(side='left', fill='y')

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)
		self.color2 = 'white'