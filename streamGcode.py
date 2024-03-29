import serial
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

maxX = 0
maxY = 0


def streamFile(filename):
    # Open grbl serial port ==> CHANGE THIS BELOW TO MATCH YOUR USB LOCATION
    s = serial.Serial('COM3',115200) # GRBL operates at 115200 baud. Leave that part alone.
    # Open g-code file
    f = open(filename,'r')
    print("Streaming " + filename)
    # Wake up grbl
    s.write("\r\n\r\n".encode())
    time.sleep(2)   # Wait for grbl to initialize
    s.flushInput()  # Flush startup text in serial input

    # Stream g-code to grbl
    for line in f:
        l = line.strip() # Strip all EOL characters for consistency
        print ('Sending: ' + l),
        s.write((l + '\n').encode()) # Send g-code block to grbl
        grbl_out = s.readline() # Wait for grbl response with carriage return
        print (' : ' + grbl_out.strip().decode())

    # Wait here until grbl is finished to close serial port and file.
    input("  Press <Enter> to exit and disable grbl.")

    # Close file and serial port
    f.close()
    s.close()


def home():
    s = serial.Serial('COM4',115200)
    s.write("\r\n\r\n".encode())
    time.sleep(2)   # Wait for grbl to initialize
    s.flushInput()  # Flush startup text in serial input
   
    s.write(('#H' + '\n').encode()) # Send g-code block to grbl
    grbl_out = s.readline() # Wait for grbl response with carriage return
    print (' : ' + grbl_out.strip().decode())


