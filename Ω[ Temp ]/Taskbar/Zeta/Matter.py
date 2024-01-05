import Zeta
import Taskbar
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

Panel = {'System': {'taskbar': '', 'wallpaper': ''}, 'Taskbar': {'root': ''}, 'Extension': {'root': ''}, 'Sector': {'root': ''}}
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
width = Zeta.System.Size.Screen.width -1 -1
sidebar.geometry(f"{width}x1+0-0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)
sidebar.update()
sidebar.geometrylock = sidebar.geometry()

sidebarbump = Toplevel()
sidebarbump.attributes('-topmost', True)
sidebarbump.attributes('-alpha', 0.1)
width = Zeta.System.Size.Screen.width -1 -1
sidebarbump.geometry(f"{width}x5+0-{Zeta.System.Size.taskbar+1}")
sidebarbump.overrideredirect(1)
sidebarbump.configure(bg=colorbg)
sidebarbump.show()
# sidebarbump.bind('<Enter>', lambda e: print('bump'))
sidebarbump.bind('<Enter>', lambda e: sidebar.lift())

sidebarext = Taskbar.Sidebar()
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

taskbar = Taskbar.Taskbar()
Panel['System']['taskbar'] = taskbar
# taskbar2 = Taskbar.Taskbar2()
taskbar2 = Zeta.Panel.BufferBar()
Workspace.chdir = taskbar2.chdir
Panel['System']['taskbar2'] = taskbar2
taskbar2.geometry('+0-1')

switcher = Taskbar.Switcher()
Panel['System']['switcher'] = switcher

wallpaper = Taskbar.Wallpaper()
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
	popup.show() if Workspace.hidden else print('hidden')
	if (x<=250): (popupmsg.configure(text='Extension'),popup.geometry('+10+10'))
	elif x>=(Zeta.System.Size.Screen.width - 250): (popupmsg.configure(text='Sector'),popup.geometry('-10+10'))
	else: (popupmsg.configure(text=selected_workspace.get()),popup.geometry('+10+10'))

def tooltip_hide():
	popup.hide() if Workspace.hidden else print('hidden')


selected_workspace = tk.StringVar()
def switch(name=''):
	if name=='': name = selected_workspace.get()
	if Workspace.hidden: Workspace.toggle_sidebar(name)
	else: Workspace.switch(name)

def addworkspace(name='', switchafter=True):
	if name=='': name = askstring('Name', 'Workspace name:')
	printable = '#[].-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/'
	name = ''.join(filter(lambda x: x in printable, name))
	Panel[name] = {'root': Taskbar.Sidebar()}
	wmenu.add_radiobutton(label=name, variable=selected_workspace, value=name, command=switch)
	
	path = Zeta.Utility.Format.Path('<Scraps>/workspace/library/'+name)
	if not os.path.exists(path): os.makedirs(path)
	wpanel = Zeta.Utility.Launch.Explorer(color='green', mode='border', path=path, geometry=sidebar2.geometry(), panelgeometry='left')
	Panel[name]['root'].path = path
	Panel[name]['root'].bind('<Button-3>', lambda e: Zeta.Utility.Launch.Explorer(color='green', path=e.widget.path, geometry=Workspace.geometry['sidebar'], transient=e.widget, panelgeometry='right'))
	Zeta.System.WM.toggle_bind(Panel[name]['root'], wpanel)
	if switchafter: switch(name)

wmenu = Menu(sidebar, tearoff=0)
wmenu.add_command(label="[ New ]", command=addworkspace)
wmenu.add_separator()
wmenu.add_radiobutton(label="Taskbar", variable=selected_workspace, value="Taskbar", command=switch)
wmenu.add_separator()


#-------------------------------------------------------------------------------

class Controller():
	def toggle_sidebar(child): toggle_sidebar()
	def preview_file(child, path): wallpaper.preview_file(path)
	def chdir(): pass
Workspace.controller = Controller()

root = Taskbar.File()
wallpaper.watch = root.File1
Workspace.controller.chdir = root.File1.change_dir
Panel['Taskbar']['root'] = root
Panel['Extension']['root'] = Taskbar.Search()
Panel['Sector']['root'] = Taskbar.Lounge()

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
sidebar.bind("<Button-3>", lambda event: wmenu.post(event.x_root, event.y_root))
Zeta.System.WM.toggle_bind(sidebarext, sidebar2)


File2.controller = Workspace.controller



Workspace.show(Workspace.active)
sidebar.mainloop()