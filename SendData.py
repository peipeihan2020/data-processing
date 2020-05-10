"""Example program to demonstrate how to send a multi-channel time series to
LSL."""

import time
from random import random as rand
import  mne

from pylsl import StreamInfo, StreamOutlet
import numpy

# first create a new stream info (here we set the name to BioSemi,
# the content-type to EEG, 8 channels, 100 Hz, and float-valued data) The
# last value would be the serial number of the device or some other more or
# less locally unique identifier for the stream as far as available (you
# could also omit it but interrupted connections wouldn't auto-recover)
gaze = numpy.load('pupil/gaze_timestamps.npy')
raw = mne.io.read_raw_brainvision('eeg/P3_S5_T3_I1.vhdr', preload=True)
data, sf, chan = raw._data, raw.info['sfreq'], raw.info['ch_names']
chanel_count = len(chan)
data_type = str(data.dtype)
info = StreamInfo('BrainVision', 'EEG', chanel_count, 100, 'float32', 'myuid34234')

# next make an outlet
outlet = StreamOutlet(info)

print("now sending data...")
data_length = data.shape[1]
while True:
    for i in range(data_length):
        # make a new random 8-channel sample; this is converted into a
        # pylsl.vectorf (the data type that is expected by push_sample)
        mysample = data[:,i].astype('float32')
        # now send it and wait for a bit
        outlet.push_sample(mysample)
        time.sleep(0.01)
