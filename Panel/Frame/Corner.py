import Zeta
from tkinter import *

class CornerFrame(Canvas):
	def __init__(self, parent, borderwidth=1, relief="flat", color=7, color2='', corner=10, cornerwidth=7):
		Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
		self._color1 = Zeta.Color.Neon(color=color, color2=color2).hex

		self._corner = corner
		self._width = cornerwidth
		self.bind("<Configure>", self._draw_corner)

	def _draw_corner(self, event=None):
		self.delete("corner")
		width = self.winfo_width()
		height = self.winfo_height()
		self.create_line(0,0,self._corner,0, width=self._width, tags=("corner",), fill=self._color1)
		self.create_line(0,0,0,self._corner, width=self._width, tags=("corner",), fill=self._color1)
		self.create_line(width,0,width-self._corner,0, width=self._width, tags=("corner",), fill=self._color1)
		self.create_line(width-1,0,width-1,self._corner, width=self._width, tags=("corner",), fill=self._color1)
		self.create_line(0,height,0,height-self._corner, width=self._width, tags=("corner",), fill=self._color1)
		self.create_line(0,height-1,self._corner,height-1, width=self._width, tags=("corner",), fill=self._color1)
		self.create_line(width-1,height-1,width-1,height-self._corner, width=self._width, tags=("corner",), fill=self._color1)
		self.create_line(width-1,height-1,width-self._corner,height-1, width=self._width, tags=("corner",), fill=self._color1)
		self.lower("corner")

class SampleApp(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.wm_overrideredirect(True)
		corner_frame = CornerFrame(self)
		corner_frame.pack(side="top", fill="both", expand=True)
		inner_frame = Frame(corner_frame)
		inner_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

		b1 = Button(inner_frame, text="Close",command=self.destroy)
		t1 = Text(inner_frame, width=40, height=10)
		b1.pack(side="top")
		t1.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()