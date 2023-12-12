import Zeta

from Zeta.Panel import *
import os
import subprocess

# class Mode(Window):
# 	def __init__(self, *args, **kwargs):
# 		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
# 		self.geometry('-1+65')
# 		self.attributes('-topmost', True)
# 		self.attributes('-alpha', Zeta.Setting.opacityneon)

# 		btnmain = Button2(self.frame, text='Mode', width=11, anchor='center', side='right', fill='y', geometry='bottom')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='right', fill='y')
# 		Button2(self.frame, text=' Relax', side='left', fill='y', geometry='bottom')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
# 		Button2(self.frame, text=' Focus', side='left', fill='y', geometry='bottom')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
# 		Button2(self.frame, text=' Generate', side='left', fill='y', geometry='bottom')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
# 		Button2(self.frame, text=' Calibrate', side='left', fill='y', geometry='bottom')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
# 		Button2(self.frame, text=' Optimize', side='left', fill='y', geometry='bottom')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
# 		Button2(self.frame, text=' Sabbath', side='left', fill='y', geometry='bottom')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
# 		Button2(self.frame, text=' Genocide', side='left', fill='y', geometry='bottom')

# 		self.theme(self.frame, bg=self.hue, fg='#ffffff')
# 		btnmain['foreground'] = '#000000'
# 		btnmain['background'] = Zeta.Color.Neon('green').hex

# class World(Window):
# 	def __init__(self, *args, **kwargs):
# 		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
# 		self.geometry('-1+105')
# 		self.attributes('-topmost', True)
# 		self.attributes('-alpha', Zeta.Setting.opacityneon)

# 		btnmain = Button2(self.frame, text='World', width=11, anchor='center', side='right', fill='y', geometry='bottom')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='right', fill='y')
# 		Button2(self.frame, text=' Philosophy', side='left', fill='y', geometry='bottom', buffer=[], menucolor='green', textcolor='white')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
# 		Button2(self.frame, text=' Ambient', side='left', fill='y', geometry='bottom', buffer=['Horror', 'Strategy', 'Adventure'], menucolor='green', textcolor='white')
# 		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')
# 		Button2(self.frame, text=' Occult', side='left', fill='y', geometry='bottom', buffer=[], menucolor='green', textcolor='white')

# 		self.theme(self.frame, bg=self.hue, fg='#ffffff')
# 		btnmain['foreground'] = '#000000'
# 		btnmain['background'] = Zeta.Color.Neon('green').hex

class Playing(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='green', *args, **kwargs)
		self.geometry('-1+25')
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerw', icontype='bw').image
		self.imgplay=Zeta.Image.Icon.Load(icon='playw', icontype='bw').image
		self.imgmusic=Zeta.Image.Icon.Load(icon='volumew', icontype='bw').image
		self.imgtext=Zeta.Image.Icon.Load(icon='textw', icontype='bw').image

		btnmain = Button2(self.frame, text='Playing', width=11, anchor='center', side='right', fill='y', geometry='bottom')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='right', fill='y')
		Button2(self.frame, text=' Text', width=111, image=self.imgtext, compound='left', side='right', fill='y', geometry='bottom', path=Zeta.System.Path.Core.X+r'/Void/# META/Lounge/Playing/Thread', listdir=True, menucolor='green', textcolor='white')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='right', fill='y')
		Button2(self.frame, text=' Image', width=111, image=self.imghdd, compound='left', side='right', fill='y', geometry='bottom', path=Zeta.System.Path.Core.X+r'/Void/# META/Lounge/Playing/Image', listdir=True, menucolor='green', textcolor='white')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='right', fill='y')
		Button2(self.frame, text=' Audio', width=111, image=self.imgmusic, compound='left', side='right', fill='y', geometry='bottom', path=Zeta.System.Path.Core.X+r'/Void/# META/Lounge/Playing/Audio', listdir=True, menucolor='green', textcolor='white')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='right', fill='y')
		Button2(self.frame, text=' Video', width=111, image=self.imgplay, compound='left', side='right', fill='y', geometry='bottom', path=Zeta.System.Path.Core.X+r'/Void/# META/Lounge/Playing/Video', listdir=True, menucolor='green', textcolor='white')

		# Mode().transient(self)
		# World().transient(self)
		self.theme(self.frame, bg=self.hue, fg='#ffffff')
		btnmain['foreground'] = '#000000'
		btnmain['background'] = Zeta.Color.Neon('green').hex