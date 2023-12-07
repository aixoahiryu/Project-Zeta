import Zeta
from Zeta.Panel import *

class Launch(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='white', *args, **kwargs)

		self.theme(self.frame, bg='#ffffff', fg='#000000')


if __name__ == "__main__":
    app = Launch(mode='basic', color2='black')
    app.mainloop()