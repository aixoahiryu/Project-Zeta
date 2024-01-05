import Zeta
from .Vector import Vector
from .Sector import Sector
from .Toolbox import Toolbox

import webbrowser
import os
import subprocess
import pathlib
from tkinter import *
import tkinter.ttk as ttk

from natsort import os_sorted

hidden = False
# cwd = os.getcwd()
cwd = Zeta.System.Path.Core.downstream2 + r'/Zeta/Interface/External/Network/Search'

colorbg = "#000000"
colorfg = "#ffffff"

from Zeta.Panel import *

class Search(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='white', *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacity)
		self.geometry("333x333+30+25")
		self.frame.grid_columnconfigure(1, weight=1)
		self.frame.grid_rowconfigure(1, weight=1)

		Button(self.frame, text='≡', command=self.search).grid(sticky='NSEW', column=0, row=0)

		frame1 = Frame(self.frame, bg=colorbg)
		frame1.grid(sticky='NSEW', column=0, row=1)
		Button(frame1, text='G', command=self.search).grid(sticky='N', row=0)
		Button(frame1, text='Y', command=self.search).grid(sticky='N', row=1)
		Button(frame1, text='B', command=self.search).grid(sticky='N', row=2)
		ttk.Separator(frame1, orient='horizontal').grid(sticky='EW', row=3)
		Button(frame1, text='yt', command=self.search).grid(sticky='N', row=4)

		frame2 = Frame(self.frame, bg=colorbg)
		frame2.grid(sticky='NSEW', column=1, row=1, ipady=10, ipadx=10)
		frame2.grid_columnconfigure(0, weight=1)
		frame2.grid_rowconfigure(3, weight=1)
		self.searchbox2 = Entry(frame2)
		self.searchbox2.grid(sticky='NSEW', row=0)
		self.searchbox2.bind('<Return>', lambda e: self.search())
		self.searchbox3 = Entry(frame2)
		self.searchbox3.grid(sticky='NSEW', row=1)
		self.searchbox3.bind('<Return>', lambda e: self.search())

		engineframe = Frame(frame2)
		engineframe.grid(sticky='NSEW', row=2)
		self.enginebox = ttk.Combobox(engineframe, state="readonly")
		self.enginebox.configure(values=['Google','Yandex','Bing'])
		self.enginebox.set('Google')
		self.enginebox.pack(side='left', fill='x')
		self.browserbox = ttk.Combobox(engineframe, state="readonly")
		self.browserbox.configure(values=['Browser','Lite','[Crawler]'])
		self.browserbox.set('Lite')
		self.browserbox.pack(side='left', fill='x')

		fileframe = Frame(frame2, bg=colorbg)
		fileframe.grid(sticky='NSEW', row=3)
		fileframe.grid_columnconfigure(1, weight=1)
		fileframe.grid_rowconfigure(0, weight=1)
		self.list1 = Listbox(fileframe)
		self.list1.grid(sticky='NSEW', row=0, column=0)
		self.list2 = Listbox(fileframe)
		self.list2.grid(sticky='NSEW', row=0, column=1)
		self.list1.bind('<Double-1>', self.change_file)
		self.list1.bind('<Button-3>', self.edit_file)
		self.list2.bind('<Double-1>', self.change_filter)

		self.searchbox = Entry(self.frame)
		self.searchbox.grid(sticky='NSEW', column=1, row=0)
		self.searchbox.bind('<Return>', lambda e: self.search())
		self.searchbox.bind('<Shift-Return>', lambda e: self.search(query=self.searchbox.get(), browser='Lite'))
		self.searchbox.bind('<Control-Return>', lambda e: self.search(engine='Google'))
		self.searchbox.bind('<Alt-Return>', lambda e: self.search(browser='Browser'))

		filelist = [x for x in os.listdir(cwd) if not os.path.isdir(os.path.join(cwd, x))]
		filelist = os_sorted(filelist)
		for item in filelist:
			self.list1.insert(END, item)

		Vector().transient(self)
		Sector().transient(self)
		Toolbox().transient(self)

		self.theme(self.frame, bg='#000000', fg='#ffffff')
		self.bind('<Expose>', lambda e: self.exposed())
		self.searchbox.bind('<Enter>', lambda e: self.exposed())
		self.searchbox2.bind('<Enter>', lambda e: self.searchbox2.focus())
		self.searchbox3.bind('<Enter>', lambda e: self.searchbox3.focus())


	def engine(self, id):
		print(id)
		search()

	def search(self, query='', engine='', browser='', *event):
		if query=='': query=self.searchbox2.get()+' '+self.searchbox.get()+' '+self.searchbox3.get()
		if engine=='': engine=self.enginebox.get()
		if browser=='': browser=self.browserbox.get()
		engineset = {'Google': 'https://www.google.com/search?q=%s&num=100&nfpr=1&hl=en-US&gl=US&filter=0&safe=off',\
		'Yandex': 'https://yandex.com/search/?text=%s',\
		'Bing': 'https://www.bing.com/search?q=%s',\
		}
		browserset = {'Browser': Zeta.System.Path.Browser().main, 'Lite': Zeta.System.Path.Browser().lite}
		subprocess.Popen([browserset[browser], engineset[engine] % query], start_new_session=True)
		# webbrowser.open(engine[self.enginebox.get()] % searchstr, new=2, autoraise=True)
		# webbrowser.open(r'https://www.google.com/search?q='+self.searchbox.get()+' '+self.searchbox2.get()+' '+self.searchbox3.get()+r'&num=100&nfpr=1', new=2, autoraise=True)

		if Zeta.Setting.module['raw']: Zeta.Raw.Network.Search(f'{engine} {browser}: {query}')

	def change_file(self, *event):
		self.list2.delete(0, END)
		picked = self.list1.get(self.list1.curselection()[0])
		path = os.path.join(cwd, picked)
		file = open(path, mode='r')
		filecontent = file.read()
		file.close()
		filecontent = filecontent.split("\n")
		for item in filecontent:
			self.list2.insert(END, item)

	def edit_file(self, *event):
		picked = self.list1.get(self.list1.curselection()[0])
		path = os.path.join(cwd, picked)
		os.startfile(path)

	def change_filter(self, *event):
		picked = self.list2.get(self.list2.curselection()[0])
		self.searchbox3.delete(0, END)
		self.searchbox3.insert(0, picked)

	def exposed(self):
		self.searchbox.focus()
		self.searchbox.selection_range(0, END)

# https://developers.google.com/custom-search/docs/xml_results