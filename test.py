from pyo import *
import subprocess
import time

s = Server().boot()
s.start()
sf = SfPlayer("test.wav", loop=True, mul=.3)
info = sndinfo("test.wav")
harm = Harmonizer(sf, transpo=-5, winsize=0.05).out()
rec = Record(harm, filename="saved-samples/altered.wav", fileformat=0, sampletype=1)
clean = Clean_objects(info[1], rec)
clean.start()

# this is kindof a hack to prevent it from
# converting to mp3 right away
time.sleep(info[1])

# mp3 conversion
wav = 'saved-samples/altered.wav'
cmd = 'lame --preset insane %s' % wav
subprocess.call(cmd, shell=True)
