import Zeta
from Zeta.Panel import *

class Overflow(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.title('Icon overflow')
		self.geometry("-0+25")
		self.overrideredirect(1)
		self.configure()
		#self.transient(taskbar)
		self.attributes('-topmost', True)
		self.imggemini=Zeta.Image.Icon.Load(icon='geminiw', icontype='bw').image
		Button(self, text=' Thaumiel', relief='flat', image=self.imggemini, compound='left').grid(column=0, row=0, sticky='NW')
		self.imgeye=Zeta.Image.Icon.Load(icon='eye2w', icontype='bw').image
		Button(self, text=' The eye', relief='flat', image=self.imgeye, compound='left').grid(column=0, row=1, sticky='NW')
		self.imgmoon=Zeta.Image.Icon.Load(icon='moonw', icontype='bw').image
		Button(self, text=' Moon cycle', relief='flat', image=self.imgmoon, compound='left').grid(column=0, row=2, sticky='NW')
		self.imgsun=Zeta.Image.Icon.Load(icon='sunw', icontype='bw').image
		Button(self, text=' Sun cycle', relief='flat', image=self.imgsun, compound='left').grid(column=0, row=3, sticky='NW')
		self.imgdice=Zeta.Image.Icon.Load(icon='dicew', icontype='bw').image
		Button(self, text=' Chaos theory', relief='flat', image=self.imgdice, compound='left').grid(column=0, row=4, sticky='NW')
		self.imgcalendar=Zeta.Image.Icon.Load(icon='calendarw', icontype='bw').image
		Button(self, text=' Calendar', relief='flat', image=self.imgcalendar, compound='left').grid(column=0, row=5, sticky='NW')
		self.imghorse=Zeta.Image.Icon.Load(icon='horsew', icontype='bw').image
		Button(self, text=' Strategy', relief='flat', image=self.imghorse, compound='left').grid(column=0, row=6, sticky='NW')
		self.imgwave=Zeta.Image.Icon.Load(icon='wave2w', icontype='bw').image
		Button(self, text=' Flunctuation', relief='flat', image=self.imgwave, compound='left').grid(column=0, row=7, sticky='NW')

		self.theme(self, bg='#000000', fg='#c9c9c9')