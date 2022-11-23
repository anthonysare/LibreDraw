from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Instantiate a compiler, specifying the interface type and the speed at which the tool should move. pass_depth controls
# how far down the tool moves after every pass. Set it to 0 if your machine does not support Z axis movement.
def convertSVG(filename):
    gcode_compiler = Compiler(interfaces.Gcode, movement_speed=3000, cutting_speed=300, pass_depth=0)
    print("Selected: " + filename)
    newName = filename.split(".")
    curves = parse_file(filename) # Parse an svg file into geometric curves

    gcode_compiler.append_curves(curves) 
    gcode_compiler.compile_to_file( newName[0]+ ".gcode", passes=1)
    print("GCODE File Created: " + newName[0] + ".gcode")
