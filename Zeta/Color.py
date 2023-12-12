class Neon():
	def __init__(self, color2='', color=7):
		self._color = ['#000000', '#FF0C12', '#FDAE32', '#FDFB00', '#5CFF00', '#00CFFB', '#8F00F2', '#ffffff']
		self._name1 = {'format': ['fg', 'bg', 'tint']}
		# self._name1 = {'black': ['#000000', '#dddddd', '#333333'], 'white': ['#ffffff', '#111111', '#cccccc']}
		self._name1['black'] = ['#000000', '#ffffff', '#eeeeee', 'light', 'mono']
		self._name1['white'] = ['#ffffff', '#000000', '#666666', 'dark', 'mono']
		self._name1['red'] = ['#fa5a5a', '#471a1a', '#5c2121', 'dark']
		self._name1['orange'] = ['#FF5F1F', '#401808', '#5c220b', 'dark']
		self._name1['yellow'] = ['#FFCC00', '#362b00', '#4f3f00', 'dark']
		self._name1['green'] = ['#6effbe', '#253B34', '#335247', 'dark']
		self._name1['blue'] = ['#00FFFF', '#014040', '#015c5c', 'dark']
		self._name1['purple'] = ['#bc13fe', '#2a0538', '#3f0854', 'dark']

		# --------------------------Extension---------------------------
		self._name1['nier'] = [Nier.foreground, Nier.background, Nier.tint, 'light', 'mono']
		self._name1['ink'] = [Ink.foreground, Ink.background, Ink.tint, 'light', 'mono']
		self._name1['quantum'] = [Quantum.foreground, Quantum.background, Quantum.tint, 'light', 'mono']
		# --------------------------------------------------------------

		self.hex = self._color[color]
		if color2 != '':
			self.colorname = color2
			self.fgcolor = 'white' if ('dark' in self._name1[color2]) else 'black'
			self.bgcolor = 'black' if ('dark' in self._name1[color2]) else 'white'
			self.hex = self._name1[color2][0]
			self.hue = self._name1[color2][1]
			self.tint = self._name1[color2][2]
			self.raw = self._name1[color2]

class Gradient():
	def __init__(self, color=7, color2=''):
		self._index = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']
		index = self._index[color]
		self._color = {'pink': ['#ffafbd', '#ffc3a0']}
		self._color['red'] = ['#ff512f', '#dd2476']
		self._color['orange'] = ['#eb3349', '#f45c43']
		self._color['yellow'] = ['#ff5f6d', '#ffc371']
		self._color['green'] = ['#56ab2f', '#a8e063']
		self._color['blue'] = ['#2193b0', '#6dd5ed']
		self._color['purple'] = ['#cc2b5e', '#753a88']
		self._color['black'] = ['#141e30', '#243b55']
		self._color['white'] = ['#bdc3c7', '#2c3e50']
		if color2 != '': index = color2
		self.array = self._color[index]

class Smoke():
	background = '#D4D4D4'
	foregroundb = '#474747'
	foregroundw = '#d8d8d8'

class Nier():
	background = '#D7D1B9'
	foreground = '#4D4940'
	tint = '#B4AF9B'
	orange = '#B55B47'
	blue = '#3C9794'

class Ink():
	background = '#B2CBC2'
	foreground = '#004706'
	tint = '#5C9983'

class Quantum():
	foreground = '#5B6F70'
	background = '#EDEDEB'
	tint = '#515151'
	red = '#B4255A'
	orange = '#FF6B02'
	yellow = '#CEB002'
	green = '#59C323'
	blue = '#04B3DD'
	purple = '#664FA1'