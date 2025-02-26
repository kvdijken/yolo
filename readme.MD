# Yolo
## Automated distortion analysis using a signal generator and oscilloscope


### Fixed frequency operation
This shows a fixed frequency CW tone from the signal generator being analyzed:

![Alt text](resources/ui_fixed.png)


<br>
<br>


This shows a FM signal (carrier frequency = 10.7MHz, fixed modulation frequency 1kHz, frequency deviation = 75kHz) which is fed to a FM demodulator and analyzed with yolo:
![Alt text](resources/ui_fixed_FM.png)
<br>
<br>


### Swept frequency operation
This shows a swept frequency (from 1MHz to 10MHz) CW tone being analyzed:

![Alt text](resources/ui_sweep.png)
<br>
<br>



This shows a FM signal (carrier frequency = 10.7MHz, modulation frequency sweep from 500Hz to 5kHz, frequency deviation = 75kHz) which is fed to a FM demodulator and analyzed with yolo:
![Alt text](resources/ui_swept_FM.png)
<br>
<br>




## Requirements
engineering-notation 0.10.0
<br>
fft_calculations     0.2.2
<br>
matplotlib           3.10.0
<br>
matplotlib-inline    0.1.6
<br>
numpy                2.2.2
<br>
pydatacq             0.4.5
<br>
PyQt6                6.8.0
<br>
PyQt6-Qt6            6.8.1
<br>
PyQt6_sip            13.9.1
<br>
PySide6              6.8.1.1
<br>
PySide6_Addons       6.8.1.1
<br>
PySide6_Essentials   6.8.1.1
<br>
PyVISA               1.14.1
<br>
PyVISA-py            0.7.2
<br>
qasync               0.27.1
<br>
quantiphy            2.20
<br>
scipy                1.15.1
<br>
uvloop               0.19.0a1
<br>
<br>

Has been tested with python version 3.11.11.

