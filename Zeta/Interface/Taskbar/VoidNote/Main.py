import Zeta
from tkinter import *
from Zeta.Panel import *

class VoidNote(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.geometry(f"{Zeta.System.Size.Window.side[0]}x20-0+20")
		self.overrideredirect(1)
		self.imgplay=Zeta.Image.Icon.Load(icon='playw', icontype='bw').image
		self.imgbrowser=Zeta.Image.Icon.Load(icon='cornerw', icontype='bw').image

		appframe = Frame(self)
		appframe.pack(side='right', fill='y')
		Button2(appframe, text='', relief='raised', image=self.imgplay, compound='left', side='left', fill='y')
		Button2(appframe, text='', relief='raised', image=self.imgbrowser, compound='left', side='left', fill='y')
		self.searchbox = Entry(self)
		self.searchbox.pack(side='left', fill='both')
		self.searchbox.bind('<Return>', lambda e: self.search())
		self.searchbox.bind('<Enter>', lambda e: self.focused())
		self.searchbox.bind('<Button-3>', lambda e: self.rightclick())

		self.searchbox2 = Entry(self)
		self.searchbox2.pack(side='left', fill='both')

		self.theme(self, bg=Workspace.color.hue, fg=Workspace.color.hex)
		self.color2 = 'white'

	def search(self):
		Zeta.Utility.Launch.Editor(path=f"<X>/Matter/Task/VoidNote/{self.searchbox.get()}.txt", color='white', geometry=Zeta.System.Size.geometry['npp'], title=f"{self.searchbox.get()}.txt")

	def focused(self):
		self.searchbox.focus()
		self.searchbox.selection_range(0, END)

	def rightclick(self):
		Zeta.System.OS.edit('<X>/Matter/Task/VoidNote')