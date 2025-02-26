# Yolo
## Automated distortion Analysis using a signal generator and oscilloscope

### Fixed frequency operation
![Alt text](resources/ui_fixed.png)

This shows a fixed frequency CW tone from the signal generator being analyzed.


![Alt text](resources/ui_fixed_FM.png)

This shows a FM signal (carrier frequency = 10.7MHz, fixed modulation frequency 1kHz, frequency deviation = 75kHz) which is fed to a FM demodulator and analyzed with yolo.
<br>
<br>


### Swept frequency operation
![Alt text](resources/ui_sweep.png)

This shows a swept frequency (from 1MHz to 10MHz) CW tone being analyzed.
<br>
<br>



![Alt text](resources/ui_swept_FM.png)

This shows a FM signal (carrier frequency = 10.7MHz, swept modulation frequency 500Hz to 5kHz, frequency deviation = 75kHz) which is fed to a FM demodulator and analyzed with yolo.


## Requirements
engineering-notation 0.10.0
fft_calculations     0.2.2
matplotlib           3.10.0
matplotlib-inline    0.1.6
numpy                2.2.2
pydatacq             0.4.5
PyQt6                6.8.0
PyQt6-Qt6            6.8.1
PyQt6_sip            13.9.1
PySide6              6.8.1.1
PySide6_Addons       6.8.1.1
PySide6_Essentials   6.8.1.1
PyVISA               1.14.1
PyVISA-py            0.7.2
qasync               0.27.1
quantiphy            2.20
scipy                1.15.1
uvloop               0.19.0a1

Has been tested with python version 3.11.11.

