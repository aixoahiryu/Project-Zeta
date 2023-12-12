import Zeta
from Zeta.Panel import *
import os

class BufferBar(Toplevel):
	def __init__(self, *args, **kwargs):
		Toplevel.__init__(self, *args, **kwargs)
		self.attributes('-topmost', True)
		self.attributes('-alpha', Zeta.Setting.opacityneon)
		self.title('Task bar')
		width = Zeta.System.Size.Screen.width
		height = Zeta.System.Size.taskbar
		self.geometry(f"{width}x{height}+0-0")
		self.overrideredirect(1)

		self.imgmenu=Zeta.Image.Icon.Load(icon='menuw', icontype='bw').image
		self.imghdd=Zeta.Image.Icon.Load(icon='hddw', icontype='bw').image
		self.corner=Zeta.Image.Icon.Load(icon='cornerw', icontype='bw').image
		self.imgex=Zeta.Image.Icon.Load(icon='mathw', icontype='bw').image
		self.imgplay=Zeta.Image.Icon.Load(icon='playw', icontype='bw').image
		self.imgtext=Zeta.Image.Icon.Load(icon='textw', icontype='bw').image
		self.imgfolder=Zeta.Image.Icon.Load(icon='tabw', icontype='bw').image

		# Workspace.chdir = self.chdir
		
		self.frame1 = Frame(self)
		self.frame1.pack(side='left', fill='both')
		self.frame2 = Frame(self)
		self.frame2.pack(side='right', fill='both')

		Button2(self.frame1, image=self.imgmenu, side='left', fill='y', geometry='top')
		Label(self.frame1, text='# [ ').pack(side='left', fill='y')
		Button2(self.frame1, text='META', side='left', fill='y', geometry='top', buffer=['Core', 'Vector', 'Tools', '|', 'Instinct'])
		Button2(self.frame1, text='Root', side='left', fill='y', geometry='top', buffer=['Requirement', 'Specification', '|', 'Idea', 'Methodology'])
		Button2(self.frame1, text='Search', side='left', fill='y', geometry='top', buffer=['[ Engine ]', '|', 'Keyword', 'Variant'])
		Button2(self.frame1, text='Link', side='left', fill='y', geometry='top', buffer=['Main', 'Repository', '|', 'Blackmarket'])
		Label(self.frame1, text=' ]').pack(side='left', fill='y')
		Button2(self.frame1, text='[ Note ]', side='left', fill='y', geometry='top', buffer=['Internal', '|', 'Shared', 'People'])
		Button2(self.frame1, text='[ Reference ]', side='left', fill='y', geometry='top', buffer=['Documentation', 'Research', 'Case study', '|', 'Book'])
		Button2(self.frame1, text='[ Network ]', side='left', fill='y', geometry='top', buffer=['Articles', 'Forums', 'Q & A', 'Tutorial', '|', 'Anonymous'])
		Button2(self.frame1, text=' Folder', image=self.imgfolder, compound='left', side='left', fill='y', geometry='top', exclude=[])
		Button2(self.frame1, text=' File', image=self.imgtext, compound='left', side='left', fill='y', geometry='top', exclude=[])

		Button2(self.frame2, image=self.imgmenu, command= lambda: Workspace.hide(Workspace.active), side='right', fill='y', geometry='top')
		btnairlock = Button2(self.frame2, text='Ω[ Airlock ]', side='right', fill='y', geometry='top')
		btnscraps = Button2(self.frame2, text='Σ[ Scraps ]', side='right', fill='y', geometry='top')
		Label(self.frame2, text=' ]').pack(side='right', fill='y')
		btnraw = Button2(self.frame2, text='Raw', side='right', fill='y', geometry='top', buffer=['History', 'Resource', 'Download'])
		btnfile = Button2(self.frame2, text='File', side='right', fill='y', geometry='top', buffer=['Scraps', 'Sandbox'])
		Label(self.frame2, text='Δ[ ').pack(side='right', fill='y')
		Button2(self.frame2, text=' Journal', image=self.imghdd, compound='left', side='right', fill='y', geometry='top')
		Button2(self.frame2, image=self.imgplay, side='right', fill='y', geometry='top', buffer=['Mindset', 'Ambient'])
		Button2(self.frame2, image=self.imgtext, side='right', fill='y', geometry='top', buffer=['Learn', 'Alternative'])
		Button2(self.frame2, image=self.imgex, side='right', fill='y', geometry='top', buffer=['Project', 'Sticky'])

		self.theme(self, bg='#000000', fg='#ffffff')

	def chdir(self, path):
		for child in self.winfo_children(): child.destroy()
		self.frame1 = Frame(self)
		self.frame1.pack(side='left', fill='both')
		self.frame2 = Frame(self)
		self.frame2.pack(side='right', fill='both')
		self.folder = Zeta.Utility.Launch.Explorer(color='white', mode='border', path=path, geometry=Workspace.geometry['sidebar'])
		self.folder.hide()

		if path!='' and (not os.path.exists(path+'/# Framework')): os.makedirs(path+'/# Framework')
		leftmenu = Button2(self.frame1, image=self.imgmenu, side='left', fill='y', geometry='top')
		Label(self.frame1, text='# [ ').pack(side='left', fill='y')
		Button2(self.frame1, text='META', side='left', fill='y', geometry='top', buffer=['Core', 'Vector', 'Tools', '|', 'Instinct'], path=path+'/# Framework/#META')
		Button2(self.frame1, text='Root', side='left', fill='y', geometry='top', buffer=['Requirement', 'Specification', '|', 'Idea', 'Methodology'], path=path+'/# Framework/#Root')
		Button2(self.frame1, text='Search', side='left', fill='y', geometry='top', buffer=['[ Engine ]', '|', 'Keyword', 'Variant'], path=path+'/# Framework/#Search')
		Button2(self.frame1, text='Link', side='left', fill='y', geometry='top', buffer=['Main', 'Repository', '|', 'Blackmarket'], path=path+'/# Framework/#Link')
		Label(self.frame1, text=' ]').pack(side='left', fill='y')
		Button2(self.frame1, text='[ Note ]', side='left', fill='y', geometry='top', buffer=['Internal', '|', 'Shared', 'People'], path=path+'/# Framework/[ Note ]')
		Button2(self.frame1, text='[ Reference ]', side='left', fill='y', geometry='top', buffer=['Documentation', 'Research', 'Case study', '|', 'Book'], path=path+'/# Framework/[ Reference ]')
		Button2(self.frame1, text='[ Network ]', side='left', fill='y', geometry='top', buffer=['Articles', 'Forums', 'Q & A', 'Tutorial', '|', 'Anonymous'], path=path+'/# Framework/[ Network ]')
		Button2(self.frame1, text=' Folder', image=self.imgfolder, compound='left', side='left', fill='y', geometry='top', exclude=[], path=path)
		Button2(self.frame1, text=' File', image=self.imgtext, compound='left', side='left', fill='y', geometry='top', exclude=[], path=path)

		rightmenu = Button2(self.frame2, image=self.imgmenu, command= lambda: Workspace.hide(Workspace.active), side='right', fill='y', geometry='top')
		btnairlock = Button2(self.frame2, text='Ω[ Airlock ]', side='right', fill='y', geometry='top', path=path+'/# Framework/Ω[ Airlock ]')
		btnscraps = Button2(self.frame2, text='Σ[ Scraps ]', side='right', fill='y', geometry='top', path=path+'/# Framework/Σ[ Scraps ]')
		Label(self.frame2, text=' ]').pack(side='right', fill='y')
		btnraw = Button2(self.frame2, text='Raw', side='right', fill='y', geometry='top', buffer=['History', 'Resource', 'Download'], path=path+'/# Framework/Δ[ Raw ]')
		btnfile = Button2(self.frame2, text='File', side='right', fill='y', geometry='top', buffer=['Scraps', 'Sandbox'], path=path+'/# Framework/Δ[ File ]')
		Label(self.frame2, text='Δ[ ').pack(side='right', fill='y')
		Button2(self.frame2, text=' Journal', image=self.imghdd, compound='left', side='right', fill='y', geometry='top', path=path+'/# Framework/Journal')
		Button2(self.frame2, image=self.imgplay, side='right', fill='y', geometry='top', buffer=['Mindset', 'Ambient'], path=path+'/# Framework/▷ Play')
		Button2(self.frame2, image=self.imgtext, side='right', fill='y', geometry='top', buffer=['Learn', 'Alternative'], path=path+'/# Framework/≡ Read')
		Button2(self.frame2, image=self.imgex, side='right', fill='y', geometry='top', buffer=['Project', 'Sticky'], path=path+'/# Framework/√ Experiment')

		self.theme(self, bg='#000000', fg='#ffffff')
		Workspace.toggle_bind(leftmenu, self.folder)
		# btnscraps['foreground'] = Zeta.Color.Neon('green').hex
		# btnfile['foreground'] = Zeta.Color.Neon('yellow').hex
		# btnraw['foreground'] = Zeta.Color.Neon('yellow').hex
		# btnairlock['foreground'] = Zeta.Color.Neon('red').hex
