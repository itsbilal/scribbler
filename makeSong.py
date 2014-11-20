# ref.  Andrea Valle
# to use this file, just say makeFile(dictionaryOfNotes, startTime, filename)
import numpy as N
import wave
from playnote import getFrequency

def get_signal_data(frequency=440, duration=1, volume=32768, samplerate=44100):
    """Outputs a numpy array of intensities"""
    samples = duration * samplerate
    period = samplerate / float(frequency)
    omega = N.pi * 2 / period
    t = N.arange(samples, dtype=N.float)
    y = volume * N.sin(t * omega)
    return y

def numpy2string(y):
    """Expects a numpy vector of numbers, outputs a string"""
    signal = "".join((wave.struct.pack('i', item) for item in y))
    # this formats data for wave library, 'h' means data are formatted
    # as short ints
    return signal

class SoundFile:
    def  __init__(self, signal, filename, duration=1, samplerate=44100):
        self.file = wave.open(filename, 'wb')
        self.signal = signal
        self.sr = samplerate
        self.duration = duration
  
    def write(self):
        self.file.setparams((1, 2, self.sr, self.sr*self.duration, 'NONE', 'noncompressed'))
        # setparams takes a tuple of:
        # nchannels, sampwidth, framerate, nframes, comptype, compname
        self.file.writeframes(self.signal)
        self.file.close()

def makeFile(notes, startTime, filename = 'song.wav'):
    data = ""
    signal = ""
    for k in sorted(notes):
    	duration = (k - startTime)/4
        frequency = getFrequency(notes[k])
        data = get_signal_data(frequency, duration)
        signal += numpy2string(data)
        startTime = k 
    f = SoundFile(signal, filename, duration)
    f.write()
    print 'file written'

if __name__ == '__main__':
    startTime = 0
    makeFile({10:'A',20:'G'},startTime)
