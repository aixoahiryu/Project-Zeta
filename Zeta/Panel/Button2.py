import Zeta
from tkinter import *

import os
from natsort import os_sorted

class Button2(Button):
	def __init__(self, master, side='', fill='', relief='flat', hover='', toggle='', geometry='right', anchor='w', anchor2='widget', button='<Button-1>', path='', buffer=[], exclude=[], menucolor='white', textcolor='', listdir=False, *args, **kwargs):
		Button.__init__(self, master, relief=relief, anchor=anchor, *args, **kwargs)
		self.geometry = geometry
		self.menucolor = menucolor
		self.textcolor = self.menucolor if textcolor=='' else Zeta.Color.Neon(textcolor).hex
		rawcolor = Zeta.Color.Neon(color2=menucolor).raw
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw' if ('dark' in rawcolor) else 'hddb', icontype='bw').image
		self.imgtext=Zeta.Image.Icon.Load(icon='textw' if ('dark' in rawcolor) else 'textb', icontype='bw').image

		self.geometry = geometry
		self.path = path
		self.buffer = buffer
		self.exclude = exclude
		self.listdir = listdir
		self.dir = ''

		if side!='': self.pack(side=side, fill=fill)
		if hover!='': Zeta.System.WM.hover_bind(self, hover, geometry=geometry, anchor=anchor2)
		if toggle!='': Zeta.System.WM.toggle_bind(self, toggle, geometry=geometry, anchor=anchor2, button=button)
		
		self.populate(self)
		if path!='': self.bind('<Enter>', lambda e: self.subhover(e.widget), add="+")
		# if path!='': self.bind('<Enter>', lambda e: self.subhover(e.widget))

		# if path!='' or buffer!=[]:
		# 	x = Zeta.Panel.Window(mode='border', color2=self.menucolor)
		# 	# x.neon = '#ffffff' if (self.menucolor not in ['white', 'black']) else x.neon
		# 	self.textcolor = x.neon if textcolor=='' else Zeta.Color.Neon(textcolor).hex
		# 	x.attributes('-topmost', True)
		# 	x.attributes('-alpha', Zeta.Setting.opacityneon)
		# 	self.menu = x

		# 	Zeta.System.WM.hover_bind(self, self.menu, geometry=geometry, anchor=anchor2)
		# 	Zeta.System.WM.toggle_bind(self, self.menu, geometry=geometry, anchor=anchor2, button=button)
		# 	# self.bind('<Button-3>', lambda e: self.sublaunch(Zeta.Panel.Control.FileBox.FilePanel(title='Explorer', home=path, color2=self.menucolor)))
		# 	self.bind('<Button-3>', lambda e: Zeta.Utility.Launch.Explorer(path=path, color=self.menucolor, geometry=Workspace.geometry['sidebar'], transient=self.menu))

		# if buffer!=[]:
		# 	for i in buffer:
		# 		if i=='|': Frame(self.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
		# 		else:
		# 			btn = Button(self.menu.frame, text=i, relief='flat', anchor='w')
		# 			btn.pack(side='top', fill='x')
		# 			# if path!='': btn.bind('<Button-1>', lambda e: self.subbutton(path, e.widget))
		# 	Frame(self.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
		# 	self.menu.theme(self.menu.frame, fg=self.textcolor, bg=x.hue)

		# if path!='':
		# 	path = Zeta.Utility.Format.Path(path)
		# 	if not os.path.exists(path): os.makedirs(path)
		# 	self.dir = os.listdir(path)

		# 	dirlist = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
		# 	filelist = [x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))]
		# 	dirlist = os_sorted(dirlist)
		# 	filelist = os_sorted(filelist)

		# 	if '|' in buffer: buffer.remove('|')
		# 	for i in buffer:
		# 		if not os.path.exists(os.path.join(path, i)):
		# 			if len(i.split('.')) != 1: open(os.path.join(path, i), 'w').close()
		# 			else: os.makedirs(os.path.join(path, i))

		# 	if listdir:
		# 		for i in dirlist: Button(self.menu.frame, text=i, image=self.imghdd, compound='left', relief='flat', anchor='w').pack(side='top', fill='x')
		# 		if len(dirlist)>0: Frame(self.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
		# 		for i in filelist: Button(self.menu.frame, text=i, image=self.imgtext, compound='left', relief='flat', anchor='w').pack(side='top', fill='x')
		# 	self.menu.theme(self.menu.frame, fg=self.textcolor, bg=x.hue)
		# 	self.menu.bind('<Button-1>', lambda e: self.subbutton(path, e.widget))

	def subbutton(self, path, btn):
		if not isinstance(btn, Button): return
		if os.path.exists(f"{path}/{btn['text']}/Ω[ redirect ].txt"):
			with open(f"{path}/{btn['text']}/Ω[ redirect ].txt", encoding='utf-8') as f: path = f.read()
		else: path = f"{path}/{btn['text']}"

		# if os.path.isdir(path): self.sublaunch(Zeta.Panel.Control.FileBox.FilePanel(title=os.path.split(path)[1], home=path, color2=self.menucolor))
		if os.path.isfile(path):
			if path.endswith('.txt'): self.sublaunch(btn, Zeta.Panel.Control.TextBox.TextPanel(title=os.path.split(path)[1], file=path, color2=self.menucolor))
			else: os.startfile(path)

	def sublaunch(self, btn, window):
		# window.tile = [window, self.menu, self.geometry, self]
		# Zeta.System.WM.geocalc(window, self.menu, self.geometry, self)
		#------------------------------------
		window.geometry(f"+{btn.winfo_toplevel().winfo_x()}+{btn.winfo_toplevel().winfo_y()}")
		window.update()
		# Zeta.System.WM.geocalc(window, btn.winfo_toplevel().menuparent, geometry=self.geometry, anchor=btn.winfo_toplevel().menuparent)
		# window.tile = [window, btn, self.geometry, btn]
		Zeta.System.WM.geocalc(window, btn, geometry=self.geometry, anchor=btn)
		if hasattr(window, 'tree'): window.transient(btn.menu)
		elif hasattr(window, 'text'): window.transient(btn.winfo_toplevel())
		window.attributes('-alpha', Zeta.Setting.opacityneon)
		window.attributes('-topmost', True)
		# window.geometry(Workspace.geometry['sidebar'])
		window.show()

	def subhover(self, btn):
		if hasattr(btn, 'dir') and (os.listdir(btn.path)!=btn.dir):
			if (btn.winfo_toplevel().winfo_x()<=btn.winfo_toplevel().winfo_width()) and (btn.geometry=='left'): btn.geometry = 'right'
			if (btn.winfo_toplevel().winfo_x()>=Zeta.System.Size.Screen.width-btn.winfo_toplevel().winfo_width()) and (btn.geometry=='right'): btn.geometry = 'left'

			if hasattr(btn.winfo_toplevel(), 'menuparent') and (btn.winfo_toplevel().menuparent.geometry in ['top', 'bottom']):
				if btn.winfo_toplevel().winfo_x() < (Zeta.System.Size.Screen.width/2): btn.geometry = 'right'
				else: btn.geometry = 'left'
			self.populate(btn)
			btn.menu.update()
			btn.menu.show()

	def populate(self, btn):
		btn.path = Zeta.Utility.Format.Path(btn.path)
		if btn.path!='' or btn.buffer!=[]:
			if hasattr(btn, 'menu'):
				x = btn.menu
				for child in x.frame.winfo_children():
					if hasattr(child, 'menu'): child.menu.destroy()
					child.destroy()
			else: x = Zeta.Panel.Window(mode='border', color2=self.menucolor)
			x.attributes('-topmost', True)
			x.attributes('-alpha', Zeta.Setting.opacityneon)
			btn.menu = x
			btn.menu.menuparent = btn

			Zeta.System.WM.hover_bind(btn, btn.menu, geometry=btn.geometry, anchor=btn)
			Zeta.System.WM.toggle_bind(btn, btn.menu, geometry=btn.geometry, anchor=btn)#, button=button)
			### btn.bind('<Button-3>', lambda e: self.sublaunch(btn, Zeta.Utility.Launch.Explorer(path=btn.path, color=self.menucolor)) )
			btn.bind('<space>', lambda e: self.sublaunch(btn, Zeta.Panel.Control.FileBox.FilePanel(title=os.path.split(btn.path)[1], home=btn.path, color2=self.menucolor)) )
			# btn.bind('<Double-1>', lambda e: Zeta.System.OS.open(btn.path))
			# btn.bind('<Button-3>', lambda e: Zeta.Utility.Dialog.newfile(btn, btn.path, btn.geometry))
			btn.bind('<Button-3>', lambda e: Zeta.Utility.Menu.directory(btn, path=btn.path, geometry=btn.geometry, color=self.menucolor, post=[e.x_root, e.y_root]))

		if btn.buffer!=[]:
			for i in btn.buffer:
				if i=='|': Frame(btn.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
				else:
					btnx = Button(btn.menu.frame, text=i, relief='flat', anchor='w')
					btnx.pack(side='top', fill='x')
					if btn.path!='':
						# btnx.bind('<Button-1>', lambda e: self.subbutton(path, e.widget))
						btnx.geometry = btn.geometry
						btnx.path = f"{btn.path}/{btnx['text']}"
						btnx.buffer = []
						btnx.exclude = []
						btnx.listdir = True

						btnx.bind('<Enter>', lambda e: self.subhover(e.widget))
						btnx.dir = ''
			Frame(btn.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
			btn.menu.theme(btn.menu.frame, fg=self.textcolor, bg=x.hue)

		if btn.path!='':
			if not os.path.exists(btn.path): os.makedirs(btn.path)
			btn.dir = os.listdir(btn.path)
			
			dirlist = [x for x in os.listdir(btn.path) if os.path.isdir(os.path.join(btn.path, x))]
			filelist = [x for x in os.listdir(btn.path) if not os.path.isdir(os.path.join(btn.path, x))]
			dirlist = os_sorted(dirlist)
			filelist = os_sorted(filelist)

			if '|' in btn.buffer: btn.buffer.remove('|')
			for i in btn.buffer:
				if not os.path.exists(os.path.join(btn.path, i)):
					if len(i.split('.')) != 1: open(os.path.join(btn.path, i), 'w').close()
					else: os.makedirs(os.path.join(btn.path, i))

			if btn.listdir:
				# for i in dirlist: Button(btn.menu.frame, text=i, image=self.imghdd, compound='left', relief='flat', anchor='w').pack(side='top', fill='x')
				for i in dirlist:
					btnx = Button(btn.menu.frame, text=i, image=self.imghdd, compound='left', relief='flat', anchor='w')
					btnx.pack(side='top', fill='x')
					btnx.geometry = btn.geometry
					btnx.path = f"{btn.path}/{btnx['text']}"
					btnx.buffer = []
					btnx.exclude = []
					btnx.listdir = True

					btnx.bind('<Enter>', lambda e: self.subhover(e.widget))
					btnx.dir = ''
				if len(dirlist)>0: Frame(btn.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
				for i in filelist: Button(btn.menu.frame, text=i, image=self.imgtext, compound='left', relief='flat', anchor='w').pack(side='top', fill='x')
			btn.menu.theme(btn.menu.frame, fg=self.textcolor, bg=x.hue)
			btn.menu.bind('<Button-1>', lambda e: self.subbutton(btn.path, e.widget))