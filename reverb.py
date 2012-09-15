from pyo import *
s = Server().boot()
sf = SfPlayer("flute.aif", loop=True, mul=.4).mix(3).out()
delay = Delay(sf, delay=[.012,.0307,.0511,.0701,.091], feedback=.1, mul=.4).out()
delay2 = Delay(sf, delay=[.101, .147, .198, .220, .251], feedback = .05, mul=.4).out()
s.gui(locals())
