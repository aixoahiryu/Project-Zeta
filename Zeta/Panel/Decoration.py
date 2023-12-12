import Zeta
from tkinter import *

class Basic(Frame):
	def __init__(self, master, title='Title', color=7, color2='', safemode=False):
		self.neon = Zeta.Color.Neon(color=color, color2=color2).hex
		self.hue = Zeta.Color.Neon(color=color, color2=color2).hue
		self.fgcolor = Zeta.Color.Neon(color=color, color2=color2).fgcolor
		self.raw = Zeta.Color.Neon(color=color, color2=color2).raw

		Frame.__init__(self, master, background=self.hue)
		top = Frame(self, background=self.hue)
		top.pack(side='top', fill=X)
		top.grid_columnconfigure(0, weight=1)
		#body = Frame(self)
		self.winfo_toplevel().decoration = self
		
		msg = Label(top, wraplength='4i', justify=LEFT, foreground=self.neon, background=self.hue, font=("Courier New", 10, "normal"))
		msg['text'] = title
		msg.grid(row=0, column=0, sticky='NW')
		btnframe = Frame(top, background=self.hue)
		btnframe.grid(row=0, column=1, sticky='E')

		mono = True if ('mono' in self.raw) else False
		self.geometry = Workspace.geometry['main'] if hasattr(__builtins__, 'Workspace') else f"{Zeta.System.Size.Screen.width}x{Zeta.System.Size.Screen.height}+0+0"
		self.maximized = False
		self.safemode = safemode
		Button(btnframe, text=u'Ζ', relief='flat', foreground=self.fgcolor, background=self.hue, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().transcend).pack(side='left')
		Button(btnframe, text=u'Α', relief='flat', foreground=self.fgcolor, background=self.hue, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().hide).pack(side='left')
		Button(btnframe, text=u'Σ', relief='flat', foreground=self.fgcolor, background=self.hue, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().hide).pack(side='left')
		Button(btnframe, text=u'Ω', relief='flat', foreground=self.fgcolor, background=self.hue, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().hide).pack(side='left')
		Button(btnframe, text=u'¦', relief='flat', foreground=self.fgcolor, background=self.hue, font=("Tahoma", 8, "normal"), command=self.winfo_toplevel().hide).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=self.neon if mono else Zeta.Color.Neon(color2='green').hex, background=self.hue, command=self.winfo_toplevel().hide).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=self.neon if mono else Zeta.Color.Neon(color2='yellow').hex, background=self.hue, command=self.maximize).pack(side='left')
		Button(btnframe, text='■', relief='flat', foreground=self.neon if mono else Zeta.Color.Neon(color2='red').hex, background=self.hue, command=self.close).pack(side='left')

		self.winfo_toplevel().bind('<Control-w>', lambda e: self.winfo_toplevel().close())
		try:
			self.winfo_toplevel().bind_drag(top)
			self.winfo_toplevel().bind_drag(msg)
			self.winfo_toplevel().bind_drag(btnframe)
			# top.bind("<ButtonPress-1>", self.winfo_toplevel().start_move)
			# top.bind("<ButtonRelease-1>", self.winfo_toplevel().stop_move)
			# top.bind("<B1-Motion>", self.winfo_toplevel().do_move)
		except: print('Window error')

	def maximize(self):
		if self.maximized: self.winfo_toplevel().geometry(self.restore)
		else:
			self.restore = self.winfo_toplevel().geometry()
			self.winfo_toplevel().geometry(self.geometry)
		self.maximized = not self.maximized

	def close(self):
		if self.safemode: self.winfo_toplevel().hide()
		else: self.winfo_toplevel().close()