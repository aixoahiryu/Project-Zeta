import Zeta
from Zeta.Panel import *

def launch(window, geometry='', transient='', parent='', anchor='widget', *args, **kargs):
	if geometry!='':
		if geometry in ['left', 'right', 'top', 'bottom']:
			window.update()
			Zeta.Utility.Geometry.calc(parent, window, geometry, anchor)
		else: window.geometry(geometry)
	if transient!='': window.transient(transient.winfo_toplevel())
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
