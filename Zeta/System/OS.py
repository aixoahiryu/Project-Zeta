import Zeta

import os
import subprocess
import platform

Windows = True if platform.system() == 'Windows' else False
Linux = True if platform.system() == 'Linux' else False
Mac = True if platform.system() == 'Darwin' else False

def launch(fullpath, program='', custom=''):
	tools = {'browser': Zeta.System.Path.Browser.main, 'lite': Zeta.System.Path.Browser.lite}
	tools['editor'] = Zeta.System.Path.Editor.main
	tools['sidebar'] = Zeta.System.Path.Editor.sidebar
	tools['python'] = Zeta.System.Path.Execute.python
	if program=='': os.startfile(fullpath)
	else: subprocess.Popen([tools[program]+' '+custom, fullpath], start_new_session=True)

def open(fullpath):
	if os.path.isfile(fullpath): path = os.path.split(fullpath)[0]
	else: path = fullpath
	os.startfile(path)
	#subprocess.Popen(r'explorer /select,"C:\xampp"')

def edit(fullpath):
	subprocess.Popen([Zeta.System.Path.Editor.main, fullpath], start_new_session=True)
	#os.startfile(r'C:\Program Files\Sublime Text 3\sublime_text.exe '+fullpath)

def terminal(fullpath):
	if os.path.isfile(fullpath): path = os.path.split(fullpath)[0]
	else: path = fullpath
	
	if Windows: subprocess.Popen(r'cmd /k cd /d '+path)
