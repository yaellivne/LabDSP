import matplotlib.pyplot as plt
import scipy.signal as signal
import numpy as np
import scipy.io.wavfile as wavefile
import pyaudio

# read audio signal from file
sample_rate, x = wavefile.read(r'C:\Studies\Year4\SemesterA\Lab - DSP\Exp2\audiofile.wav')
Nsig = np.size(x)
# calculate FFT
X = np.abs(np.fft.fft(x))
t = np.arange(Nsig) / sample_rate
f = np.arange(0, Nsig) / Nsig * sample_rate
# plot signal

fig1, ax1 = plt.subplots(1, 1, figsize=[5, 4])

ax1.plot(t, x)
ax1.grid()
ax1.set(xlim=[t[0], t[-1]], xlabel='t [sec]', title='audio signal')

# plot FFT
fig2, ax2 = plt.subplots(1, 1, figsize=[5, 4])
ax2.plot(f, 20 * np.log10(X))
ax2.grid()
ax2.set(xlim=[f[0], f[-1]], ylim=(ax2.get_ylim()[1] - [120, 0]),
        xlabel='f [Hz]', title='FFT of audio signal')

fir_lpf = np.array(8 * [1 / 8])

y = signal.lfilter(fir_lpf, 1, x.astype(float))
ax1.plot(t, y)
Y = np.abs(np.fft.fft(y))

w, H = signal.freqz(fir_lpf, 1)
fig3, ax3 = plt.subplots(1, 1, figsize=[5, 4])
ax3.plot(w * sample_rate / (2 * np.pi), np.abs(H))
ax3.set(
    xlabel='f [Hz]', title='FIR Frequency response')
# play audio to speakers/headphone
pa = pyaudio.PyAudio()
stream = pa.open(format=pa.get_format_from_width(2), channels=1, rate=sample_rate, output=True)
# stream.write(np.int16(y))

N_firls = 1003  # set order of FIR filter
bands = (0, 5500, 5500, 6500, 6600, 23900)  # fill in boundaries of frequency regions
desired = (1, 1, 0, 0, 1 ,1)  # fill in desired frequency response at these regions
fir_bsf = signal.firls(N_firls, bands=bands, desired=desired, fs=sample_rate)
fig4, ax4 = plt.subplots(1, 1, figsize=[5, 4])
ax4.plot(fir_bsf)
"""
y = signal.lfilter(fir_bsf, 1, x.astype(float))
Y = np.abs(np.fft.fft(y))
# stream.write(np.int16(y))
ax1.plot(f, 20 * np.log10(Y))
"""
w, H = signal.freqz(fir_bsf, 1)
ax3.plot(w * sample_rate / (2 * np.pi), np.abs(H))
plt.show()
