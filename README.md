# Streamlined

Setup:

Install Python on your device, and create a virtual environment for this folder if you wish to do so (if you don't know what a virtual environment is, ignore and carry on).

Then execute the following commands on your terminal:

  pip3 install kivy

  pip3 install pyserial

This is required for the graphical interface, and the Arduino code that drives the motors, respectively, to function correctly.

To run the text interface, type "python3 text_interface.py" on your terminal after locating the folder with all the necessary code files on your device.

To run the graphical interface, similarly type "python3 graphical_interface.py" on your terminal.

Install Arduino IDE to work with the physical circuit, and identify the port that the Arduino is connected to. Change the port values in database.py as required (the default value is COM7).

Install SimulIDE to run the simulation, loading the correct .simu and .ino files onto the interface first.

Good luck, hopefully it works on your device too!
