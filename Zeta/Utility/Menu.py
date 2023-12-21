import Zeta
from tkinter import *

def directory(anchor, path='', geometry='right', color='white', post=[]):
	Zeta.Image.Common.bw()
	menubar = Menu(tearoff=0)
	menubar.add_command(label="New", command=lambda: Zeta.Utility.Dialog.newfile(anchor, path, geometry))
	menubar.add_separator()
	menubar.add_command(label="Open", command=lambda: Zeta.System.OS.open(path))
	menubar.add_command(label="Edit", command=lambda: Zeta.System.OS.edit(path))
	subexecute = Menu(menubar, tearoff=0)
	menubar.add_cascade(label="Execute", menu=subexecute)
	subexecute.add_command(label="System", command=lambda: Zeta.System.OS.launch(path))
	subexecute.add_command(label="Browser", command=lambda: Zeta.System.OS.launch(path, 'browser'))
	subexecute.add_separator()
	subexecute.add_command(label="Python", command=lambda: Zeta.System.OS.launch(path, 'python'))
	menubar.add_separator()
	menubar.add_command(label="Terminal", image=imgtermbw, compound='left', command=lambda: Zeta.System.OS.terminal(path))
	menubar.add_command(label="Detach", image=imgdetachbw, compound='left', command=lambda: Zeta.Utility.Launch.Explorer(path=path, color=color, transient=anchor, geometry=geometry, parent=anchor, anchor=anchor))
	menubar.add_separator()
	return mpost(menubar, anchor, post)

def file(anchor, path='', geometry='right', color='white', post=[]):
	menubar = Menu(tearoff=0)
	menubar.add_command(label="View", command=lambda: Zeta.Utility.Launch.Editor(path=path, color=color, transient=anchor, geometry=geometry, parent=anchor, anchor=anchor))
	menubar.add_separator()
	menubar.add_command(label="Open", command=lambda: Zeta.System.OS.open(path))
	menubar.add_command(label="Edit", command=lambda: Zeta.System.OS.edit(path))
	menubar.add_separator()
	return mpost(menubar, anchor, post)


def mpost(menu, anchor, pos):
	if pos==[]:
		x = anchor.winfo_x() if isinstance(anchor, Toplevel) else anchor.winfo_rootx()
		y = anchor.winfo_y() if isinstance(anchor, Toplevel) else anchor.winfo_rooty()
		menu.post(x, y)
	else: menu.post(pos[0], pos[1])
	return menu