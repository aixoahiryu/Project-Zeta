import Zeta
from tkinter import *

class Label2(Label):
	def __init__(self, master, side='', fill='', *args, **kwargs):
		Label.__init__(self, master, *args, **kwargs)
		if side!='': self.pack(side=side, fill=fill)