import Zeta
from Zeta.Panel import *

class Dial(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.attributes('-topmost', True)
		self.geometry(Zeta.System.Size.geometry['npp'])

		notebook = Notebook(self.frame)
		notebook.enable_traversal()
		notebook.pack(fill='both')
		frame0 = Frame(notebook)
		frame1 = Frame(notebook)
		frame0.pack(fill='both')
		frame1.pack(fill='both')

		notebook.add(frame0, text='Sephiroth')
		notebook.add(frame1, text='Journal')

		Button(frame0, text='Temp').pack()
		Button(frame0, text='MV').pack()
		Button(frame1, text='MP3').pack()

		self.theme(self.frame, bg='#ffffff', fg='#000000')