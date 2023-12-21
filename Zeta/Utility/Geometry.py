import Zeta

def calc(parent, child, geometry='right', anchor='widget', always=False):
	if always: child.tile = [child, parent, geometry, anchor]
	else: Zeta.System.WM.geocalc(child, parent, geometry, anchor)