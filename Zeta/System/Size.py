from tkinter import *

geometry = {'main': ''}
taskbar = 30
topbar = 50

class Screen():
	width = 1366
	height = 768

class Window():
	main = [920, 740]
	side = [444, 740]
	mpv = [444, 270]
	npp = [444, 424]
	aimp = [444, 50]

width = Screen.width - Window.aimp[0] -2 -2
height = Screen.height - taskbar -2
geometry['main'] = f"{width}x{height}+2+2"

width = Window.mpv[0] - 2
height = Window.mpv[1]
bottom = taskbar
geometry['mpv'] = f"{width}x{height}-2-{bottom}"

width = Window.npp[0] - 2
height = Window.npp[1]
bottom = taskbar + Window.mpv[1]
geometry['npp'] = f"{width}x{height}-2-{bottom+2}"

width = Window.aimp[0] - 2
height = Window.aimp[1] - 12
bottom = taskbar + Window.mpv[1] + Window.npp[1]
geometry['aimp'] = f"{width}x{height}-2-{bottom+2+2}"