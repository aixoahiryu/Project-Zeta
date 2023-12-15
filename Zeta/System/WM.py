import Zeta

def transparent(root):
	if Zeta.System.OS.Windows: root.wm_attributes("-transparentcolor", "white")
	if Zeta.System.OS.Linux: root.configure(bg='')
	if Zeta.System.OS.Mac: (root.wm_attributes("-transparent", True), root.config(bg='systemTransparent'))


def geocalc(child, widget, geometry, anchor='widget'):
	ref = widget if anchor=='widget' else anchor
	if not isinstance(ref, Zeta.Panel.Toplevel): anchor = 'widget'

	left = ref.winfo_rootx() if anchor=='widget' else ref.winfo_x()
	top = ref.winfo_rooty() if anchor=='widget' else ref.winfo_y()
	width = ref.winfo_width()
	height = ref.winfo_height()
	cwidth = child.winfo_width()
	cheight = child.winfo_height()
	# if geometry=='right': child.geometry(f'+{ref.winfo_x() + ref.winfo_width() +5}+{ref.winfo_y()}')
	# elif geometry=='bottom': child.geometry(f'+{ref.winfo_x()}+{ref.winfo_y() + ref.winfo_height() +5}')
	# elif geometry=='top': child.geometry(f'+{ref.winfo_x()}+{ref.winfo_y() - child.winfo_height() -5}')
	# elif geometry=='left': child.geometry(f'+{ref.winfo_x() - child.winfo_width() -5}+{ref.winfo_y()}')

	if geometry=='right':
		left = left + width +5
		top = top
	elif geometry=='bottom':
		left = left
		top = top + height +5
	elif geometry=='top':
		left = left
		top = top - cheight -5
	elif geometry=='left':
		left = left - cwidth -5
		top = top

	if (left+cwidth) > Zeta.System.Size.Screen.width: left = Zeta.System.Size.Screen.width - cwidth
	if (top+cheight) > Zeta.System.Size.Screen.height: top = Zeta.System.Size.Screen.height - cheight
	if left < 0: left = 0
	if top < 0: top = 0

	# print(f'{ref.winfo_x()}:{ref.winfo_y()} | {child.winfo_height()}:{child.winfo_width()} > {left}:{top}')

	result = f'+{left}+{top}'
	child.geometry(result)
	return result


def toggle_hide(master):
	for i in master.toggle: i.hide()

def toggle_show(master):
	if master.stay:
		for i in master.toggle: i.show()
		master.on = True

def toggle(master, manual):
	if master.on:
		for i in master.toggle: i.hide()
	else:
		for i in master.toggle: i.show()
	
	master.on = not master.on
	if hasattr(master, 'stay') and manual: master.stay = master.on

	if manual and (isinstance(master, Zeta.Panel.Button) or isinstance(master, Zeta.Panel.Label)):
		tempcolor = master['background']
		master['background'] = master['foreground']
		master['foreground'] = tempcolor

def toggle_bind(master, child, button='<Button-1>', stay=True, escape=False, geometry='', anchor='widget'):
	# if isinstance(master, Zeta.Panel.Toplevel): child.transient(master)
	if not hasattr(master, 'toggle'):
		master.toggle = []
		master.on = False
		master.bind(button, lambda e: toggle(master, True), add="+")

		# if geometry!='': master.bind('<Button-1>', lambda e: geocalc(child, e.widget, geometry, anchor), add="+")
		if geometry!='': child.tile=[child, master, geometry, anchor] #if child.tile==[] else master.bind('<Button-1>', lambda e: geocalc(child, e.widget, geometry, anchor), add="+")
		
		if not escape: master.winfo_toplevel().bind('<<hide>>', lambda e: toggle_hide(master), add="+")
		if stay:
			master.stay = False
			master.winfo_toplevel().bind('<<show>>', lambda e: toggle_show(master), add="+")

	if isinstance(child, list): master.toggle = child
	else: master.toggle.append(child)
	child.protocol( 'WM_DELETE_WINDOW' , lambda: toggle_unbind(master, child))

def toggle_unbind(master, child):
	master.toggle.remove(child)


def hover_show(master):
	for i in master.hover: i.show()

def hover_hide(master):
	if hasattr(master, 'on') and master.on: return
	for i in master.hover: i.hide()

def hover_stay(master, widget):
	if hasattr(master, 'on') and master.on: return
	if widget in master.hover:
		for i in master.hover: i.hide()

def hover_bind(master, child, stay=False, geometry='', anchor='widget'):
	# if isinstance(master, Zeta.Panel.Toplevel): child.transient(master)
	if not hasattr(master, 'hover'):
		master.hover = []
		master.bind('<Enter>', lambda e: hover_show(master), add="+")

		# if geometry!='': master.bind('<Enter>', lambda e: geocalc(child, e.widget, geometry, anchor), add="+")
		if geometry!='': child.tile=[child, master, geometry, anchor] #if child.tile==[] else master.bind('<Enter>', lambda e: geocalc(child, e.widget, geometry, anchor), add="+")
		
		master.winfo_toplevel().bind('<<hide>>', lambda e: hover_hide(master), add="+")
		if stay: child.bind('<Leave>', lambda e: hover_stay(master, e.widget), add="+")
		else: master.bind('<Leave>', lambda e: hover_hide(master), add="+")

	if isinstance(child, list): master.hover = child
	else: master.hover.append(child)
	child.protocol( 'WM_DELETE_WINDOW' , lambda: hover_unbind(master, child))

def hover_unbind(master, child):
	master.hover.remove(child)


class Workspace():
	def __init__(self, panel):
		# Panel = {'System': {'taskbar': '', 'wallpaper': ''}, 'File': {'root': ''}, 'Network': {'root': ''}, 'Lounge': {'root': ''}}
		self.panel = panel
		self.active = ''
		self.hidden = False
		self.controller = ''
		self.path = ''

		self.toggle = []
		self.hover = []

	def toggle_sidebar(self, group=''):
		if self.hidden:
			if group=='': return
			self.show('System')
			self.show(group)
			# if group=='': self.show(self.active)
			# else: self.show(group)
		else:
			self.hide(self.active)
			self.hide('System')
			for master in self.hover: hover_hide(master)
			for master in self.toggle:
				if master.on: toggle(master, False)
			
		self.hidden = not self.hidden

	def switch(self, group):
		if self.hidden: self.toggle_sidebar(group)
		else:
			self.hide(self.active)
			self.show(group)

	def hide(self, group=''):
		if group=='':
			for g in self.panel.values():
				for w in g.values(): w.hide()
		else:
			for w in self.panel[group].values(): w.hide()

	def show(self, group=''):
		if group=='': group = 'System'
		for w in self.panel[group].values(): w.show()
		if group!='System': self.active = group

	def toggle_bind(self, master, child, stay=False, geometry=''):
		self.toggle.append(master)
		toggle_bind(master, child, stay=stay, geometry=geometry)

	def hover_bind(self, master, child, stay=False):
		self.hover.append(master)
		hover_bind(master, child, stay=stay)