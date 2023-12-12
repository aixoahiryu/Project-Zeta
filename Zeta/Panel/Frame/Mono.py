import Zeta
from tkinter import *

class MonoFrame(Canvas):
	'''A gradient frame which uses a canvas to draw the background'''
	def __init__(self, parent, borderwidth=1, relief="flat", color=7, color2=''):
		Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief)
		self._color1 = Zeta.Color.Neon(color=color, color2=color2).hex
		self._color2 = Zeta.Color.Neon(color=color, color2=color2).hex
		self.bind("<Configure>", self._draw_gradient)

	def _draw_gradient(self, event=None):
		'''Draw the gradient'''
		self.delete("gradient")
		width = self.winfo_width()
		height = self.winfo_height()
		limit = width
		(r1,g1,b1) = self.winfo_rgb(self._color1)
		(r2,g2,b2) = self.winfo_rgb(self._color2)
		r_ratio = float(r2-r1) / limit
		g_ratio = float(g2-g1) / limit
		b_ratio = float(b2-b1) / limit

		for i in range(limit):
			nr = int(r1 + (r_ratio * i))
			ng = int(g1 + (g_ratio * i))
			nb = int(b1 + (b_ratio * i))
			color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
			self.create_line(i,0,i,height, tags=("gradient",), fill=color)
		self.lower("gradient")

class SampleApp(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.wm_overrideredirect(True)
		gradient_frame = MonoFrame(self)
		gradient_frame.pack(side="top", fill="both", expand=True)
		inner_frame = Frame(gradient_frame)
		inner_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

		b1 = Button(inner_frame, text="Close",command=self.destroy)
		t1 = Text(inner_frame, width=40, height=10)
		b1.pack(side="top")
		t1.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
	app = SampleApp()
	app.mainloop()