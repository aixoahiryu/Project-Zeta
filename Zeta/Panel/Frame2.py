import Zeta
from tkinter import *

class Frame2(Frame):
	def __init__(self, master, side='', fill='', *args, **kwargs):
		Frame.__init__(self, master, *args, **kwargs)
		if side!='': self.pack(side=side, fill=fill)