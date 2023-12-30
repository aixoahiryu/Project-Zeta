import Zeta
from Zeta.Panel import *

class Pattern(Window):
	def __init__(self, *args, **kwargs):
		Window.__init__(self, mode='border', color2='black', *args, **kwargs)
		self.geometry('+5+5')
		self.attributes('-topmost', True)
		self.imghdd=Zeta.Image.Icon.Load(icon='hddb', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerb', icontype='bw').image
		self.imgex=Zeta.Image.Icon.Load(icon='mathb', icontype='bw').image
		self.imgplay=Zeta.Image.Icon.Load(icon='playb', icontype='bw').image
		self.imgtext=Zeta.Image.Icon.Load(icon='textb', icontype='bw').image
		self.placeholder = ''
		self.InitWindow()
		
		Button2(self.frame, text=' Emergence', image=self.imghdd, compound='left', side='left', fill='y', hover=self._Emergence, toggle=self._Emergence, geometry='bottom')
		Frame(self.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='left', fill='y')

		self.theme(self.frame, bg=self.hue, fg=self.neon)

	def InitWindow(self):
		self.InitSubEmergence()

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text='# META', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='bottom')
		Button2(x.frame, text='[ Reference ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Ref, toggle=self._Emergence_Ref, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text='√ Experiment', image=self.imgex, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='≡ Read', image=self.imgtext, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='ᐅ Play', image=self.imgplay, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text='¦ Philosophy', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Philosophy, toggle=self._Emergence_Philosophy, geometry='right')
		Button2(x.frame, text='¦ Paranormal', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Paranormal, toggle=self._Emergence_Paranormal, geometry='right')
		Button2(x.frame, text='¦ Physical', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Physical, toggle=self._Emergence_Physical, geometry='right')
		Button2(x.frame, text='¦ Politics', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Politics, toggle=self._Emergence_Politics, geometry='right')
		Button2(x.frame, text='¦ Technology', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Tech, toggle=self._Emergence_Tech, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text='0 ¦ Core', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='1 ¦ Layers', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='2 ¦ Tree', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='3 ¦ Elements', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='4 ¦ Automata', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='5 ¦ Emergence', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='6 ¦ Fractals', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='7 ¦ Chaos', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text='Formal', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Formal, toggle=self._Emergence_Formal, geometry='right')
		Button2(x.frame, text='Natural', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Natural, toggle=self._Emergence_Natural, geometry='right')
		Button2(x.frame, text='Social', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Social, toggle=self._Emergence_Social, geometry='right')
		Button2(x.frame, text='Malice', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Malice, toggle=self._Emergence_Malice, geometry='right')
		Button2(x.frame, text='Occult', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Occult, toggle=self._Emergence_Occult, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text='Δ[ Increasement ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='Σ[ Divergent ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text='Ω[ Airlock ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence = x
		x.bind('<Button-3>', lambda e: self.rightclick(e))

	def InitSubEmergence(self):
		self.InitSub_Emergence_Ref()
		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' [ Explore ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self._Emergence_Ref_Explore, toggle=self._Emergence_Ref_Explore, geometry='right')
		Button2(x.frame, text=' [ Tools ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text=' [ List ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Ref = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' Research', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Recall', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Simulate', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Systemics', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Philosophy = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' [ 0:Self - 7:World ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text=' Theory', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Frontier', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Truth', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Paranormal = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' Combat', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Intelligence', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Stealth: lockpick, audio, visual', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Medical', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Physical = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' [ Pyramid ] [ Board ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Strategy', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Politics = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' [ Coding ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' [ Hacking ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' [ Forensics ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' [ RE ]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Tech = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' System: pattern[tree, layers, elements, fractals, automata], [structure, information, energy], [particle, wave:vibration:frequency:resonance:cymatics], entropy, cycle', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' 	Complex[nonlinearity, emergence, spontaneous order, adaptation, and feedback loops]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' 	Network[graph, contagion, scale-free, evolution]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' 	Space[phase], Time[line, attractor], Mind[game, society]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Metaphysics: quantum, cosmology, ontology, identity, causality, relativity, philosophy', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Chaos: labyrinth, kaleidoscope, echo', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text=' Cognitive: ethics, theology, behavior[gambit]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Machine: analog, computer', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Mathematics: formal, axiom[euclid], game', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Formal = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' Biology: genetic, food, medical, neurology', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Chemistry:', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Physics:', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text=' Engineering: material, fuel', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Mechanics: kinetics, force, motion, reference', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Natural = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' Geography', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' History: archaeology', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text=' Art: painting, film, story, music', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Language: linguistics', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Culture: religion, anthropology', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Social = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' Economic: corporate[mo, process, software], finance, career', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text=' Military: alliance', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Politics: gov, org, weapon, ideology, cult[freemason, zion]', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Industry: aviation, auto, energy, pharma', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		Button2(x.frame, text=' Academic: publisher, author, education, crisis', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Media: crisis, conop, propaganda, people', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Malice = x

		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button2(x.frame, text=' Psionic:', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Intent:', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Mind: egregore, deception[self-delusion], revelation', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Quantum:', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		Button2(x.frame, text=' Mathematics:', image=self.imghdd, compound='left', side='top', fill='x', hover=self.placeholder, toggle=self.placeholder, geometry='right')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Occult = x

	def InitSub_Emergence_Ref(self):
		x = Window(mode='border', color2='black')
		x.attributes('-topmost', True)
		Button(x.frame, text=' # Vector', relief='flat', image=self.corner, compound='left', anchor='w').pack(side='top', fill='x')
		Frame(x.frame, highlightbackground=self.neon, highlightthickness=1).pack(side='top', fill='x')
		x.theme(x.frame, fg=x.neon, bg=x.hue)
		self._Emergence_Ref_Explore = x

	def rightclick(self, e):
		self.winfo_toplevel().clipboard_clear()
		self.winfo_toplevel().clipboard_append(e.widget['text'])
		self.winfo_toplevel().update()