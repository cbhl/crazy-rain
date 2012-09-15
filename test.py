from pyo import *
import subprocess
import time

s = Server(duplex=0, audio="offline").boot()
dur = info = sndinfo("test.wav")[1]
s.recordOptions(dur=dur, filename="saved-samples/altered.wav", fileformat=0, sampletype=1)

# processing
sf = SfPlayer("test.wav", loop=True, mul=.3)
harm = Harmonizer(sf, transpo=-5, winsize=0.05).out()

s.start()

# mp3 conversion
wav = 'saved-samples/altered.wav'
cmd = 'lame --preset insane %s' % wav
subprocess.call(cmd, shell=True)
