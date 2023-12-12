import Zeta
import inspect
import os

class Core():
	ZLCORE = r'D:\MEGA\ZL-Core'
	ZETA = os.path.split(inspect.getfile(Zeta))[0]
	X = os.path.join(os.path.split(ZETA)[0], 'X')
	downstream = r'D:\ZL-Core'
	downstream2 = os.path.join(os.path.split(ZETA)[0], 'ZL-Core')

	# Sidebar = r'D:\ZL-Core\Toolbar\_\[ Sidebar ]'
	# Planner = r'D:\MEGA\ZL-Core\Commit\_'
	Void = X+r'\Void\[ Workspace ]\╬'
	Planner = X+r'\Null\Planner'
	Sidebar = downstream2+r'\X\Void\# META\Sidebar'
	Commit = X+r'\Void\[ Workspace ]\Commit'

class Execute():
	python = 'py -B'

class Editor():
	main = r'C:\Program Files\Sublime Text 3\sublime_text.exe'
	sidebar = r'C:\Program Files\Notepad++\notepad++.exe'

class Browser():
	main = r'C:\Users\Administrator\AppData\Local\Chromium\Application\chrome.exe' # --disk-cache-size=0 --force-dark-mode --media-cache-size=0 --profile-directory="Default" --process-per-site
	experiment = r'D:\Tools\Vivaldi\Application\vivaldi.exe' # --disk-cache-size=0 --force-dark-mode --media-cache-size=0 --process-per-site
	lite = r'C:\Program Files\Links\links-g.exe'

class Scraps():
	path = r'D:\Scraps'

class Resource():
	mp3 = r'D:\MP3'
	video = r'D:\Temp'

	data = r'D:\Data'
	politics = r'C:\Users\Administrator\Desktop\P'
	shared = r'D:\Shared'

	furry = r'D:\Furry\Archive'