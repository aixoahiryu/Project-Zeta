import Zeta
from Zeta.Panel import *

class Debug(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='white', *args, **kwargs)
		home = r'D:\MEGA\ZL-Core\Commit\╬'
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacity)
		height = Zeta.System.Size.Window.mpv[1]
		self.geometry(f"333x{height}+30-{Zeta.System.Size.taskbar}")

		notebook = Notebook(self.frame)
		notebook.enable_traversal()
		notebook.pack(fill='both')

		finfo = Frame(notebook)
		finfo.pack(fill='both')
		ftoolbox = Frame(notebook)
		ftoolbox.pack(fill='both')
		fevent = Frame(notebook)
		fevent.pack(fill='both')
		fconsole = Frame(notebook)
		fconsole.pack(fill='both')
		
		notebook.add(finfo, text='Info')
		notebook.add(ftoolbox, text='Toolbox')
		notebook.add(fevent, text='Event')
		notebook.add(fconsole, text='Console')

		self.theme(self.frame, bg='#000000', fg='#ffffff')