# from inspect import getfile, getfullargspec
# from functools import wraps

# def runtime(f):
# 	filename = getfile(f)
# 	defaults = getfullargspec(f)[-1]
# 	@wraps(f)
# 	def wrapped(*args, **kwargs):
# 		for k, v in defaults.items():
# 			if k not in kwargs:
# 				kwargs[k] = v()
# 		return f(*args, **kwargs)
# 	# and return it
# 	return wrapped

from . import Color
from . import Image
from . import Setting
from . import System

from . import Error
from . import Raw

from . import Panel
from . import Utility

