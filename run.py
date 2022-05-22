import gdlevelconverter.command_line
import traceback
from tkinter import filedialog
import sys

try:
    print("Geometry Dash 2.0+ to 1.9 Level Converter")
    print("by ~zmx")
    input_file = filedialog.askopenfilename(title='Open the level file', filetypes=(('GMD File', '*.gmd'),))
    if not input_file: exit()
    output_file = filedialog.asksaveasfilename(title='Output .gmd file', filetypes=(('GMD File', '*.gmd'),), defaultextension='gmd')
    if not output_file: exit()

    args = [input_file, '-o', output_file]
    
    gdlevelconverter.command_line._main(args)

    input("Finished, press enter to close...")

except KeyboardInterrupt:
    input("Cancelling, press enter to close...")
except Exception as ex:
    traceback.print_exception(type(ex), ex, ex.__traceback__)
    input("")