# Copyright danielmm8888, all rights reserved
# Revision 0.1
import sys
import os
import struct

# Get a handle to the CAT file and get its size
catFileName = sys.argv[1]
catFile = open(catFileName, 'rb') 
catFileSize = os.path.getsize(catFileName)

# Skip the signature
catFile.seek(0x10)

# Create the folder where we'll be dumping the content into (if necessary)
if not os.path.exists("dump/"):
    os.makedirs("dump/")

# We divide the file size by the size of an entry to get the maximum number of entries
for i in xrange( (catFileSize - 0x10) / 0x20):
    # Read in a single entry from the CAT file
    entry_data = catFile.read(0x20)
    # Skip the SHA1 (we don't need it right now)
    localOffset = 0x14

    # Store the file offset
    offset = struct.unpack('<L', entry_data[localOffset:localOffset + 0x4])[0]
    localOffset += 0x4

    # Store the file size
    size = struct.unpack('<L', entry_data[localOffset:localOffset + 0x4])[0]
    localOffset += 0x4

    # Store the number of the CAS file the file is residing in
    cas_num = struct.unpack('<L', entry_data[localOffset:localOffset + 0x4])[0]

    print "Extracting entry #" + str(i) + " (Offset = " + str(hex(offset)) + " / Size = " + str(hex(size)) + ")"

    # Opens the CAS file, reads the content and then saves it to a new file
    try:
        casFileName = 'cas_' + str(cas_num).zfill(2) + '.cas'
        casFile = open(casFileName, 'rb')
        casFile.seek(offset)
        casData = casFile.read(size)
        casFile.close()
    
        extractedFile = open('dump/' + str(i), 'wb+')
        extractedFile.write(casData)
        extractedFile.close()
    except IOError:
        print "File " + 'cas_' + str(cas_num).zfill(2) + '.cas' + " not found, skipping."

    
catFile.close()

