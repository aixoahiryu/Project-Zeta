import Zeta
from Zeta.Panel import *

def launch(window, geometry='', transient='', *args, **kargs):
	if geometry!='': window.geometry(geometry)
	if transient!='': window.transient(transient)
	window.attributes('-alpha', Zeta.Setting.opacityneon)
	window.attributes('-topmost', True)
	window.show()

def Explorer(path=Zeta.System.Path.Scraps.path, color='green', title='', mode='basic', panelgeometry='right', *args, **kargs):
	x = Zeta.Panel.Control.FileBox.FilePanel(title=title, home=path, color2=color, mode=mode, panelgeometry=panelgeometry)
	launch(x, *args, **kargs)
	return x

def Editor(path='', color='green', title='', mode='basic', *args, **kargs):
	x = Zeta.Panel.Control.TextBox.TextPanel(title=title, file=path, color2=color, mode=mode)
	launch(x, *args, **kargs)
	return x
