from pyo import *
s = Server().boot()
sf = SfPlayer("flute.aif", loop=True, mul=1).out()
s.gui(locals())
