from pyo import *
s = Server().boot()
s.start()
sf = SfPlayer("test.wav", loop=True, mul=.3)
info = sndinfo("test.wav")
harm = Harmonizer(sf, transpo=-5, winsize=0.05).out()
rec = Record(harm, filename="altered.wav", fileformat=0, sampletype=1)
clean = Clean_objects(info[1], rec)
clean.start()
