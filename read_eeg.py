import mne

# Import the BrainVision data into an MNE Raw object
raw = mne.io.read_raw_brainvision('eeg/P3_S5_T3_I1.vhdr', preload=True)
data, sf, chan = raw._data, raw.info['sfreq'], raw.info['ch_names']
print('finshed')
