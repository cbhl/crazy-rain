from pyo import *
f="test.wav"
s = Server().boot()
sf = SfPlayer(f, loop=True)
wgv = WGVerb(sf, feedback=[.74], cutoff=4500, bal=.3, mul=.3).out()
s.gui(locals())
