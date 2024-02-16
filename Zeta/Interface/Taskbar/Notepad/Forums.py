import Zeta
from Zeta.Panel import *

class Forums(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.geometry(f"{Zeta.System.Size.Window.side[0]}x20-0+0")
		self.overrideredirect(1)

		appframe = Frame(self)
		appframe.pack(side='right', fill='y')
		Button2(appframe, text='Root', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Forums/Root')
		Button2(appframe, text='Thread', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Forums/Thread')
		Button2(appframe, text='Scraps', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Forums/Scraps')
		Button2(appframe, text='Resource', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Forums/Resource')
		Button2(appframe, text='Anti', relief='flat', side='left', fill='y', geometry='bottom', listdir=True, path='<X>/Matter/Task/Forums/Anti')
		Frame2(self, side='right', fill='y', highlightthickness=1, highlightcolor='#c9c9c9')
		Button2(self, text='Forums', side='left', fill='both', width=55, anchor='center', relief='flat', geometry='bottom', listdir=True, path='<X>/Matter/Quick/Forums').bind("<Button-3>", lambda event: Workspace.notepadmenu.post(event.x_root, event.y_root))

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)
		self.color2 = 'white'