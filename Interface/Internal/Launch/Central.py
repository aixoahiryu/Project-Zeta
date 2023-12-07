import Zeta
from Zeta.Panel import *

class Central(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.attributes('-topmost', True)
		self.geometry(Zeta.System.Size.geometry['main'])

		notebook = Notebook(self.frame)
		notebook.enable_traversal()
		notebook.pack(fill='both')
		frame0 = Frame(notebook)
		frame1 = Frame(notebook)
		frame2 = Frame(notebook)
		frame3 = Frame(notebook)
		frame0.pack(fill='both')
		frame1.pack(fill='both')
		frame2.pack(fill='both')
		frame3.pack(fill='both')

		notebook.add(frame0, text='Analysis')
		notebook.add(frame1, text='Task')
		notebook.add(frame2, text='Service')
		notebook.add(frame3, text='Raw')

		Button(frame1, text='Temp').pack()
		Button(frame1, text='MV').pack()
		Button(frame2, text='MP3').pack()

		self.theme(self.frame, bg='#ffffff', fg='#000000')