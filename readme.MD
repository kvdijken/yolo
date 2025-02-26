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

## Usage

### On linux:

From the directory in which `yolo.py` was installed:
```
python3 -m yolo.py
```

### On macOS:

### On Windows:

### On first use

On first use the ip-addresses of the oscilloscope and the signal generator needs to be entered. This can be done in the Settings dialog:

![Alt text](resources/settings.png)

The data in this dialog will be saved in `/home/koen/.config/FM Homelab/yolo.conf`


## Tested with

- Fedora Linux 39
- Gnome 45.10
- Linux 6.11.9-100.fc39.x86_64
- oscilloscope: Siglent SDS1202X-E
- signale generator: Siglent SDG1032X
- python 3.11.11


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

## pyvisa vs. pydatacq


## More to do

- make engine a class
- set sample memory as low as needed
- make settings dialog a modal dialog
- clean up code
- document code
 


