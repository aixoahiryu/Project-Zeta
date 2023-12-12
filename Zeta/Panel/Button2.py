import Zeta
from tkinter import *

import os
from natsort import os_sorted

class Button2(Button):
	def __init__(self, master, side='', fill='', relief='flat', hover='', toggle='', geometry='right', anchor='w', anchor2='widget', button='<Button-1>', path='', buffer=[], exclude=[], menucolor='white', textcolor='', listdir=False, *args, **kwargs):
		Button.__init__(self, master, relief=relief, anchor=anchor, *args, **kwargs)
		self.geometry = geometry
		self.menucolor = menucolor
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.imgtext=Zeta.Image.Icon.Load(icon='textw', icontype='bw').image

		if side!='': self.pack(side=side, fill=fill)
		if hover!='': Zeta.System.WM.hover_bind(self, hover, geometry=geometry, anchor=anchor2)
		if toggle!='': Zeta.System.WM.toggle_bind(self, toggle, geometry=geometry, anchor=anchor2, button=button)

		if path!='' or buffer!=[]:
			x = Zeta.Panel.Window(mode='border', color2=self.menucolor)
			# x.neon = '#ffffff' if (self.menucolor not in ['white', 'black']) else x.neon
			self.textcolor = x.neon if textcolor=='' else Zeta.Color.Neon(textcolor).hex
			x.attributes('-topmost', True)
			x.attributes('-alpha', Zeta.Setting.opacityneon)
			self.menu = x

			Zeta.System.WM.hover_bind(self, self.menu, geometry=geometry, anchor=anchor2)
			Zeta.System.WM.toggle_bind(self, self.menu, geometry=geometry, anchor=anchor2, button=button)
			# self.bind('<Button-3>', lambda e: self.sublaunch(Zeta.Panel.Control.FileBox.FilePanel(title='Explorer', home=path, color2=self.menucolor)))
			self.bind('<Button-3>', lambda e: Zeta.Utility.Launch.Explorer(path=path, color=self.menucolor, geometry=Workspace.geometry['sidebar'], transient=self.menu))

		if buffer!=[]:
			for i in buffer:
				if i=='|': Frame(self.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
				else:
					btn = Button(self.menu.frame, text=i, relief='flat', anchor='w')
					btn.pack(side='top', fill='x')
					# if path!='': btn.bind('<Button-1>', lambda e: self.subbutton(path, e.widget))
			Frame(self.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
			self.menu.theme(self.menu.frame, fg=self.textcolor, bg=x.hue)

		if path!='':
			path = Zeta.Utility.Format.Path(path)
			if not os.path.exists(path): os.makedirs(path)
			dirlist = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
			filelist = [x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))]
			dirlist = os_sorted(dirlist)
			filelist = os_sorted(filelist)

			if '|' in buffer: buffer.remove('|')
			for i in buffer:
				if not os.path.exists(os.path.join(path, i)):
					if len(i.split('.')) != 1: open(os.path.join(path, i), 'w').close()
					else: os.makedirs(os.path.join(path, i))

			if listdir:
				for i in dirlist: Button(self.menu.frame, text=i, image=self.imghdd, compound='left', relief='flat', anchor='w').pack(side='top', fill='x')
				if len(dirlist)>0: Frame(self.menu.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
				for i in filelist: Button(self.menu.frame, text=i, image=self.imgtext, compound='left', relief='flat', anchor='w').pack(side='top', fill='x')
			self.menu.theme(self.menu.frame, fg=self.textcolor, bg=x.hue)
			self.menu.bind('<Button-1>', lambda e: self.subbutton(path, e.widget))

	def subbutton(self, path, btn):
		if not isinstance(btn, Button): return
		if os.path.exists(f"{path}/{btn['text']}/Ω[ redirect ].txt"):
			with open(f"{path}/{btn['text']}/Ω[ redirect ].txt", encoding='utf-8') as f: path = f.read()
		else: path = f"{path}/{btn['text']}"

		if os.path.isdir(path): self.sublaunch(Zeta.Panel.Control.FileBox.FilePanel(title=os.path.split(path)[1], home=path, color2=self.menucolor))
		elif os.path.isfile(path): self.sublaunch(Zeta.Panel.Control.TextBox.TextPanel(title=os.path.split(path)[1], file=path, color2=self.menucolor))

	def sublaunch(self, window):
		# window.tile = [window, self.menu, self.geometry, self]
		# Zeta.System.WM.geocalc(window, self.menu, self.geometry, self)
		window.update()
		Zeta.System.WM.geocalc(window, self, geometry=self.geometry, anchor=self)
		window.transient(self.menu)
		window.attributes('-alpha', Zeta.Setting.opacityneon)
		window.attributes('-topmost', True)
		# window.geometry(Workspace.geometry['sidebar'])
		window.show()