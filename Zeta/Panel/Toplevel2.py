import Zeta
from tkinter import *

class Toplevel2(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		if Zeta.Setting.antifragment: self.attributes('-alpha', 0.99)
		
		self.child = []
		self.owner = []
		self.visible = True
		self.tile = []
		#self.protocol( 'WM_DELETE_WINDOW' , self.close)

		self.data = {'token': ''}
		self.control = {'self': self}
		self.function = {'Right-click drag': self.bind_rightclick}
		self.context = {'action': ''}

		self.transcended = False
		if Zeta.Setting.lazyload: self.hide()

	def hide(self):
		self.withdraw()
		self.visible = False
		if self.transcended:
			self.overrideredirect(False)
			self.iconify()

		for w in self.child:
			try: w.hide()
			except: print('hide() failed')
		self.event_generate("<<hide>>", when="tail")

	def show(self, geometry=''):
		if self.tile!=[]:
			if isinstance(self.tile, Toplevel): self.geometry(self.tile.geometry())
			else: Zeta.System.WM.geocalc(self.tile[0], self.tile[1], self.tile[2], self.tile[3])
		if geometry!='': self.geometry(geometry)

		self.deiconify()
		self.visible = True

		for w in self.child:
			try: w.show()
			except: print('show() failed')
		self.event_generate("<<show>>", when="tail")

	def close(self):
		for w in self.child: w.close()
		for w in self.owner: w.child.remove(self)
		self.destroy()

	def transient(self, master):
		self.owner.append(master)
		master.child.append(self)

	def orphan(self):
		for w in self.owner: w.child.remove(self)
		self.owner = []

	def adopt(self, master):
		self.orphan()
		self.transient(master)

	def transcend(self):
		self.orphan()
		self.bind('<Expose>', lambda e: self.overrideredirect(True))
		self.attributes('-topmost', False)
		self.transcended = True

	# def theme(self, bg='#000000', fg='#ffffff'):
	# 	for c in self.control:
	# 		if hasattr(c, 'background'): c['background'] = bg
	# 		if hasattr(c, 'foreground'): c['foreground'] = fg

	def theme(self, target, bg='#000000', fg='#ffffff', relief=''):
		# for b in filter(lambda w:isinstance(w,Button), target.children.itervalues()):
		try: 
			target['background'] = bg
			target['foreground'] = fg
			if relief!='': target.configure(relief=relief)
			# if relief!='' and isinstance(target,Button): target['relief']=relief
		except Exception as error: print(error)
		for c in target.children.values(): self.theme(c, bg, fg, relief)


	def start_move(self, event):
		self.x = event.x
		self.y = event.y

	def stop_move(self, event):
		self.x = None
		self.y = None
		x = self.winfo_x() - (self.winfo_x() % 10)
		y = self.winfo_y() - (self.winfo_y() % 10)
		self.geometry(f"+{x}+{y}")

	def do_move(self, event):
		deltax = event.x - self.x
		deltay = event.y - self.y
		x = self.winfo_x() + deltax
		y = self.winfo_y() + deltay
		self.geometry(f"+{x}+{y}")

	def bind_rightclick(self):
		self.bind("<ButtonPress-3>", self.start_move)
		self.bind("<ButtonRelease-3>", self.stop_move)
		self.bind("<B3-Motion>", self.do_move)

	def resize(self, direction):
		height = self.winfo_height()
		width = self.winfo_width()
		if direction=='Up': height-=50
		if direction=='Down': height+=50
		if direction=='Left': width-=50
		if direction=='Right': width+=50
		self.geometry(f"{width}x{height}")

	def bind_drag(self, control):
		control.bind("<ButtonPress-1>", self.start_move)
		control.bind("<ButtonRelease-1>", self.stop_move)
		control.bind("<B1-Motion>", self.do_move)

		# if Zeta.System.OS.Windows:
		# 	self.bind("<Alt-ButtonPress-1>", self.start_move)
		# 	self.bind("<Alt-ButtonRelease-1>", self.stop_move)
		# 	self.bind("<Alt-B1-Motion>", self.do_move)

		self.bind("<Alt-Up>", lambda e: self.resize('Up'))
		self.bind("<Alt-Down>", lambda e: self.resize('Down'))
		self.bind("<Alt-Left>", lambda e: self.resize('Left'))
		self.bind("<Alt-Right>", lambda e: self.resize('Right'))