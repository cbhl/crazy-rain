from pyo import *
s = Server().boot()
sf = SfPlayer("test.wav", loop=True, mul=.3).out()
s.gui(locals())
