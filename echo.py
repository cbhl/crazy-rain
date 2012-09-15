from pyo import *
s = Server().boot()
sf = SfPlayer("test.wav", loop=True, mul=.3)
delay = Delay(sf, delay=[.2,.5], feedback=.7, mul=.7).out()
s.gui(locals())
