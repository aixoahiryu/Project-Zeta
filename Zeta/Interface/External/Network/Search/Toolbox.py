import Zeta
from Zeta.Panel import *

class Toolbox(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='white', *args, **kwargs)
		left = 25 +5
		bottom = Zeta.System.Size.taskbar + 25 +5
		height = Zeta.System.Size.Screen.height - bottom - 333 - 25 -5
		self.geometry(f'333x{height}+{left}-{bottom}')
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacity)

		notebook = Notebook(self.frame)
		notebook.enable_traversal()
		notebook.pack(fill='both')

		fintercept = Frame(notebook)
		fintercept.pack(fill='both')
		fdriver = Frame(notebook)
		fdriver.pack(fill='both')
		fserver = Frame(notebook)
		fserver.pack(fill='both')
		
		notebook.add(fintercept, text='Intercept')
		notebook.add(fdriver, text='Driver')
		notebook.add(fserver, text='Server')

		self.theme(self.frame, bg='#000000', fg='#ffffff')