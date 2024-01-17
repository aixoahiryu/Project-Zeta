import Zeta
from Zeta.Panel import *
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.simpledialog import askstring

# import copy
import time
import os
import glob
import subprocess

from natsort import os_sorted
#import codecs


ZLCORE = os.environ['ZLCORE']
#os.chdir(home)
#cwd = os.getcwd()

addicon = False
darkmode = True
tooltip = True
colorbg = "#000000" if darkmode else "#ffffff"
colorbg2 = "#253B34" if darkmode else "#6effbe"
colorfg = "#ffffff" if darkmode else "#000000"

Panel = {'System': {'sidebarext': ''}, 'Task': {'root': ''}, 'Bridge': {'root': ''}, 'Monitoring': {'root': ''}}
__builtins__.Workspace = Zeta.System.WM.Workspace(Panel)
__builtins__.WorkspaceColor = 'white'
Workspace.active = ''

Workspace.geometry = {'main': '', 'sidebar': ''}
Workspace.geometry['sidebar'] = f"333x{Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25}+30+25"
Workspace.geometry['main'] = f"{Zeta.System.Size.Screen.width - 333 - 30 -5}x{Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25}-1+25"
Workspace.color = Zeta.Color.Neon(color2='white')
import Taskbar

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
width = Zeta.System.Size.Screen.width -1 -1
sidebar.geometry(f"{width}x1+0-0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)
sidebar.update()
sidebar.geometrylock = sidebar.geometry()

sidebarbump = Toplevel()
sidebarbump.attributes('-topmost', True)
sidebarbump.attributes('-alpha', 0.01)
width = Zeta.System.Size.Screen.width -1 -1
sidebarbump.geometry(f"{width}x25+0-{Zeta.System.Size.taskbar+1}")
sidebarbump.overrideredirect(1)
sidebarbump.configure(bg=colorbg)
sidebarbump.show()
sidebarbump.moved = False
sidebarbump.bind('<Leave>', lambda e: sidebar.lift())
def bumpmove(e):
	sidebarbump.geometry(f"+0-{Zeta.System.Size.taskbar+1}" if sidebarbump.moved else f"+0-{Zeta.System.Size.taskbar+25}")
	sidebarbump.moved = not sidebarbump.moved
sidebarbump.bind('<Motion>', bumpmove)

sidebarext = Taskbar.Sidebar()
Panel['System']['sidebarext'] = sidebarext

sidebar2 = Window(color2=WorkspaceColor, mode='border')
sidebar2.title('===[ Sidebar: File ]===')
sidebar2.attributes('-topmost', True)
sidebar2.attributes('-alpha', Zeta.Setting.opacity)
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25
sidebar2.geometry(f"333x{height}-1+25")
sidebar2.overrideredirect(1)
File2 = FileBox(sidebar2.frame, home=Zeta.System.Path.Core.Sidebar, color2=WorkspaceColor, panelgeometry='left')

popup = Toplevel()
popup.title('Popup')
popup.geometry("+10+350")
popup.overrideredirect(1)
popup.attributes('-alpha', Zeta.Setting.opacity)
popup.configure(bg=colorbg)
popup.attributes('-topmost', True)
popupmsg = Label(popup, text='', bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
popupmsg.grid(sticky='NWES')

style = ttk.Style()
style.theme_use('alt')
style.configure("Treeview", background=colorbg, foreground=colorfg, fieldbackground=colorbg)
style.map('Treeview', background=[('selected', colorbg2)], foreground=[('selected', '#6effbe')])
style.configure("TCombobox", background=colorbg, foreground=colorfg, fieldbackground=colorbg, highlightcolor=colorfg, arrowcolor=colorfg)
style.map('TCombobox', background=[('readonly', colorbg)], foreground=[('readonly', colorfg)], fieldbackground=[('readonly', colorbg)], highlightcolor=[('readonly', colorfg)], arrowcolor=[('readonly', colorfg)] )
style.configure("TScrollbar", background=colorbg, foreground=colorfg, fieldbackground=colorbg, highlightcolor=colorfg, troughcolor=colorbg, arrowcolor=colorfg)
style.configure("Menu", background=colorbg, foreground=colorfg, fieldbackground=colorbg, highlightcolor=colorfg)
style.configure("TNotebook", background='#000000');
style.map("TNotebook.Tab", background=[("selected", '#ffffff')], foreground=[("selected", '#000000')])
style.configure("TNotebook.Tab", background='#000000', foreground='#ffffff')

def toggle_sidebar(*event):
	if (not Workspace.hidden) and (popupmsg.cget('text')!=Workspace.active): Workspace.switch(popupmsg.cget('text'))
	else: Workspace.toggle_sidebar(popupmsg.cget('text'))
	if sidebar.geometry()!=sidebar.geometrylock: sidebar.geometry(sidebar.geometrylock)

def tooltip_show(x, y):
	if (x<=50): popupmsg.configure(text='Bridge')
	elif x>=(Zeta.System.Size.Screen.width - 500): popupmsg.configure(text='Monitoring')
	else: popupmsg.configure(text=selected_workspace.get())

selected_workspace = tk.StringVar()
def switch(name=''):
	if name=='': name = selected_workspace.get()
	if Workspace.hidden: Workspace.toggle_sidebar(name)
	else: Workspace.switch(name)

def addworkspace(name='', switchafter=True):
	if name=='': name = askstring('Name', 'Workspace name:')
	printable = '#[].-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/'
	name = ''.join(filter(lambda x: x in printable, name))
	Panel[name] = {'root': Taskbar.Sidebar(), 'task': Taskbar.Task()}
	wmenu.add_radiobutton(label=name, variable=selected_workspace, value=name, command=switch)
	
	path = Zeta.Utility.Format.Path('<Scraps>/workspace/matter/'+name)
	if not os.path.exists(path): os.makedirs(path)
	wpanel = Zeta.Utility.Launch.Explorer(color='green', mode='border', path=path, geometry=sidebar2.geometry(), panelgeometry='left')
	Panel[name]['root'].path = path
	Panel[name]['root'].bind('<Button-3>', lambda e: Zeta.Utility.Launch.Explorer(color='green', path=e.widget.path, geometry=Workspace.geometry['sidebar'], transient=e.widget, panelgeometry='right'))
	Zeta.System.WM.toggle_bind(Panel[name]['root'], wpanel)
	if switchafter: switch(name)

Workspace.widget = {'dragdrop': [Taskbar.DragDrop(), tk.BooleanVar(value=False)], 'console': [Taskbar.Console(), tk.BooleanVar(value=False)], 'notepad': [Taskbar.Notepad(), tk.BooleanVar(value=False)]}
def widget(name):
	if Workspace.widget[name][1].get(): Workspace.widget[name][0].show()
	else: Workspace.widget[name][0].hide()

wmenu = Menu(sidebar, tearoff=0)
wmenu.add_command(label="[ New ]", command=addworkspace)
wmenu.add_separator()
wmenu.add_radiobutton(label='Task', variable=selected_workspace, value='Task', command=switch)
wmenu.add_separator()
wmenu.add_checkbutton(label=r'Drag & Drop', command=lambda: widget('dragdrop'), variable=Workspace.widget['dragdrop'][1], onvalue=True, offvalue=False)
wmenu.add_checkbutton(label=r'Notepad', command=lambda: widget('notepad'), variable=Workspace.widget['notepad'][1], onvalue=True, offvalue=False)
wmenu.add_checkbutton(label=r'Console', command=lambda: widget('console'), variable=Workspace.widget['console'][1], onvalue=True, offvalue=False)
wmenu.add_separator()

#-------------------------------------------------------------------------------

Panel['Task']['root'] = Taskbar.Task()
Panel['Bridge']['root'] = Taskbar.Bridge()
Panel['Monitoring']['root'] = Taskbar.Monitoring()

Panel['Task']['taskbar'] = Taskbar.Task2()
Panel['Bridge']['wallpaper'] = Taskbar.Wallpaper()
Panel['Monitoring']['wallpaper'] = Taskbar.Wallpaper()

#-------------------------------------------------------------------------------

if tooltip:
	sidebar.bind("<Enter>", lambda e: tooltip_show(e.x, e.y))
	sidebar.bind('<Motion>', lambda e: tooltip_show(e.x, e.y))

sidebar.bind("<Button-1>", toggle_sidebar, add="+")
sidebar.bind("<Button-3>", lambda event: wmenu.post(event.x_root, event.y_root))
Zeta.System.WM.toggle_bind(sidebarext, sidebar2)


File2.controller = Workspace.controller



Workspace.show(Workspace.active)
sidebar.mainloop()