# Copyright PistonMiner, all rights reserved
# Revision 0.1

# Import future division for float division.
from __future__ import division

import sys
import os

# read the data in.
filename_in = sys.argv[1]
input = open(filename_in, "rb")

input.seek(0x128)
lookup_data = input.read(0x101)

input.seek(0, 2)
encrypted_size = input.tell() - 0x22C

input.seek(0x22C)

output_data = [0] * encrypted_size
	
for i in xrange(encrypted_size):
	if(i % 512 == 0)
		encrypted_data = input.read(512)
	print("Decrypting byte " + str(i) + "/" + str(encrypted_size) + (" (%.4f" % (i / encrypted_size)) + "%)")
	output_data[i] = ord(encrypted_data[i % 512]) ^ ord(lookup_data[i % 257]) ^ 0x7b

input.close()

output_data = str(bytearray(output_data))

filename_out = filename_in + ".out"
output = open(filename_out , "wb")
output.write(output_data)
output.close()