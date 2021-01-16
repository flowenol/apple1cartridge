import sys
import binascii

"""
This utility transforms binary data to A1 monitor format, starting offset
(in hex) is required.
"""
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print('Usage: python bin2a1monitor.py <hex_offset> <file>')
        exit(1)

    def print_row(offset, row_data):
        print(hex(offset)[2:].upper() + ': ' + " ".join(row_data))

    row_offset = int(sys.argv[1], 16)
    row = list()
    with open(sys.argv[2], 'rb') as file:
        byte = file.read(1)
        while byte:

            row.append(binascii.hexlify(byte).upper())
            if len(row) == 8:
                print_row(row_offset, row)
                row = list()
                row_offset += 0x08

            byte = file.read(1)

        if row:
            print_row(row_offset, row)
