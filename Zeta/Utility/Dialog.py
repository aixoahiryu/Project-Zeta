import Zeta
from tkinter import *
from tkinter.simpledialog import askstring

import time
import os

def input(msg='', printable=''):
	name = askstring('Input', msg)
	# name = ''.join(filter(lambda x: x in printable, name))
	return name

def newFileOrFolder(path, newFileName, dialog):
	if os.path.isdir(path): fullpath2 = path
	if os.path.isfile(path): fullpath2 = os.path.split(path)[0]
	if len(newFileName.get().split('.')) != 1:
		open(os.path.join(fullpath2, newFileName.get()), 'w').close()
	else:
		os.makedirs(os.path.join(fullpath2, newFileName.get()))
	dialog.destroy()

def newfile(path='', parent='', geometry='right'):
	parent = parent.winfo_toplevel()
	newFileName = StringVar(parent, "", 'new_name')
	newFileName.set('')
	# colorfg = 'white' if parent.darkmode else 'black'
	# colorbg = 'black' if parent.darkmode else 'white'

	dialog = Zeta.Panel.Window(color2=parent.color2, mode='basic', title='Create file')
	# dialog.geometry(f"+{25+10+333}+25")
	dialog.attributes('-topmost', True)
	#dialog.attributes('-alpha', Zeta.Setting.opacity)
	dialog.resizable(False, False)
	dialog.title("New")
	dialog.transient(parent)
	dialog.columnconfigure(0, weight=1)
	Label(dialog.frame, text='Enter File or Folder name').grid()
	Entry(dialog.frame, textvariable=newFileName).grid(column=0, sticky='NSEW')
	btnframe = Frame(dialog.frame)
	btnframe.grid(column=0, sticky='NSEW')
	Button(btnframe, text="Time", command=lambda: newFileName.set( str(round(time.time())) )).pack(side=LEFT)
	Button(btnframe, text="TXT", command=lambda: newFileName.set(newFileName.get()+'.txt')).pack(side=LEFT)
	Button(btnframe, text="[  ]", command=lambda: newFileName.set(r'[ '+newFileName.get()+r' ]')).pack(side=LEFT)
	Button(btnframe, text=" ¦ ", command=lambda: newFileName.set(newFileName.get()+r' ¦ ')).pack(side=LEFT)
	Button(btnframe, text=" √ ", command=lambda: newFileName.set(r'√ ')).pack(side=LEFT)
	Button(btnframe, text=" ≡ ", command=lambda: newFileName.set(r'≡ ')).pack(side=LEFT)
	Button(btnframe, text=" ▷ ", command=lambda: newFileName.set(r'▷ ')).pack(side=LEFT)
	Button(btnframe, text=" Δ ", command=lambda: newFileName.set(r'Δ[ '+newFileName.get()+r' ]')).pack(side=LEFT)
	Button(btnframe, text=" Σ ", command=lambda: newFileName.set(r'Σ[ '+newFileName.get()+r' ]')).pack(side=LEFT)
	Button(btnframe, text=" Ω ", command=lambda: newFileName.set(r'Ω[ '+newFileName.get()+r' ]')).pack(side=LEFT)
	Button(btnframe, text="Create", command=lambda: newFileOrFolder(path, newFileName, dialog)).pack(side=LEFT)
	dialog.theme(target=dialog.frame, bg=Zeta.Color.Neon(parent.color2).hue, fg=Zeta.Color.Neon(parent.color2).hex)
	Zeta.System.WM.geocalc(dialog, parent, geometry, parent)
	dialog.show()
	return dialog