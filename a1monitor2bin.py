import codecs
import sys

if __name__ == "__main__":

    byte_data = list()

    if len(sys.argv) != 2:
        print('Usage: python a1monitor2bin.py <file>')
        exit(1)

    with open(sys.argv[1], 'r') as file:
        line = file.readline()
        while line:

            bytes_arr = line.strip().split(':')
            if len(bytes_arr) == 2:
                bytes_str_arr = bytes_arr[1].strip().split()
                for x in bytes_str_arr:
                    byte_data.append(codecs.decode(x, 'hex'))
            line = file.readline()

    for x in byte_data:
        sys.stdout.write(x)

# to visually compare
# paste apple30th.txt <(hexdump -e '"%08.8_Ax\n"' -e '"%08.8_ax " 8/1 " %02x"' -e '"\n"' apple30th.bin)
