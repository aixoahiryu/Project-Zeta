import Zeta
import os

def Path(raw, home=os.path.abspath(os.sep)):
	data = raw
	data = data.replace(r'<Home>', home)
	data = data.replace(r'<Zeta>', Zeta.System.Path.Core.ZETA)
	data = data.replace(r'<X>', Zeta.System.Path.Core.X)
	data = data.replace(r'<Scraps>', Zeta.System.Path.Scraps.path)
	data = data.replace(r'<Resource>', Zeta.System.Path.Scraps.resource)
	data = data.replace(r'<Downstream>', Zeta.System.Path.Core.downstream2)
	if Zeta.System.OS.Windows: data = data.replace('/', '\\')
	return data