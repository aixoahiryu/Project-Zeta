import Zeta
from Zeta.Panel import *
from .Dial import Dial
from .Console import Console
from .Central import Central

import os
import subprocess

Utility = Zeta.System.Path.Core.X + r'/Null/[ Program ]/Utility'

class Launch(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.title('===[ Sidebar: File ]===')
		self.attributes('-topmost', True)
		self.geometry(Zeta.System.Size.geometry['mpv'])
		self.frame.grid_columnconfigure(1, weight=1)
		self.frame.grid_rowconfigure(1, weight=1)

		frame0 = Frame(self.frame)
		frame0.grid(sticky='E', column=0, row=0, ipady=0, ipadx=0)
		Button(frame0, text='[ Scraps ]', command=lambda: os.startfile(Utility+r'/[ Scraps ].txt')).grid(sticky='W', column=0, row=0)
		Button(frame0, text='Active', command=lambda: os.startfile(Utility+r'/Active.txt')).grid(sticky='W', column=1, row=0)

		frame1 = Frame(self.frame)
		frame1.grid(sticky='S', column=0, row=1)
		Button(frame1, text='Proxy', command=lambda: os.startfile(Utility+r'/Proxy.py')).grid(sticky='N', row=0)
		Button(frame1, text='Sticky', command=exit).grid(sticky='N', row=1)
		#Button(frame1, text='B', command=menu_clear).grid(sticky='N', row=2)
		#ttk.Separator(frame1, orient='horizontal').grid(sticky='EW', row=3)
		#Button(frame1, text='yt', command=menu_clear).grid(sticky='N', row=4)

		frame2 = Frame(self.frame)
		frame2.grid(sticky='NSEW', column=1, row=1)
		frame2.grid_columnconfigure(0, weight=1)
		frame2.grid_rowconfigure(0, weight=1)
		frame2_1 = Frame(frame2)
		frame2_1.grid(sticky='SW', column=0, row=0)
		Button(frame2_1, text='Breach', command=exit, bg='black', fg='white').grid(sticky='SW', row=0)
		frame2_2 = Frame(frame2)
		frame2_2.grid(sticky='SE', column=1, row=0)
		self.imgscreen=Zeta.Image.Icon.Load(icon='proxyb', icontype='bw').image
		Button(frame2_2, text='FastStone ', compound='right', image=self.imgscreen, command=lambda: os.startfile(r'D:\Tools\FSCapture97\FSCapture.exe')).grid(sticky='SE', row=0, column=0)
		self.imgplay=Zeta.Image.Icon.Load(icon='playb', icontype='bw').image
		Button(frame2_2, text='mpv ', compound='right', image=self.imgplay, command=lambda: os.startfile(r'C:\cygwin64\home\sidebar\mpv.vbs')).grid(sticky='SE', row=1, column=0)
		self.imgbrowser=Zeta.Image.Icon.Load(icon='cornerb', icontype='bw').image
		Button(frame2_2, text='links2 ', compound='right', image=self.imgbrowser, command=lambda: os.startfile(r'D:\MEGA\ZL-Core\Toolbar\F\Utility\Links.lnk')).grid(sticky='SE', row=2, column=0)
		nullbtn = Button(frame2_2, text='- Null', command=lambda: os.startfile(Utility+r'/- Null.py'))
		nullbtn.grid(sticky='SE', row=3, column=0)
		nullbtn.bind("<Button-3>", lambda e: subprocess.Popen(["C:\\Program Files\\Notepad++\\notepad++.exe", "-ro", Utility+r'/- Null.py'], start_new_session=True))

		frame3 = Frame(self.frame)
		frame3.grid(sticky='E', column=1, row=0, ipady=0, ipadx=0)
		Button(frame3, text='Experiment', command=lambda: os.startfile(Utility+r'/Experiment.txt')).grid(sticky='W', row=0, column=0)
		Button(frame3, text='File', command=lambda: os.startfile(Utility+r'/File.txt')).grid(sticky='W', row=0, column=1)
		Label(frame3, text='|').grid(sticky='W', row=0, column=2)
		#Button(frame3, text='_', command=lambda: goPath('D:\\_')).grid(sticky='W', row=0, column=3)
		#Button(frame3, text='Data', command=lambda: goPath('D:\\Data')).grid(sticky='W', row=0, column=4)
		#Button(frame3, text='Core', command=lambda: goPath('D:\\ZL-Core')).grid(sticky='W', row=0, column=5)

		linkbtn = Button(self.frame, text='[ Link ]', command=lambda: os.startfile(Utility+r'/Link.py'))
		linkbtn.configure(font="-family {Courier New} -size 20")
		linkbtn.place(relx=0.284, rely=0.369, height=74, width=167)
		linkbtn.bind("<Button-3>", lambda e: subprocess.Popen(["C:\\Program Files\\Notepad++\\notepad++.exe", "-ro", Utility+r'/Link.py'], start_new_session=True))

		Dial().transient(self)
		Console().transient(self)
		Central().transient(self)
		self.theme(self.frame, bg='#ffffff', fg='#000000')