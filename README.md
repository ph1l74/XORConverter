# Multibyte XOR converter
### About
Multibyte XOR converter made for calculating checksum with XOR
algorythm. There are different protocols that uses XOR-checksum,
e.g. BANDI Camera protocol.

### Example
I will use typical BANDI-Command to set the camera properties:

`AE 01 00 10 01 20 9E 00 00 00 00 00 00 00 05 0A 0A 01 02 05 01 00 00 00 00 03 00 00 CS AE`

AE -- is the sychro-byte and we needn't to count it.

CS -- checksum-byte. It sum up all bytes from second to pre-CS-byte.

So we need to count checksum of this package:

`01 00 10 01 20 9E 00 00 00 00 00 00 00 05 0A 0A 01 02 05 01 00 00 00 00 03 00 00`

And it will be: `AF`

## window-app
### About
In this directory you can find the windowed version of XOR-Converter.
It was made with PyQt4.
#### Libs
* PyQt4.QtCore
* PyQt4.QtGui
#### Files
* form.ui - user interface PyQt file. You can open it in QtDesigner.
* form.py - user interface in Python format.
* main.py - main file that combined UI and Logic.

## browser-app
### About
In this directory you can find the web version of XOR-Converter.
It was made flask. All you need is to run http.py to start web-server
with XOR-Converter.
#### Libs
* Flask
