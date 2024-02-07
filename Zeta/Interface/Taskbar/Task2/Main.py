import Zeta
from Zeta.Panel import *

class Task2(Toplevel):
	def __init__(self, *args, **kwargs):
		# Window.__init__(self, mode='border', color2=Workspace.color.colorname, *args, **kwargs)
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.geometry(f"+0+0")
		self.overrideredirect(1)
		self.imgtab=Zeta.Image.Icon.Load(icon='tabw', icontype='bw').image


		appframe = Frame(self)
		appframe.pack(side='left', fill='y')
		Button2(appframe, text='[ Core ]', relief='flat', image=self.imgtab, compound='left', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Tab/CORE')
		Frame2(appframe, side='left', fill='y', highlightthickness=1, highlightcolor='#c9c9c9')
		Button2(appframe, text='Social', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Tab/Social')
		Button2(appframe, text='Local', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Tab/Local')
		Button2(appframe, text='Remote', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Tab/Remote')

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)
		self.color2 = 'white'