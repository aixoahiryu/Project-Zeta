import Zeta
import External
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

Panel = {'System': {'taskbar': '', 'wallpaper': ''}, 'File': {'root': ''}, 'Filter': {'root': ''}, 'Network': {'root': ''}, 'Lounge': {'root': ''}}
__builtins__.Workspace = Zeta.System.WM.Workspace(Panel)
__builtins__.WorkspaceColor = 'white'
Workspace.active = ''

Workspace.geometry = {'main': '', 'sidebar': ''}
Workspace.geometry['sidebar'] = f"333x{Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25}+30+25"
Workspace.geometry['main'] = f"{Zeta.System.Size.Screen.width - 333 - 30 -5}x{Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25}-1+25"

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
sidebar.geometry(f"1x{height}+0+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)
sidebar.update()
sidebar.geometrylock = sidebar.geometry()

sidebarext = External.Sidebar()
Panel['System']['sidebarext'] = sidebarext

# sidebar2 = Toplevel(sidebar)
sidebar2 = Window(color2=WorkspaceColor, mode='border')
sidebar2.title('===[ Sidebar: File ]===')
sidebar2.attributes('-topmost', True)
sidebar2.attributes('-alpha', Zeta.Setting.opacity)
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar - 25
sidebar2.geometry(f"333x{height}-1+25")
sidebar2.overrideredirect(1)
File2 = FileBox(sidebar2.frame, home=Zeta.System.Path.Core.Sidebar, color2=WorkspaceColor, panelgeometry='left')

taskbar = External.Taskbar()
Panel['System']['taskbar'] = taskbar
# taskbar2 = External.Taskbar2()
taskbar2 = Zeta.Panel.BufferBar()
Workspace.chdir = taskbar2.chdir
Panel['System']['taskbar2'] = taskbar2

switcher = External.Switcher()
Panel['System']['switcher'] = switcher

wallpaper = External.Wallpaper()
Panel['System']['wallpaper'] = wallpaper

popup = Toplevel()
popup.title('Popup')
popup.geometry("+10+350")
popup.overrideredirect(1)
popup.attributes('-alpha', Zeta.Setting.opacity)
popup.configure(bg=colorbg)
popup.attributes('-topmost', True)
popupmsg = Label(popup, text='', bg=colorbg, fg=colorfg, font=("Lucida Console", 8, "normal"))
popupmsg.grid(sticky='NWES')

#root.tk.call("source", r"C:\Users\Administrator\Desktop\tcl\theme\Forest\void.tcl")
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
	wallpaper.preview_clipboard()
	if sidebar.geometry()!=sidebar.geometrylock: sidebar.geometry(sidebar.geometrylock)

def tooltip_show(x, y):
	#popup.show() if Workspace.hidden else print('hidden')
	if (y<=50 and x==0): popupmsg.configure(text='Network')
	# elif (y>50 and y<100): (popupmsg.configure(text='File'),popup.geometry('+10+50'))
	#elif x>=1: (popupmsg.configure(text='F'),popup.geometry('+10+10'))
	elif y>=(Zeta.System.Size.Screen.height - Zeta.System.Size.Window.mpv[1] - Zeta.System.Size.taskbar): popupmsg.configure(text='Lounge')
	else: popupmsg.configure(text=selected_workspace.get())

def tooltip_hide():
	popup.hide() if Workspace.hidden else print('hidden')

def rightclick_sidebar(x, y):
	if y<=Zeta.System.Size.Window.aimp[1]: Panel['Network']['root'].search(query=sidebar.clipboard_get(), browser='Lite')
	elif y>=(Zeta.System.Size.Screen.height - Zeta.System.Size.Window.mpv[1] - Zeta.System.Size.taskbar): wmenu.post(x, y)
	else: wmenu.post(x, y)


selected_workspace = tk.StringVar()
def switch(name=''):
	if name=='': name = selected_workspace.get()
	if Workspace.hidden: Workspace.toggle_sidebar(name)
	else: Workspace.switch(name)

def addworkspace(name='', switchafter=True):
	if name=='': name = askstring('Name', 'Workspace name:')
	printable = '#[].-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/'
	name = ''.join(filter(lambda x: x in printable, name))
	Panel[name] = {'root': External.Sidebar()}
	wmenu.add_radiobutton(label=name, variable=selected_workspace, value=name, command=switch)
	
	path = Zeta.Utility.Format.Path('<Scraps>/workspace/void/'+name)
	if not os.path.exists(path): os.makedirs(path)
	wpanel = Zeta.Utility.Launch.Explorer(color='green', mode='border', path=path, geometry=sidebar2.geometry(), panelgeometry='left')
	Panel[name]['root'].path = path
	Panel[name]['root'].bind('<Button-3>', lambda e: Zeta.Utility.Launch.Explorer(color='green', path=e.widget.path, geometry=Workspace.geometry['sidebar'], transient=e.widget, panelgeometry='right'))
	Zeta.System.WM.toggle_bind(Panel[name]['root'], wpanel)
	if switchafter: switch(name)

wmenu = Menu(sidebar, tearoff=0)
wmenu.add_command(label="[ New ]", command=addworkspace)
wmenu.add_separator()
wmenu.add_radiobutton(label="File", variable=selected_workspace, value="File", command=switch)
wmenu.add_radiobutton(label="Filter", variable=selected_workspace, value="Filter", command=switch)
wmenu.add_separator()


#-------------------------------------------------------------------------------

class Controller():
	def toggle_sidebar(child): toggle_sidebar()
	def preview_file(child, path): wallpaper.preview_file(path)
	def chdir(): pass
Workspace.controller = Controller()

root = External.File()
wallpaper.watch = root.File1
Workspace.controller.chdir = root.File1.change_dir
Panel['File']['root'] = root
Panel['Filter']['root'] = External.Filter()
Panel['Network']['root'] = External.Search()
Panel['Lounge']['root'] = External.Lounge()

# Panel['Console'] = {'root': External.Sidebar()}
# Panel['Test'] = {'root': External.Sidebar()}
# Panel['Downstream'] = {'root': External.Sidebar()}
# wmenu.add_radiobutton(label="Console", variable=selected_workspace, value="Console", command=switch)
# wmenu.add_radiobutton(label="Test", variable=selected_workspace, value="Test", command=switch)
# wmenu.add_radiobutton(label="Downstream", variable=selected_workspace, value="Downstream", command=switch)
addworkspace('Console')
addworkspace('Test')
addworkspace('Downstream')
wmenu.add_separator()

#-------------------------------------------------------------------------------

if tooltip:
	sidebar.bind("<Enter>", lambda e: tooltip_show(e.x, e.y))
	sidebar.bind('<Motion>', lambda e: tooltip_show(e.x, e.y))
	sidebar.bind("<Leave>", lambda e: tooltip_hide())
	sidebar.bind("<Button-1>", lambda e: tooltip_hide())

sidebar.bind("<Button-1>", toggle_sidebar, add="+")
sidebar.bind("<Button-3>", lambda e: rightclick_sidebar(e.x, e.y))
# Workspace.toggle_bind(sidebarext, sidebar2)
Zeta.System.WM.toggle_bind(sidebarext, sidebar2)

# taskbar.bind("<Enter>", lambda e: root.hide())
# taskbar.bind("<Button-1>", lambda event: Workspace.hide(Workspace.active))
# sidebarext.bind("<Button-1>", lambda event: Workspace.hide(Workspace.active), add="+")

File2.controller = Workspace.controller



Workspace.show(Workspace.active)
sidebar.mainloop()