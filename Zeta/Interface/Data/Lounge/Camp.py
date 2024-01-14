import Zeta

from Zeta.Panel import *
import os
import subprocess

class Camp(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		bottom = Zeta.System.Size.taskbar
		self.geometry(f'+{25+10}-{bottom}')
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerw', icontype='bw').image
		self.imgram=Zeta.Image.Icon.Load(icon='ramw', icontype='bw').image
		self.imgbrain=Zeta.Image.Icon.Load(icon='brainw', icontype='bw').image
		self.InitWindow()

		Button2(self.frame, text=' World', image=self.imgram, compound='left', side='left', fill='y', hover=self._World, toggle=self._World, geometry='top')
		Button2(self.frame, text=' Mode', image=self.imgbrain, compound='left', side='left', fill='y', hover=self._Mode, toggle=self._Mode, geometry='top')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
		Button2(self.frame, text=' Camp', image=self.imghdd, compound='left', side='left', fill='y', hover=self._Camp, toggle=self._Camp, geometry='top')
		Button2(self.frame, text=' Lounge', image=self.imghdd, compound='left', side='left', fill='y', hover=self._Lounge, toggle=self._Lounge, geometry='top')
		Button2(self.frame, text=' Study', image=self.imghdd, compound='left', side='left', fill='y', hover=self._Study, toggle=self._Study, geometry='top')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
		Button2(self.frame, text=' Base', image=self.imghdd, compound='left', side='left', fill='y', hover=self._Base, toggle=self._Base, geometry='top')
		Button2(self.frame, text=' Survival', image=self.imghdd, compound='left', side='left', fill='y', hover=self._Survival, toggle=self._Survival, geometry='top')
		Button2(self.frame, text=' Strategy', image=self.imghdd, compound='left', side='left', fill='y', hover=self._Strategy, toggle=self._Strategy, geometry='top')
		Button2(self.frame, text=' Adventure', image=self.imghdd, compound='left', side='left', fill='y', hover=self._Adventure, toggle=self._Adventure, geometry='top')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')

		self.theme(self.frame, bg=self.hue, fg='#ffffff')

	def InitWindow(self):
		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button2(x.frame, text='Philosophy', side='top', fill='x', geometry='right')
		Button2(x.frame, text='Ambient', side='top', fill='x', geometry='right', buffer=['Horror', 'Strategy', 'Adventure'], menucolor='green', textcolor='white')
		Button2(x.frame, text='Occult', side='top', fill='x', geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._World = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button2(x.frame, text='1 ¦ Relax', side='top', fill='x', geometry='right')
		Button2(x.frame, text='2 ¦ Focus', side='top', fill='x', geometry='right')
		Button2(x.frame, text='3 ¦ Generate', side='top', fill='x', geometry='right')
		Button2(x.frame, text='4 ¦ Calibrate', side='top', fill='x', geometry='right')
		Button2(x.frame, text='5 ¦ Optimize', side='top', fill='x', geometry='right')
		Button2(x.frame, text='6 ¦ Sabbath', side='top', fill='x', geometry='right')
		Button2(x.frame, text='7 ¦ Genocide', side='top', fill='x', geometry='right')
		Frame(x.frame, highlightbackground=x.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Mode = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Project Aego', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Stranded', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' The Smoke Room', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Tent', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Stealth', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Desert', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Camp = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Polar night', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Machina Lutris', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Lackadaisy', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' No Umbrellas Allowed', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Strange Horticulture', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Potion craft', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Lounge = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Intertwined', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Violet memoir', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' City', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Masion', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Library', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Greenhouse', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Conservatory', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Study = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Rain world', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Darkwood', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' The cat lady', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' This war of mine', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Don\'t starve', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Sunless Sea', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Project Moon[ Lobotomy Corporation, Library of Ruina, Limbus Company ]', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' OF MICE AND SAND', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Frostpunk', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Beholder', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Papers please, Mind Scanners', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Do Not Feed the Monkeys', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Aground | Cave story | Core keeper | Owlboy', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Home safety hotline', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Hypnospace outlaw', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Welcome to the game, XXX_CYBERRAT_XXX', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Base = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' NEO scavenger', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Cataclysm: Dark Days Ahead', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' The long dark', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' The forest | Green hell', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Survival = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Whitewolf[WoD] | Cultist simulator', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Inscryption | Buckshot Roulette', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Loop hero', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Back to the dawn, The Escapist', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Strategy = x

		x = Window(mode='border', color2='green')
		x.attributes('-topmost', True)
		x.attributes('-alpha', Zeta.Setting.opacityneon)
		Button(x.frame, text=' Axiom Verge, Castlevania', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Megaman Zero', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Faith', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' WORLD OF HORROR', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Termina', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Hellnight', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Stargate | SCP | Alan Wake, CONTROL, Quantum Break, Max Payne', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Heavy Rain, Fahrenheit', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Twilight Zone, Harvester, Phantasmagoria, Darkseed', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' The evil within', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Valentine\'s Rain', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Chrono Trigger', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Katana 0, The final station, Black future \'88', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button(x.frame, text=' Erin Hunter, Kyell Gold, Rick Griffin', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Outlaw star', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Button(x.frame, text=' Inherit the earth, Redwall, Small Saga', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg='#ffffff', bg=x.hue)
		self._Adventure = x