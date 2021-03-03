import codecs
import binascii
import sys

"""
This utility transforms CFFA formatted Integer BASIC programs to binary, outputting
to file name with LOMEM & HIMEM appended
"""
if __name__ == "__main__":

    byte_data = list()

    if len(sys.argv) != 2:
        print('Usage: python bas2bin.py <file>')
        exit(1)

    with open(sys.argv[1], 'r') as file:
        line_counter = 0
        line = file.readline()
        while line:

            if line_counter not in [0, 1]:
                bytes_arr = line.strip().split('  ')
                if len(bytes_arr) >= 3:
                    try:
                        bytes_str_arr = bytes_arr[1].strip().split() + bytes_arr[2].strip().split()
                        for x in bytes_str_arr:
                            byte_data.append(codecs.decode(x, 'hex'))
                    except binascii.Error:
                        break

            line_counter += 1
            line = file.readline()

    # delete CFFA bytes
    del byte_data[256:512]
    del byte_data[0:74]

    def output_filename(input_file_name, mem_arr):
        output_name = input_file_name
        if input_file_name.endswith('.txt'):
            output_name = output_name[0:-4]

        output_name = output_name + '-' + mem_arr[1].hex() + mem_arr[0].hex() + '-' + mem_arr[3].hex() + mem_arr[2].hex() + '.bin'
        return output_name.lower()

    with open(output_filename(sys.argv[1], byte_data[0:4]), 'wb') as output:
        for x in byte_data:
            output.write(x)
