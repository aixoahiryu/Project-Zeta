def read(path):
	with open(path, 'r+', encoding='utf-8') as target:
		content = target.read()
	return content

def write(path, content):
	f = open(path, "w", encoding="utf-8")
	f.write(content)
	f.close()