import Zeta
from Zeta.Panel import *

class Console(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.attributes('-topmost', True)
		self.geometry(Zeta.System.Size.geometry['aimp'])

		self.theme(self.frame, bg='#ffffff', fg='#000000')