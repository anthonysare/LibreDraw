from tkinter import Tk
from tkinter.filedialog import askopenfilename
from convert import *
from streamGcode import *


def printGCODEfile():
    print("LibreDraw V0.1B")
    print("Please select a gcode file to draw.")
    filename = askopenfilename(filetypes=[("GCODE", ".gcode")])
    streamFile(filename)

