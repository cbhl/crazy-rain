from pyo import *
s = Server().boot()
sf = SfPlayer("/Users/mavericklee/Desktop/test.wav", loop=True, mul=.3)
harm = Harmonizer(sf, transpo=-5, winsize=0.05).out()
s.gui(locals())
