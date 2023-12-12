import Zeta
from Zeta.Panel import *

class ProgramMenu(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerw', icontype='bw').image
		self.imgcode=Zeta.Image.Icon.Load(icon='codew', icontype='bw').image
		self.imgfile=Zeta.Image.Icon.Load(icon='textw', icontype='bw').image
		self.imgnetwork=Zeta.Image.Icon.Load(icon='networkw', icontype='bw').image
		self.imgsys=Zeta.Image.Icon.Load(icon='systemw', icontype='bw').image
		self.imgutil=Zeta.Image.Icon.Load(icon='tempw', icontype='bw').image
		self.InitWindow()

		Button2(self.frame, text=' Coding', image=self.imgcode, compound='left', side='top', fill='x', hover=self._Coding, toggle=self._Coding, geometry='right')
		Button2(self.frame, text=' Content', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Content, toggle=self._Content, geometry='right')
		Button2(self.frame, text=' File', image=self.imgfile, compound='left', side='top', fill='x', hover=self._File, toggle=self._File, geometry='right')
		Button2(self.frame, text=' Network', image=self.imgnetwork, compound='left', side='top', fill='x', hover=self._Network, toggle=self._Network, geometry='right')
		Button2(self.frame, text=' System', image=self.imgsys, compound='left', side='top', fill='x', hover=self._System, toggle=self._System, geometry='right')
		Button2(self.frame, text=' Utility', image=self.imgutil, compound='left', side='top', fill='x', hover=self._Utility, toggle=self._Utility, geometry='right')
		# Button(self.frame, text=' Coding', relief='flat', image=self.imgcode, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.ZETA)).pack(side='top', fill='x')
		# Button(self.frame, text=' Content', relief='flat', image=self.imghdd, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X)).pack(side='top', fill='x')
		# Button(self.frame, text=' File', relief='flat', image=self.imgfile, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X)).pack(side='top', fill='x')
		# Button(self.frame, text=' Network', relief='flat', image=self.imgnetwork, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X)).pack(side='top', fill='x')
		# Button(self.frame, text=' System', relief='flat', image=self.imgsys, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X)).pack(side='top', fill='x')
		# Button(self.frame, text=' Utility', relief='flat', image=self.imgutil, compound='left', anchor='w', command=lambda: Zeta.System.OS.open(Zeta.System.Path.Core.X)).pack(side='top', fill='x')
		
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		
		Button2(self.frame, text=' Note', image=self.corner, compound='left', side='top', fill='x', hover=self._Note, toggle=self._Note, geometry='right')
		# btnnote = Button(self.frame, text=' Note', relief='flat', image=self.corner, compound='left', anchor='w')
		# btnnote.pack(side='top', fill='x')
		# Zeta.System.WM.hover_bind(btnnote, self._Note(), geometry='right')
		# Zeta.System.WM.toggle_bind(btnnote, self._Note(), stay=True, geometry='right')
		Button2(self.frame, text=' Editor', image=self.corner, compound='left', side='top', fill='x', hover=self._Editor, toggle=self._Editor, geometry='right')
		Button2(self.frame, text=' Clipboard', image=self.corner, compound='left', side='top', fill='x', hover=self._Clipboard, toggle=self._Clipboard, geometry='right')
		Button2(self.frame, text=' Terminal', image=self.corner, compound='left', side='top', fill='x', hover=self._Terminal, toggle=self._Terminal, geometry='right')

		self.theme(self.frame, bg=self.hue, fg='#ffffff')

	def InitWindow(self):
		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Editor', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Debugger: [ GDB ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' API: [ SoapUI, API-guide mentalis ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Documentation', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Demo', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Local', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Coding = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Audio: [ Sunvox ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Game', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Image: [ Photoshop, Inkscape, Aseprite ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Writing: [ Furry, Twine ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Content = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Archive: [ 7z ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Compress: [ Caesium ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Analysis: [ Spacesniffer ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Merge', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Restore', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._File = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Browser: [ ungoogled-chromium, Links2, K-meleon, Otter, IceWeasel, Pale moon ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Update: [ QuiteRSS, urlwatch ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Security: [ KeepassXC, VirusTotal ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' File: [ Syncthing ] [ qBitorrent, Filezilla, ZOOM, DC++, Soulseek ] [ MegaBasterd ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' ===[ Zeta-net ]===', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Chat: [ Discord, Telegram, Pidgin, qTox, RetroShare ] [ IRC, XMPP, Matrix ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' E-mail: [ Claws-Mail ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' File: [ OnionShare ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Market: [ OpenBazaar ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' ', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Darknet: [ Tor, Zeronet, Gemini, Gopher ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Protocol: [ Torrent, Soulseek, Direct Connect ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Network = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Monitoring: [ Process hacker, Core Temp, Rainmeter ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Emulator: [ VMware ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Internal: [ PChunter, PowerToys ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Health: [ Crystaldisk ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._System = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Screenshot: [ Faststone ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Media: [ mpv ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Audio: [ AIMP ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Document: [ SumatraPDF ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Image: [ Irfanview ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Keyboard: https://vietnamese.typeit.org/', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Utility = x

		#---------------------------------------------

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Notepad++', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		Button(x.frame, text=' Cherrytree', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		Button(x.frame, text=' Treesheet', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Note = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Sublime', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		Button(x.frame, text=' VScodium', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		Button(x.frame, text=' Kate', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Editor = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' CopyQ', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Clipboard = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' CMD', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		Button(x.frame, text=' Cygwin', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='left')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Terminal = x


class ProgramMenu2(Menu):
	def __init__(self, *args, **kwargs):
		Menu.__init__(self, tearoff=0, *args, **kwargs)

		self.add_command(label="Zeta")
		self.add_command(label="X")
		self.add_separator()
		self.add_command(label="# Scraps")
		self.add_separator()
		#subedit = Menu(self, tearoff=0)
		#self.add_cascade(label="Edit", menu=subedit, command=menu_edit)
		# self.imgterm = Zeta.Image.Icon.Load('termbw', 'bw').image
		# self.add_command(label="Terminal", image=self.imgterm, compound='left', command=lambda: (self.controller.toggle_sidebar(), Zeta.System.OS.terminal(self.fullpath)))
		# self.imgdetach = Zeta.Image.Icon.Load('windowbw', 'bw').image
		# self.add_command(label="Detach", image=self.imgdetach, compound='left', command=self.menu_detach)
		# self.tree.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))
