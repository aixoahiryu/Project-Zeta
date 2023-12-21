import builtins
from .Icon import Load

def bw():
	builtins.imgtermbw = Load('termbw', 'bw').image
	builtins.imgdetachbw = Load('windowbw', 'bw').image
