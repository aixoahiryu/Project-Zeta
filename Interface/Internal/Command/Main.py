import Zeta

from Zeta.Panel import *
import os
import subprocess

ZLCORE = Zeta.System.Path.Core.ZLCORE

class Command(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.title('===[ Sidebar: File ]===')
		self.attributes('-topmost', True)
		width = Zeta.System.Size.Screen.width - 10 - 10
		height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 10 -10
		self.geometry(f"{width}x{height}+10+10")

		notebook = Notebook(self.frame)
		notebook.enable_traversal()
		notebook.pack(fill='both')
		frame0 = Frame(notebook)
		frame1 = Frame(notebook)
		frame2 = Frame(notebook)
		frame3 = Frame(notebook)
		frame4 = Frame(notebook)
		frame5 = Frame(notebook)
		frame6 = Frame(notebook)
		frame0.pack(fill='both')
		frame1.pack(fill='both')
		frame2.pack(fill='both')
		frame3.pack(fill='both')
		frame4.pack(fill='both')
		frame5.pack(fill='both')
		frame6.pack(fill='both')

		notebook.add(frame0, text='Matter')
		notebook.add(frame1, text='Infernal')
		notebook.add(frame2, text='Physical')
		notebook.add(frame3, text='Theory')
		notebook.add(frame4, text='Digital')
		notebook.add(frame5, text='Astral')
		notebook.add(frame6, text='Data')

		Button(frame1, text='Temp').pack()
		Button(frame1, text='MV').pack()
		Button(frame2, text='MP3').pack()

		self.theme(self.frame, bg='#ffffff', fg='#000000')