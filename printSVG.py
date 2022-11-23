from tkinter import Tk
from tkinter.filedialog import askopenfilename
from convert import *
from streamGcode import *


def main():
    print("LibreDraw V0.1B")
    print("Please select an svg file to draw.")
    filename = askopenfilename(filetypes=[("SVG", ".svg")])
    convertSVG(filename)
    gcodefName = filename.split(".")
    streamFile(gcodefName[0] + ".gcode")


if __name__ == "__main__":
    main()