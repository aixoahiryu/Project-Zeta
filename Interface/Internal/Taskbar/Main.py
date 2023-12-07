import Zeta
from Zeta.Panel import *
from .Overflow import Overflow
from .Toolbar import Toolbar

import os

ZLCORE = Zeta.System.Path.Core.ZLCORE

class Taskbar(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.title('Task bar')
		width = Zeta.System.Size.Screen.width
		height = Zeta.System.Size.taskbar
		self.geometry(f"{width}x{height}+0-0")
		self.overrideredirect(1)
		self.grid_rowconfigure(0, weight=1)
		#Label(self, text=r'[ Workspace ]').place(relx=0.48, rely=0)

		appframe = Frame(self)
		appframe.grid(sticky='NSW', column=0, row=0)
		appframe.grid_rowconfigure(0, weight=1)
		self.imgmenu=Zeta.Image.Icon.Load(icon='menu2b', icontype='bw').image
		btnoverflow = Button(appframe, text='', relief='flat', image=self.imgmenu, compound='left')
		btnoverflow.grid(column=0, row=0, sticky='NSW')
		overflow = Overflow()
		# Zeta.System.WM.toggle_bind(btnoverflow, overflow)
		Workspace.toggle_bind(btnoverflow, overflow)

		quickframe = Frame(self)
		quickframe.grid(sticky='NSW', column=1, row=0)
		quickframe.grid_rowconfigure(0, weight=1)
		self.imgbrowser=Zeta.Image.Icon.Load(icon='eye2b', icontype='bw').image
		Button(quickframe, text='', relief='flat', image=self.imgbrowser, compound='left').grid(column=0, row=0, sticky='NSW')
		self.imgproxy=Zeta.Image.Icon.Load(icon='proxyb', icontype='bw').image
		Button(quickframe, text='', relief='flat', image=self.imgproxy, compound='left').grid(column=1, row=0, sticky='NSW')
		
		programframe = Frame(self)
		programframe.grid(sticky='NSW', column=2, row=0)
		programframe.grid_rowconfigure(0, weight=1)
		Button(programframe, text='[ Main ]', relief='flat').grid(column=0, row=0, sticky='NSW')
		Button(programframe, text='Peripheral', relief='flat').grid(column=1, row=0, sticky='NSW')
		Button(programframe, text='Transient', relief='flat').grid(column=2, row=0, sticky='NSW')
		
		trayframe = Frame(self)
		trayframe.grid(sticky='NSE', column=3, row=0)
		trayframe.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(3, weight=1)
		
		toolbar = Toolbar()
		btnF = Button(trayframe, text=' F ', relief='flat')
		btnF.grid(column=0, row=0, sticky='NSW')
		btnF.bind("<Button-3>", lambda e: (os.startfile(ZLCORE+r'\Toolbar\F'), Workspace.toggle_sidebar()))
		btnN = Button(trayframe, text=' N ', relief='flat')
		btnN.grid(column=1, row=0, sticky='NSW')
		btnN.bind("<Button-3>", lambda e: (os.startfile(ZLCORE+r'\Toolbar\N'), Workspace.toggle_sidebar()))
		btn_ = Button(trayframe, text=' _ ', relief='flat')
		btn_.grid(column=2, row=0, sticky='NSW')
		btn_.bind("<Button-3>", lambda e: (os.startfile(ZLCORE+r'\Toolbar\_'), Workspace.toggle_sidebar()))
		Workspace.hover_bind(btnF, toolbar, stay=True)
		Workspace.hover_bind(btnN, toolbar, stay=True)
		Workspace.hover_bind(btn_, toolbar, stay=True)

		self.imgrect=Zeta.Image.Icon.Load(icon='cornerb', icontype='bw').image
		Button(trayframe, text='', relief='flat', image=self.imgrect, compound='left').grid(column=3, row=0, sticky='NSW')
		self.imghardware=Zeta.Image.Icon.Load(icon='cpub', icontype='bw').image
		Button(trayframe, text=' System', relief='flat', image=self.imghardware, compound='left').grid(column=4, row=0, sticky='NSW')
		self.imgmonitoring=Zeta.Image.Icon.Load(icon='motherboardb', icontype='bw').image
		Button(trayframe, text=' Manager', relief='flat', image=self.imgmonitoring, compound='left').grid(column=5, row=0, sticky='NSW')
		self.imgcalendar=Zeta.Image.Icon.Load(icon='calendarb', icontype='bw').image
		Button(trayframe, text=' Z[1.95996|97.5] 54.7356° π[3.14159] √[1.41421] ϕ[1.61803]', relief='flat', image=self.imgcalendar, compound='left').grid(column=6, row=0, sticky='NSW')
		Button(trayframe, text=' ', relief='flat', command= lambda: Workspace.hide(Workspace.active)).grid(column=7, row=0, sticky='NSW')

		self.theme(self, bg='#ffffff', fg='#000000')