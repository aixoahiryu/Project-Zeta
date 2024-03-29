import Zeta
import Internal
from Zeta.Panel import *
import tkinter.ttk as ttk

import webbrowser
import os

from natsort import os_sorted


ZLCORE = os.environ['ZLCORE']

addicon = False
darkmode = False
tooltip = True
colorbg = "#000000" if darkmode else "#ffffff"
colorbg2 = "#253B34" if darkmode else "#6effbe"
colorfg = "#ffffff" if darkmode else "#000000"

Panel = {'System': {'taskbar': '', 'wallpaper': ''}, 'Monolith': {'root': ''}, 'Command': {'root': ''}, 'Launch': {'root': ''}, 'Whiteboard': {'root': ''}}
__builtins__.Workspace = Zeta.System.WM.Workspace(Panel)
Workspace.active = ''

Workspace.geometry = {'main': '', 'sidebar': ''}
Workspace.geometry['sidebar'] = f"333x{Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar -5 -5}+5+5"
Workspace.geometry['main'] = f"{Zeta.System.Size.Screen.width - 333 -5 -10}x{Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar -5 -5}-5+5"

sidebar = Tk()
sidebar.attributes('-topmost', True)
sidebar.attributes('-alpha', 0.1)
sidebar.title('1px')
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
sidebar.geometry(f"1x{height}-0+0")
sidebar.overrideredirect(1)
sidebar.configure(bg=colorbg)
sidebar.update()
sidebar.geometrylock = sidebar.geometry()

sidebarext = Toplevel(sidebar)
sidebarext.attributes('-topmost', True)
sidebarext.attributes('-alpha', 0.1)
sidebarext.title('1ext')
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
sidebarext.geometry(f"1x{height}+0+0")
sidebarext.overrideredirect(1)
sidebarext.configure(bg=colorbg)
Panel['System']['sidebarext'] = sidebarext

taskbar = Internal.Taskbar()
Panel['System']['taskbar'] = taskbar

wallpaper = Toplevel(sidebar)
wallpaper.title('Wallpaper')
width = Zeta.System.Size.Screen.width
height = Zeta.System.Size.Screen.height - Zeta.System.Size.taskbar
wallpaper.geometry(f"{width}x{height}+0+0")
wallpaper.overrideredirect(1)
wallpaper.configure(bg=colorbg)
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
style.configure("TNotebook", background='#ffffff', borderwidth=0);
style.map("TNotebook.Tab", background=[("selected", '#000000')], foreground=[("selected", '#ffffff')])
style.configure("TNotebook.Tab", background='#ffffff', foreground='#000000')

def toggle_sidebar(*event):
	Workspace.toggle_sidebar(popupmsg.cget('text'))
	if sidebar.geometry()!=sidebar.geometrylock: sidebar.geometry(sidebar.geometrylock)	
	# if sidebarext.on: Zeta.System.WM.toggle(sidebarext)
	# if btnoverflow.on: Zeta.System.WM.toggle(btnoverflow)

def rightclick_sidebar(x, y):
	if y<=Zeta.System.Size.Window.aimp[1]: Zeta.System.OS.edit('<Downstream>')
	elif y>=(Zeta.System.Size.Screen.height - Zeta.System.Size.Window.mpv[1] - Zeta.System.Size.taskbar): Zeta.System.OS.launch('<X>/Null/[ Program ]/Utility/Link.py')
	else: Workspace.toggle_sidebar('Whiteboard')

def tooltip_show(x, y):
	#popup.show() if hidden else print(e)
	if Workspace.hidden:
		if y<=Zeta.System.Size.Window.aimp[1]: popupmsg.configure(text='Monolith')
		#elif x>=1: (popupmsg.configure(text='_'),popup.geometry('-10+10'),popup.show())
		elif y>=(Zeta.System.Size.Screen.height - Zeta.System.Size.Window.mpv[1] - Zeta.System.Size.taskbar): popupmsg.configure(text='Launch')
		else: popupmsg.configure(text='Command')

def tooltip_hide():
	popup.hide() if Workspace.hidden else print('hidden')

#-------------------------------------------------------------------------------

def menu_clear():
	#os.execv(sys.argv[0], sys.argv)
	os.execv(sys.executable, ['python'] + sys.argv)

Panel['Launch']['root'] = Internal.Launch()
Panel['Monolith']['root'] = Internal.Monolith()
Panel['Command']['root'] = Internal.Command()
Panel['Whiteboard']['root'] = Internal.Whiteboard()

#-------------------------------------------------------------------------------

if tooltip:
	sidebar.bind("<Enter>", lambda e: tooltip_show(e.x, e.y))
	sidebar.bind('<Motion>', lambda e: tooltip_show(e.x, e.y))
	sidebar.bind("<Leave>", lambda e: tooltip_hide())
	sidebar.bind("<Button-1>", lambda e: tooltip_hide())

sidebar.bind("<Button-1>", toggle_sidebar, add="+")
sidebar.bind("<Button-3>", lambda e: rightclick_sidebar(e.x, e.y), add="+")
# Workspace.toggle_bind(sidebarext, sidebar2)
# sidebarext.bind("<Button-1>", lambda event: Workspace.hide(Workspace.active), add="+")


#taskbar.bind("<Enter>", lambda e: root.hide())



Workspace.show(Workspace.active)
sidebar.mainloop()