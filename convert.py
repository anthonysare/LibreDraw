from svg_to_gcode.svg_parser import parse_file
from svg_to_gcode.compiler import Compiler, interfaces
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Instantiate a compiler, specifying the interface type and the speed at which the tool should move. pass_depth controls
# how far down the tool moves after every pass. Set it to 0 if your machine does not support Z axis movement.
def convertSVG(f):
    gcode_compiler = Compiler(interfaces.Gcode, movement_speed=3000, cutting_speed=2000, pass_depth=0)
    #!!!!!!if !filename, filename = askopenfilename(filetypes=[("SVG", ".svg")])!!!!!
    if f is False:
        f = askopenfilename(filetypes=[("SVG", ".svg")])

    print("Selected: " + f)
    newName = f.split(".")

    #generate_gcode(filename)

    curves = parse_file(f) # Parse an svg file into geometric curves
    gcode_compiler.append_curves(curves) 
    gcode_compiler.compile_to_file( newName[0]+ ".gcode", passes=1)
    
    #Fixing GCODE
    # Read in the file
    with open(newName[0]+ ".gcode", 'r') as file :
        filedata = file.read()

    # Replace the target string
        filedata = filedata.replace('S255', 'S30')

    # Write the file out again
    with open(newName[0]+ ".gcode", 'w') as file:
        file.write(filedata)

    print("GCODE File Created: " + newName[0] + ".gcode")

