import Zeta
from Zeta.Panel import *

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfilename

import os
import time

class TextBox(Frame):
	def __init__(self, master, file='', darkmode=True, richtext=False, color2='', neonmode=False):
		Frame.__init__(self, master)
		self.pack(fill='both', expand=True)
		file = Zeta.Utility.Format.Path(file)
		# self.text = ScrolledText(self, height=30, wrap='none', tabs='0.5c', undo=True, setgrid=True, pady=2, padx=3, font=("Lucida Console", 8, "normal"))
		# self.text.pack(fill='both', expand=True) # in_=
		textContainer = tk.Frame(self)
		self.text = tk.Text(textContainer, wrap="none", undo=True, tabs='0.5c', font=("Lucida Console", 8, "normal"), highlightthickness=0, borderwidth=0)
		textVsb = ttk.Scrollbar(textContainer, orient="vertical", command=self.text.yview)
		textHsb = ttk.Scrollbar(textContainer, orient="horizontal", command=self.text.xview)
		self.text.configure(yscrollcommand=lambda f, l: self.autoscroll(textVsb, f, l), xscrollcommand=lambda f, l:self.autoscroll(textHsb, f, l))
		self.text.grid(row=0, column=0, sticky="nsew")
		textVsb.grid(row=0, column=1, sticky="ns")
		textHsb.grid(row=1, column=0, sticky="ew")
		textContainer.grid_rowconfigure(0, weight=1)
		textContainer.grid_columnconfigure(0, weight=1)
		textContainer.pack(side="top", fill="both", expand=True)
		self.text.bind("<Tab>", self.tab_pressed)

		self.path = ''
		if file!='': self.read(file)

		self.text.bind('<Control-o>', lambda e: self.open())
		self.text.bind('<Control-e>', lambda e: self.edit(self.path))
		self.text.bind('<Control-r>', lambda e: self.read(self.path))
		self.text.bind('<Control-s>', lambda e: self.save(self.path))
		# self.text.bind('<Control-w>', lambda e: self.winfo_toplevel().close())
		self.text.bind('<Alt-r>', lambda e: self.read_only())
		self.text.bind('<Control-p>', lambda e: (self.winfo_toplevel().clipboard_clear(),self.winfo_toplevel().clipboard_append(self.path),self.winfo_toplevel().update()))
		self.text.bind('<Alt-v>', lambda e: Zeta.System.OS.edit(self.scraps))
		# self.text.bind('<Alt-v>', lambda e: os.startfile(self.scraps))
		self.text.bind('<w>', lambda e: self.wrap())
		self.text.bind('<l>', lambda e: self.os('lite'))
		self.text.bind('<b>', lambda e: self.os('browser'))
		self.text.bind('<e>', lambda e: self.os('editor'))
		self.text.bind('<s>', lambda e: self.os('sidebar'))

		self.wordwrap = tk.StringVar(value=self.text['wrap'])
		self.readonly = tk.StringVar(value=self.text['state'])
		menubar = Menu(self, tearoff=0)
		menubar.add_command(label="Launch", command=self.os)
		menubar.add_command(label="Edit", command=lambda: self.edit(self.path))
		menubar.add_separator()
		subbrowser = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Browser", menu=subbrowser)
		subbrowser.add_command(label="Main", command=lambda: self.os('browser'))
		subbrowser.add_command(label="Lite", command=lambda: self.os('lite'))
		subeditor = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Editor", menu=subeditor)
		subeditor.add_command(label="Editor", command=lambda: self.os('editor'))
		subeditor.add_command(label="Sidebar", command=lambda: self.os('sidebar'))
		subformat = Menu(menubar, tearoff=0)
		menubar.add_cascade(label="Format", menu=subformat)
		subformat.add_command(label="Tab")
		menubar.add_separator()
		self.imgver = Zeta.Image.Icon.Load('historybw', 'bw').image
		menubar.add_command(label="Version", image=self.imgver, compound='left', command=lambda: Zeta.System.OS.edit(self.scraps))
		menubar.add_checkbutton(label="Wordwrap", command=self.wrap, variable=self.wordwrap, onvalue='word', offvalue='none')
		menubar.add_checkbutton(label="Read-only", command=self.read_only, variable=self.readonly, onvalue='disabled', offvalue='normal')
		self.text.bind("<Button-3>", lambda event: menubar.post(event.x_root, event.y_root))

	def autoscroll(self, sbar, first, last):
		first, last = float(first), float(last)
		if first <= 0 and last >= 1:
			sbar.grid_remove()
		else:
			sbar.grid()
		sbar.set(first, last)

	def tab_pressed(self, event:tk.Event) -> str:
	    self.text.insert("insert", " "*4)
	    return "break"

	def open(self):
		path = askopenfilename() #filetypes=validFileTypes, initialdir=initialdir
		self.read(path)

	def read(self, path):
		if path=='': return

		self.text['state'] = 'normal'
		self.path = path
		if not os.path.isfile(self.path): return
		with open(path, 'r+', encoding='utf-8') as target:
			content = target.read()
			self.text.delete('1.0', 'end')
			self.text.insert('end', content)
		self.text['state'] = 'disabled'
		# self.readonly.set(self.text['state'])
		self.version()

	def edit(self, path):
		if path!='': Zeta.System.OS.edit(path)

	def wrap(self):
		if self.text['state']=='normal': return
		if self.text['wrap']=='none': self.text['wrap'] = 'word'
		else: self.text['wrap'] = 'none'
		self.wordwrap.set(self.text['wrap'])

	def read_only(self):
		if self.text['state']=='normal': self.text['state'] = 'disabled'
		else: self.text['state'] = 'normal'
		self.readonly.set(self.text['state'])

	def os(self, program=''):
		if self.text['state']=='normal': return
		Zeta.System.OS.launch(self.text.selection_get(), program)

	def save(self, path):
		if path=='': return
		os.makedirs(os.path.dirname(path), exist_ok=True)
		f = open(path, "w", encoding="utf-8")
		f.write(self.text.get('1.0', 'end-1c'))
		f.close()
		self.version()

	def version(self):
		if self.path=='': return
		if self.path.startswith(Zeta.System.Path.Scraps.path): return
		scraps = self.path
		scraps = scraps.replace(':', '')
		scraps = scraps.replace('\\', '/')
		scraps = Zeta.Utility.Format.Path('<Scraps>/version/'+scraps)
		self.scraps = scraps

		if not os.path.isdir(scraps):
			os.makedirs(scraps)
			self.save(f"{scraps}/{str(round(time.time()))}.txt")
		else:
			lastfile = f"{scraps}/{os.listdir(scraps)[-1]}"
			last = Zeta.Utility.File.read(lastfile)
			current = self.text.get('1.0', 'end-1c')
			if last!=current: self.save(f"{scraps}/{str(round(time.time()))}.txt")
		# os.startfile(scraps)


class TextPanel(Window):
	def __init__(self, mode='basic', color2='green', file='', *args, **kargs):
		Window.__init__(self, mode=mode, color2=color2, *args, **kargs)
		self.geometry("444x444")
		maintext = TextBox(self.frame, file=file)

		self.theme(self.frame, fg=self.neon, bg=self.hue)

if __name__ == '__main__':
	TextPanel(title='Text panel', file=r'D:\_\Interface\Void.py').mainloop()