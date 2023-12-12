import Zeta
from Zeta.Panel import *
from .Overflow import Overflow
from .Menubar import *

class Taskbar(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.title('Task bar')
		width = Zeta.System.Size.Screen.width
		height = 25
		self.geometry(f"{width}x{height}+1+0")
		self.overrideredirect(1)
		#self.configure(bg=colorbg, bd=1, relief='groove')
		Label(self, text=r'[ Workspace ]').place(relx=0.48, rely=0)

		appframe = Frame(self)
		appframe.pack(side='left', fill='y')
		#Button(appframe, text='1', relief='flat', background='#3c3c3c').grid(column=0, row=0, sticky='NW')
		Button(appframe, text='1', relief='flat', foreground='#6effbe').grid(column=0, row=0, sticky='NW')
		Button(appframe, text='2', relief='flat').grid(column=1, row=0, sticky='NW')
		Button(appframe, text='3', relief='flat').grid(column=2, row=0, sticky='NW')
		Button(appframe, text='4', relief='flat').grid(column=3, row=0, sticky='NW')
		Button(appframe, text='#', relief='flat').grid(column=4, row=0, sticky='NW')

		# =======================[ Menu ]=======================
		menuframe = Frame(self)
		menuframe.pack(side='left', fill='y')

		progmenu = ProgramMenu()
		self.imgdatabase=Zeta.Image.Icon.Load(icon='database', icontype='neon').image
		Button2(menuframe, text=' Program', image=self.imgdatabase, compound='left', side='left', fill='y', hover=progmenu, toggle=progmenu, geometry='bottom')

		filemenu = FileMenu()
		self.imgfile=Zeta.Image.Icon.Load(icon='file', icontype='neon').image
		Button2(menuframe, text=' File', image=self.imgfile, compound='left', side='left', fill='y', hover=filemenu, toggle=filemenu, geometry='bottom')

		networkmenu = NetworkMenu()
		self.imglink=Zeta.Image.Icon.Load(icon='qr', icontype='neon').image
		Button2(menuframe, text=' Network', image=self.imglink, compound='left', side='left', fill='y', hover=networkmenu, toggle=networkmenu, geometry='bottom')

		Frame(menuframe, highlightthickness=1, highlightbackground='white').pack(side='left', fill='y')

		codemenu = CodeMenu()
		self.imgcode=Zeta.Image.Icon.Load(icon='code', icontype='neon').image
		Button2(menuframe, text=' Coding', image=self.imgcode, compound='left', side='left', fill='y', hover=codemenu, toggle=codemenu, geometry='bottom')

		hackmenu = HackingMenu()
		self.imgterm=Zeta.Image.Icon.Load(icon='term3', icontype='neon').image
		Button2(menuframe, text=' Hacking', image=self.imgterm, compound='left', side='left', fill='y', hover=hackmenu, toggle=hackmenu, geometry='bottom')

		forensicsmenu = ForensicsMenu()
		self.imgfor=Zeta.Image.Icon.Load(icon='folder', icontype='neon').image
		Button2(menuframe, text=' Forensics', image=self.imgfor, compound='left', side='left', fill='y', hover=forensicsmenu, toggle=forensicsmenu, geometry='bottom')

		remenu = REMenu()
		self.imgre=Zeta.Image.Icon.Load(icon='table', icontype='neon').image
		Button2(menuframe, text=' RE', image=self.imgre, compound='left', side='left', fill='y', hover=remenu, toggle=remenu, geometry='bottom')
		#=======================================================

		trayframe = Frame(self)
		trayframe.pack(side='right', fill='y')
		self.grid_columnconfigure(1, weight=1)
		self.imgcpu=Zeta.Image.Icon.Load(icon='cpuw', icontype='bw').image
		Button(trayframe, text=' 13%', relief='flat', image=self.imgcpu, compound='left').grid(column=0, row=0, sticky='NW')
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		Button(trayframe, text=' 322G', relief='flat', image=self.imghdd, compound='left').grid(column=1, row=0, sticky='NW')
		self.imgnetwork=Zeta.Image.Icon.Load(icon='networkw', icontype='bw').image
		Button(trayframe, text=' 0.7 MB/s', relief='flat', image=self.imgnetwork, compound='left').grid(column=2, row=0, sticky='NW')
		self.imgram=Zeta.Image.Icon.Load(icon='ramw', icontype='bw').image
		Button(trayframe, text=' 2.2 GB', relief='flat', image=self.imgram, compound='left').grid(column=3, row=0, sticky='NW')
		self.imgtemp=Zeta.Image.Icon.Load(icon='tempw', icontype='bw').image
		Button(trayframe, text=' 33°C', relief='flat', image=self.imgtemp, compound='left').grid(column=4, row=0, sticky='NW')
		self.imgvolume=Zeta.Image.Icon.Load(icon='volumew', icontype='bw').image
		Button(trayframe, text=' Ballad', relief='flat', image=self.imgvolume, compound='left').grid(column=5, row=0, sticky='NW')
		self.imgmenu=Zeta.Image.Icon.Load(icon='menuw', icontype='bw').image
		
		overflow = Overflow()
		btnoverflow = Button(trayframe, text='', relief='flat', image=self.imgmenu, compound='none')
		btnoverflow.grid(column=6, row=0, sticky='NW')
		Workspace.toggle_bind(btnoverflow, overflow)

		self.theme(self, bg='#000000', fg='#ffffff')