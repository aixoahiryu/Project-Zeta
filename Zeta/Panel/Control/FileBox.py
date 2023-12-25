import Zeta
from Zeta.Panel import Window

import time
import os
import glob
import subprocess
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted


# ZLCORE = os.environ['ZLCORE']
ZLCORE = Zeta.System.Path.Core.ZLCORE
#os.chdir(home)


class Controller():
	def toggle_sidebar(child): print('toggled')
	def preview_file(child, path): print(path)

class FileBox(Frame):
	def __init__(self, master, controller=None, home='', darkmode=True, fileicon=False, color2='', neonmode=False, workspace='', dryrun=False, safemode=False, panelgeometry='right'):
		self.home = os.path.abspath(os.sep) if home=='' else Zeta.Utility.Format.Path(home)
		if not os.path.exists(self.home): os.makedirs(self.home)
		self.fullpath = self.home
		self.controller = controller if controller!=None else Controller()
		self.window = master.winfo_toplevel()
		self.workspace = workspace
		self.dialog = ''
		self.newFileName = StringVar(master, "", 'new_name')
		self.dryrun = dryrun
		self.safemode = safemode
		self.panelgeometry = panelgeometry

		self.color2 = color2
		# self.color2 = 'green' if color2 in ['', 'white'] else color2
		# self.darkmode = darkmode
		# self.neonmode = neonmode = False if color2 in ['white', 'black'] else True
		fgcolor = 'white' if ('dark' in Zeta.Color.Neon(self.color2).raw) else 'black'
		bgcolor = 'black' if ('dark' in Zeta.Color.Neon(self.color2).raw) else 'white'
		neon = Zeta.Color.Neon(self.color2).hex
		hue = Zeta.Color.Neon(self.color2).hue
		tint = Zeta.Color.Neon(self.color2).tint
		# neonhue = Zeta.Color.Neon(self.color2).tint
		# neonhue = Zeta.Color.Neon(self.color2).tint if neonmode else Zeta.Color.Neon(self.color2).hue
		# self.colorbg = "black" if darkmode else "white"
		# self.colorbg2 = neonhue if darkmode else neon
		# self.colorfg = "white" if darkmode else "black"
		# self.colorfg2 = neon if darkmode else "black"
		# if darkmode & neonmode: self.colorbg=Zeta.Color.Neon(self.color2).hue
		# self.buttoncolor = neon if neonmode else self.colorfg
		# self.buttonrelief = 'flat' if neonmode else 'raised'
		# self.colorname = 'black' if darkmode==False else self.color2

		style = ttk.Style()
		theme = style.theme_use()
		if theme!='alt':
			style.theme_use('alt')
		if (style.configure(f"{self.color2}.Treeview")==None):
			style.configure(f"{self.color2}.Treeview", background=hue, foreground=fgcolor, fieldbackground=hue)
			style.map(f"{self.color2}.Treeview", background=[('selected', tint)], foreground=[('selected', neon)])
			# style.configure("TCombobox", background=bgcolor, foreground=fgcolor, fieldbackground=bgcolor, highlightcolor=fgcolor, arrowcolor=fgcolor)
			# style.map("TCombobox", background=[('readonly', bgcolor)], foreground=[('readonly', fgcolor)], fieldbackground=[('readonly', bgcolor)], highlightcolor=[('readonly', fgcolor)], arrowcolor=[('readonly', fgcolor)] )
			style.configure(f"{self.color2}.TCombobox", background=hue, foreground=fgcolor, fieldbackground=hue, highlightcolor=fgcolor, arrowcolor=fgcolor)
			style.map(f"{self.color2}.TCombobox", background=[('readonly', hue)], foreground=[('readonly', fgcolor)], fieldbackground=[('readonly', hue)], highlightcolor=[('readonly', fgcolor)], arrowcolor=[('readonly', fgcolor)] )
			# style.configure(f"TScrollbar", background=bgcolor, foreground=fgcolor, fieldbackground=bgcolor, highlightcolor=fgcolor, troughcolor=bgcolor, arrowcolor=fgcolor)
			# style.configure(f"{self.color2}.TScrollbar", background=hue, foreground=fgcolor, fieldbackground=bgcolor, highlightcolor=fgcolor, troughcolor=bgcolor, arrowcolor=fgcolor)
			style.configure(f"{self.color2}.Vertical.TScrollbar", background=hue, foreground=fgcolor, fieldbackground=hue, highlightcolor=fgcolor, troughcolor=hue, arrowcolor=fgcolor)
			style.configure(f"{self.color2}.Horizontal.TScrollbar", background=hue, foreground=fgcolor, fieldbackground=hue, highlightcolor=fgcolor, troughcolor=hue, arrowcolor=fgcolor)
			style.configure("Menu", background=bgcolor, foreground=fgcolor, fieldbackground=bgcolor, highlightcolor=fgcolor)
		# if neonmode and (style.configure("neon.Treeview")==None):
		# 	style.configure("neon.Treeview", background=self.colorbg, foreground=self.colorfg, fieldbackground=self.colorbg)
		# 	style.map('neon.Treeview', background=[('selected', self.colorbg2)], foreground=[('selected', self.colorfg2)])

		master.grid_columnconfigure(1, weight=1)
		master.grid_rowconfigure(1, weight=1)
		Button(master, text='≡', command=self.goHome).grid(sticky='NSEW', column=0, row=0)

		frame1 = Frame(master)
		frame1.grid(sticky='NSEW', column=0, row=1)
		button1 = Button(frame1, text='∆', command=self.goBack)
		button2 = Button(frame1, text='X', command=self.goBack)
		button1.grid(sticky='N', row=0)
		button2.grid(sticky='N', row=1)
		#button1.place(relx=0, rely=0, relwidth=0.1, relheight=0.1)
		Frame.__init__(self, master)
		self.grid(sticky='NSEW', column=1, row=1)

		#Entry(master, textvariable=currentPath, fg=self.colorfg)
		frame3 = Frame(master)
		frame3.grid(sticky='NSEW', column=1, row=0)
		frame3_1 = Frame(frame3)
		frame3_1.grid(sticky='W', row=0, column=0)
		metapath = os.path.join(self.home, '# META')
		metapath = os.path.join(metapath, r'Ω[ FileBox ].txt')
		if not os.path.isfile(metapath): metapath = Zeta.System.Path.Core().ZETA + '/Panel/Control/FileBox.txt'
		with open(metapath, encoding='utf-8') as f:
			data = f.read()
		data = Zeta.Utility.Format.Path(data, self.home)
		# data = data.replace(r'<Home>', self.home)
		# data = data.replace(r'<X>', Zeta.System.Path.Core.X)
		# data = data.replace(r'<Scraps>', Zeta.System.Path.Scraps.path)
		# data = data.replace(r'<Downstream>', Zeta.System.Path.Core.downstream2)
		self.metadata = data.split('-------------')
		for i in filter(None, self.metadata[0].split('\n')):
			if i == '---': Label(frame3_1, text='¦').pack(side='left')
			else:
				btntemp = Button(frame3_1, text=i.split('|')[0])
				btntemp.pack(side='left')
				btntemp.btnpath = i.split('|')[1]
				btntemp.bind('<Button-1>', lambda e: self.goPath(e.widget.btnpath))
				btntemp.bind('<Button-3>', lambda e: self.rightclick_detach(e.widget.btnpath))
		# Button(frame3_1, text='C', command=lambda: self.goPath('C:\\')).grid(sticky='W', row=0, column=0)
		# Button(frame3_1, text='D', command=lambda: self.goPath('D:\\')).grid(sticky='W', row=0, column=1)
		# Label(frame3_1, text='|').grid(sticky='W', row=0, column=2)
		# Button(frame3_1, text='╬', command=lambda: self.goPath(r'D:\MEGA\ZL-Core\Commit\╬')).grid(sticky='W', row=0, column=3)
		# Button(frame3_1, text=' _ ', command=lambda: self.goPath('D:\\_')).grid(sticky='W', row=0, column=4)
		# Button(frame3_1, text='Data', command=lambda: self.goPath('D:\\Data')).grid(sticky='W', row=0, column=5)
		# Button(frame3_1, text='Core', command=lambda: self.goPath('D:\\ZL-Core')).grid(sticky='W', row=0, column=6)
		# Button(frame3_1, text='Scraps', command=lambda: self.goPath('D:\\Scraps')).grid(sticky='W', row=0, column=7)
		frame3_2 = Frame(frame3)
		frame3_2.grid(sticky='E', row=0, column=1)
		frame3.grid_columnconfigure(1, weight=1)
		self.combo1 = ttk.Combobox(frame3_2, state="readonly", values=['--------------'], width=10, takefocus=0, style=f"{self.color2}.TCombobox")
		self.combo1.grid(sticky='E', row=0, column=0)
		self.combo1.bind('<Button-3>', lambda e: self.combo1.configure(state="normal"))
		self.combo1.bind('<Button-1>', lambda e: self.workspace_select())
		self.combo1.bind('<<ComboboxSelected>>', lambda e: self.workspace_select())

		self.vsb = ttk.Scrollbar(self, orient="vertical", style=f"{self.color2}.Vertical.TScrollbar")
		self.hsb = ttk.Scrollbar(self, orient="horizontal", style=f"{self.color2}.Horizontal.TScrollbar")
		self.tree = ttk.Treeview(self, columns=("fullpath", "type", "size"), show="tree", style=f"{self.color2}.Treeview",
		# self.tree = ttk.Treeview(self, columns=("fullpath", "type", "size"), show="tree", style="neon.Treeview" if neonmode else "self.Treeview",
			displaycolumns="size", yscrollcommand=lambda f, l: self.autoscroll(self.vsb, f, l),
			xscrollcommand=lambda f, l:self.autoscroll(self.hsb, f, l))
		self.vsb['command'] = self.tree.yview
		self.hsb['command'] = self.tree.xview
		self.tree.grid(column=0, row=0, sticky='NSEW')
		self.vsb.grid(column=1, row=0, sticky='ns')
		self.hsb.grid(column=0, row=1, sticky='ew')
		self.grid_columnconfigure(0, weight=1)
		self.grid_rowconfigure(0, weight=1)

		self.tree.heading("#0", text="Directory Structure", anchor='w')
		self.tree.heading("size", text="File Size", anchor='w')
		self.tree.column("size", stretch=0, width=0)
		#tree['show'] = ('headings', 'tree')

		self.populate_masters(self.tree)
		self.tree.bind('<<TreeviewOpen>>', self.update_tree)
		self.tree.bind('<Double-Button-1>', self.change_dir)
		self.tree.bind('<Return>', self.change_dir)
		self.tree.bind('<ButtonRelease-1>', self.selectItem)
		self.winfo_toplevel().tree = self.tree


		#menubar = Menu(master, tearoff=0, background='#ffffff', foreground='#000000', activebackground='#000000', activeforeground='#ffffff')
		menubar = Menu(master, tearoff=0)
		menubar.add_command(label="View", command=self.editor)
		menubar.add_command(label="New", command=self.open_popup)
		menubar.add_separator()
		menubar.add_command(label="Open", command=lambda: (self.controller.toggle_sidebar(), Zeta.System.OS.open(self.fullpath)))
		#subedit = Menu(menubar, tearoff=0)
		#menubar.add_cascade(label="Edit", menu=subedit, command=menu_edit)
		menubar.add_command(label="Edit", command=lambda: (self.controller.toggle_sidebar(), Zeta.System.OS.edit(self.fullpath)))
		subexecute = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Execute", menu=subexecute)
		subexecute.add_command(label="System", command=lambda: Zeta.System.OS.launch(self.fullpath))
		subexecute.add_command(label="Browser", command=lambda: Zeta.System.OS.launch(self.fullpath, 'browser'))
		subexecute.add_separator()
		subexecute.add_command(label="Python", command=lambda: Zeta.System.OS.launch(self.fullpath, 'python'))
		menubar.add_separator()
		menubar.add_command(label="Select", command=self.menu_select)
		menubar.add_command(label="Copy path", command=lambda: (self.window.clipboard_clear(),self.window.clipboard_append(self.fullpath),self.window.update()))
		menubar.add_command(label="Go to path", command=lambda: self.menu_select(self.window.clipboard_get()))
		self.imgterm = Zeta.Image.Icon.Load('termbw', 'bw').image
		menubar.add_command(label="Terminal", image=self.imgterm, compound='left', command=lambda: (self.controller.toggle_sidebar(), Zeta.System.OS.terminal(self.fullpath)))
		self.imgdetach = Zeta.Image.Icon.Load('windowbw', 'bw').image
		menubar.add_command(label="Detach", image=self.imgdetach, compound='left', command=self.menu_detach)
		menubar.add_separator()
		self.imgworkspace = Zeta.Image.Icon.Load('calc', 'neon').image
		if self.workspace!='': menubar.add_command(label="Workspace", image=self.imgworkspace, compound='left', command=self.menu_workspace)
		# menubar.add_command(label="Test", command=lambda e: print(e.widget))
		#menubar.add_command(label="Exit", command=menu_clear)
		#menubar.add_command(label="Exit", command=master.quit)
		#master.config(menu=menubar)
		self.tree.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))
		self.winfo_toplevel().theme(master, bg=hue, fg=neon, relief='flat')

	def menu_select(self, path=''):
		node = self.tree.focus()
		if self.tree.parent(node):
			if path!='': self.fullpath = path
			if os.path.isfile(self.fullpath): self.fullpath = os.path.split(self.fullpath)[0]
			self.tree.delete(self.tree.get_children(''))
			self.populate_masters(self.tree)

	def menu_detach(self):
		import Zeta.Panel
		panelcolor = self.color2 #if self.neonmode else self.colorfg
		path = self.fullpath if os.path.isdir(self.fullpath) else os.path.split(self.fullpath)[0]

		#detached = Zeta.Panel.Window(border='mono', color2=panelcolor, mode='basic')
		detached = Zeta.Panel.Window(color2=self.color2, title=os.path.split(path)[1])
		detached.attributes('-topmost', True)
		# detached.geometry(f"+{25+10+333}+25")
		Zeta.System.WM.geocalc(detached, self, 'right', self.winfo_toplevel())
		detached.attributes('-alpha', Zeta.Setting.opacity)
		detached.transient(self.window)
		Zeta.Panel.FileBox(detached.frame, color2=self.color2, home=path, controller=self.controller)#, darkmode=self.darkmode, neonmode=self.neonmode)
		detached.show()

	def rightclick_detach(self, path):
		self.fullpath = path
		self.menu_detach()

	def menu_workspace(self):
		if os.path.isfile(self.fullpath): return
		self.workspace.path = self.fullpath
		self.workspace.chdir(self.fullpath)

	def menu_clear():
		#os.execv(sys.argv[0], sys.argv)
		os.execv(sys.executable, ['python'] + sys.argv)

	def selectItem(self, a):
		selectedfocus = self.tree.focus()
		selecteditem = self.tree.item(selectedfocus)
		self.fullpath = selecteditem.get('values')[0]
		self.controller.preview_file(self.fullpath)

	def populate_tree(self, tree, node):
		if tree.set(node, "type") != 'directory':
			return

		path = tree.set(node, "fullpath")
		tree.delete(*tree.get_children(node))

		parent = tree.parent(node)
		#special_dirs = [] if parent else glob.glob('.') + glob.glob('..')
		special_dirs = []

		dirlist = [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
		filelist = [x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))]
		dirlist = os_sorted(dirlist)
		filelist = os_sorted(filelist)

		for i in dirlist:
			fname = os.path.split(i)[1]
			i = os.path.join(path, i)
			#folderimg = PhotoImage(file=ZLCORE+r"/Toolbar/_/[ Program ]/[ Source ]/gif/neon/folder.gif")
			#id = tree.insert(node, "end", text=fname, values=[i, "directory"], image=folderimg)
			id = tree.insert(node, "end", text=fname, values=[i, "directory"])
			tree.insert(id, 0, text="dummy")
			tree.item(id, text=fname)

		for i in filelist:
			fname = os.path.split(i)[1]
			i = os.path.join(path, i)
			id = tree.insert(node, "end", text=fname, values=[i, "file"])
			size = os.stat(i).st_size
			tree.set(id, "size", "%d bytes" % size)

		# for p in special_dirs + os.listdir(path):
		#	 ptype = None
		#	 p = os.path.join(path, p).replace('\\', '/')
		#	 if os.path.isdir(p): ptype = "directory"
		#	 elif os.path.isfile(p): ptype = "file"

		#	 fname = os.path.split(p)[1]
		#	 id = tree.insert(node, "end", text=fname, values=[p, ptype])

		#	 if ptype == 'directory':
		#		 if fname not in ('.', '..'):
		#			 tree.insert(id, 0, text="dummy")
		#			 tree.item(id, text=fname)
		#	 elif ptype == 'file':
		#		 size = os.stat(p).st_size
		#		 tree.set(id, "size", "%d bytes" % size)

	def populate_masters(self, tree):
		#dir = os.path.abspath('.').replace('\\', '/')
		dir = self.fullpath
		node = tree.insert('', 'end', text=dir, values=[dir, "directory"], open=True)
		self.populate_tree(tree, node)

	def update_tree(self, event):
		tree = event.widget
		self.populate_tree(tree, tree.focus())

	def change_dir(self, event):
		if self.dryrun: return
		tree = event.widget
		node = tree.focus()
		if tree.parent(node):
			path = os.path.abspath(tree.set(node, "fullpath"))
			if os.path.isfile(path):
				if path.endswith(('.txt', '.py', '.bat')): self.editor()
				else:
					if not self.safemode: os.startfile(path)
			# if os.path.isdir(path):
			# 	os.chdir(path)
			# 	tree.delete(tree.get_children(''))
			# 	populate_masters(tree)

	def autoscroll(self, sbar, first, last):
		first, last = float(first), float(last)
		if first <= 0 and last >= 1:
			sbar.grid_remove()
		else:
			sbar.grid()
		sbar.set(first, last)

	def goBack(self, event=None):
		self.fullpath = self.tree.item(self.tree.get_children('')).get('values')[0]
		#self.goPath(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))
		self.goPath(os.path.abspath(os.path.join(self.fullpath, os.pardir)))

	def goHome(self, event=None):
		self.goPath(self.home)

	def goPath(self, path):
		self.fullpath = path
		self.tree.delete(self.tree.get_children(''))
		self.populate_masters(self.tree)

	def open_popup(self):
		self.newFileName.set('')
		# colorfg = 'white' if self.darkmode else 'black'
		# colorbg = 'black' if self.darkmode else 'white'

		self.dialog = Zeta.Panel.Window(color2=self.color2, mode='basic', title='Create file')
		# self.dialog.geometry(f"+{25+10+333}+25")
		Zeta.System.WM.geocalc(self.dialog, self, 'right', self.winfo_toplevel())
		self.dialog.attributes('-topmost', True)
		#self.dialog.attributes('-alpha', Zeta.Setting.opacity)
		self.dialog.resizable(False, False)
		self.dialog.title("New")
		self.dialog.transient(self.window)
		self.dialog.columnconfigure(0, weight=1)
		Label(self.dialog.frame, text='Enter File or Folder name').grid()
		Entry(self.dialog.frame, textvariable=self.newFileName).grid(column=0, sticky='NSEW')
		btnframe = Frame(self.dialog.frame)
		btnframe.grid(column=0, sticky='NSEW')
		Button(btnframe, text="Time", command=lambda: self.newFileName.set( str(round(time.time())) )).pack(side=LEFT)
		Button(btnframe, text="TXT", command=lambda: self.newFileName.set(self.newFileName.get()+'.txt')).pack(side=LEFT)
		Button(btnframe, text="[  ]", command=lambda: self.newFileName.set(r'[ '+self.newFileName.get()+r' ]')).pack(side=LEFT)
		Button(btnframe, text=" ¦ ", command=lambda: self.newFileName.set(self.newFileName.get()+r' ¦ ')).pack(side=LEFT)
		Button(btnframe, text=" √ ", command=lambda: self.newFileName.set(r'√ ')).pack(side=LEFT)
		Button(btnframe, text=" ≡ ", command=lambda: self.newFileName.set(r'≡ ')).pack(side=LEFT)
		Button(btnframe, text=" ▷ ", command=lambda: self.newFileName.set(r'▷ ')).pack(side=LEFT)
		Button(btnframe, text=" Δ ", command=lambda: self.newFileName.set(r'Δ[ '+self.newFileName.get()+r' ]')).pack(side=LEFT)
		Button(btnframe, text=" Σ ", command=lambda: self.newFileName.set(r'Σ[ '+self.newFileName.get()+r' ]')).pack(side=LEFT)
		Button(btnframe, text=" Ω ", command=lambda: self.newFileName.set(r'Ω[ '+self.newFileName.get()+r' ]')).pack(side=LEFT)
		Button(btnframe, text="Create", command=self.newFileOrFolder).pack(side=LEFT)
		self.dialog.theme(target=self.dialog.frame, bg=Zeta.Color.Neon(self.color2).hue, fg=Zeta.Color.Neon(self.color2).hex)
		self.dialog.show()

	def newFileOrFolder(self):
		if os.path.isdir(self.fullpath): fullpath2 = self.fullpath
		if os.path.isfile(self.fullpath): fullpath2 = os.path.split(self.fullpath)[0]
		if len(self.newFileName.get().split('.')) != 1:
			open(os.path.join(fullpath2, self.newFileName.get()), 'w').close()
		else:
			os.makedirs(os.path.join(fullpath2, self.newFileName.get()))
		self.dialog.destroy()
		if os.path.isdir(self.fullpath): self.populate_tree(self.tree, self.tree.focus())
		else: self.populate_tree(self.tree, self.tree.parent(self.tree.focus()))

	#currentPath = StringVar(master, name='currentPath', value=pathlib.Path.cwd())
	#currentPath.trace('w', pathChange)

	def workspace_select(self):
		self.combo1.configure(state="readonly")

		content = list(filter(None, self.metadata[1].split('\n')))
		# file = open(ZLCORE+r'\Toolbar\F\[ Workspace ]\[ Sidebar ]\Internal.txt', mode='r')
		# filecontent = file.read()
		# file.close()
		# filecontent = filecontent.split("\n")
		# self.combo1['values'] = filecontent
		self.combo1['values'] = content[1:]

		# combo1.configure(width=len(combo1.get())+1)
		# self.fullpath = ZLCORE+'\\Toolbar\\F\\[ Workspace ]\\[ Sidebar ]\\'+self.combo1.get()
		self.fullpath = os.path.join(content[0], self.combo1.get())
		if os.path.isdir(self.fullpath):
			self.tree.delete(self.tree.get_children(''))
			self.populate_masters(self.tree)

	def editor(self):
		editor = Zeta.Utility.Launch.Editor(path=self.fullpath, color=self.color2, title=os.path.split(self.fullpath)[1])
		editor.transient(self.winfo_toplevel())
		# if self.panelgeometry!='right': editor.geometry('333x333')
		Zeta.System.WM.geocalc(editor, self, self.panelgeometry, self.winfo_toplevel())


class FilePanel(Window):
	def __init__(self, title='', mode='basic', color2='green', home='', neonmode=False, panelgeometry='right', *args, **kargs):
		if title=='': title = os.path.split(home)[1]
		Window.__init__(self, title=title, mode=mode, color2=color2, *args, **kargs)
		FileBox(self.frame, home=home, color2=color2, panelgeometry=panelgeometry)

		# self.theme(self.frame, fg=self.neon, bg=self.hue, relief='flat')

if __name__ == '__main__':
	FilePanel(title='File panel', home=r'D:\_\Interface').mainloop()