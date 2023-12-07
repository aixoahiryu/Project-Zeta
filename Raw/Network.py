import Zeta

class Search():
	def __init__(self, data):
		path = Zeta.System.Path.Scraps().path + r'/raw/search.txt'
		with open(path, 'a+') as target:
			target.write(data)
			target.write('\n')