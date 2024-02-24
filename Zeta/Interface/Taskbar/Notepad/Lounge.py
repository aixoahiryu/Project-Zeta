import Zeta
from Zeta.Panel import *

class Lounge(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.geometry(f"{Zeta.System.Size.Window.side[0]}x20-0+0")
		self.overrideredirect(1)

		appframe = Frame(self)
		appframe.pack(side='right', fill='y')
		Button2(appframe, text='Entertainment', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Lounge/Entertainment')
		Button2(appframe, text='Furry', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Lounge/Furry')
		Frame2(appframe, side='left', fill='y', highlightthickness=1, highlightcolor='#ffffff')
		Button2(appframe, text='Explore', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Lounge/Explore')
		Button2(appframe, text='Flow', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Lounge/Flow')
		Frame2(self, side='right', fill='y', highlightthickness=1, highlightcolor='#c9c9c9')
		Button2(self, text='Lounge', side='left', fill='both', width=55, anchor='center', relief='flat', geometry='left', listdir=True, path='<X>/Matter/Quick/Lounge').bind("<Button-3>", lambda event: Workspace.notepadmenu.post(event.x_root, event.y_root))

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)
		self.color2 = 'white'