# our whf lexer and future parser
from whf_main import *

# very powerful
# https://docs.python.org/3/library/optparse.html#module-optparse
from optparse import OptionParser

# for reading from files
import os

# just for ceil
import math

parser = OptionParser()
parser.add_option("-p", "--praise-whf", help="praise weihang fan with your message <PRAISE_WHF>")

(options, args) = parser.parse_args()

if (options.praise_whf):
	print("\n\n")
	print("        ##############################")
	print("        #                            #")
	print("        #         praising...        #")
	print("        #                            #")
	print("        #   ~~~~~~~~~~~~~~~~~~~~~~   #")
	print("        #                            #")

	a = options.praise_whf
	while (len(a) > 0):
		b = a[:22]
		a = a[22:]
		print("        #   " + " " * ((22 - len(b)) // 2) + b + " " * math.ceil((22 - len(b)) / 2) + "   #")

	print("        #                            #")
	print("        #   ~~~~~~~~~~~~~~~~~~~~~~   #")
	print("        #                            #")
	print("        #   weihang fan is praised.  #")
	print("        #                            #")
	print("        ##############################")
	print("\n\n")

code = ""

if (len(args) < 1):
	print("input file not specified. whf is exiting...")
	exit()

whf_file = args[0]

with open(whf_file, "r") as f:
	code = f.read()

if (code != ""):
	main(code)