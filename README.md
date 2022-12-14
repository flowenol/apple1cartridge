![apple1cartridge](/apple1cartridge.jpg)

# apple1cartridge

This repository contains firmware and gerber files for the "Apple-1 RAM/ROM Cartridge" expansion card for the Apple-1 computer.

## Description

This project aims to equip Apple-1 users with a quick way to expand RAM capacity in their systems up to 52 KB and to simultaneously
store Apple-1 programs in ~30KB of on-board ROM, which can be banked in and out via software. The on-board ROM also contains a loader
program which is capable of loading programs spanning across noncontinuous memory locations. You can either use a default loader
program at `4000R`, which displays the list of all available program entries, or the fast loader program at `4300R`, which loads the
specific program entry (selected in ZP variable at `$00`) automatically.

The A1C expansion card allows to completely disable the ROM/loader functionality (which takes up to 2 KB of memory at `$4000-$47FF`)
via physical switch and to provide continuous 44KB wide RAM address space instead (`$1000-$BFFF`). This can be done while the
system is running, thus after a program is loaded, one can change the switch position disabling ROM banking functionality
and use the entire memory address space as RAM.

Loader programs in ROM mode copy bytes sequentially from ROM to RAM locations, as described in the entries table, banking the ROM
in and out. Each entry may consist of several segments that can be loaded to non adjacent memory locations. For obvious reasons
the address space between `$4000-$47FF` cannot be utilised at loading time, because it would require the loader program
to overwrite itself in ROM.

The A1C expansion card in RAM mode works great in conjunction with [Apple-1 Serial Interface](http://github.com/flowenol/apple1serial)
card or the original Apple Cassette Interface, expanding the available address space to load programs.

You can also replace the Apple-1 on-board RAM entirely using an alternative address decoder mapping (check details in the [Mappings](#mappings) section).

## Memory map

With physical switch in ROM position:

| address | function |
| --- | --- |
| `$0000` | program entry to load via the fast loader program |
| `$1000-$3FFF` | RAM region #1 |
| `$4000` | the start address of the on-board loader program |
| `$4300` | the start address of the fast loader program |
| `$47F8-$47FF` | write to these memory locations causes ROM to be banked in or out depending on the least significant bit of the address, A0=0 - ROM banked out, A0=1 - ROM banked in  |
| `$4800-$BFFF` | RAM region #2 when ROM banked out |
| `$4800-$BFFF` | ROM with program contents when ROM banked in |

With physical switch in RAM position:

| address | function |
| --- | --- |
| `$1000-$BFFF` | RAM region |

## Contents

The contents of this repository are as following:

* gerber/ - gerber files needed to manufacture the PCB
* inc/ - contains Apple-1 programs in binary format, the archive is available [here](https://drive.google.com/file/d/1G0ycKSszlr45RE8Rp6eW-0qxz4MS9qDN/view?usp=sharing)
* mapping/ - contains .eqn and .jed files for GAL22V10 based address decoder
* scripts/ - a bunch of useful python scripts which do the conversion between binary and Woz monitor format and vice versa
* src/ - contains the 6502 assembly sources for the on-board ROM loader programs

## Mappings

There are two .jed files for the GAL22V10 based address decoder:

1. **address_decoder.jed** - defines the standard mapping where additional RAM memory is mapped to the regions `$1000-$BFFF` as
described above. This mapping assumes that your Apple-1 board has "X" and "W" RAM chips populated and mapped to regions
`$0000-$0FFF` and `$E000-$EFFF`.
2. **address_decoder1.jed** - defines an alternative mapping allowing tu run Apple-1 Computer entirely from the A1C. The regions
`$0000-$0FFF` and `$E000-$EFFF` are additionally mapped to the A1C RAM1 chip. Be sure to remove the "X" and "W" memory chips
from Apple-1 board for safety, and to disconnect the "X" and "W" lines (if they were mapped to the "0" and "E" segments).

## Requirements

You need the following to successfully build and install the firmware:

* [xa](https://www.floodgap.com/retrotech/xa/) cross assembler
* Software capable of translating the .eqn files into .jed's. I used for this purpose the DOS based EQN2JED from OPALjr PLD Development Package. This is only required if you wish to make some changes to the GAL based address decoder. The default .jed file should be fine for most users.
* EEPROM programmer to write ROM and GAL. I used [TL866](http://autoelectric.cn/EN/TL866_main.html) programmer for this purpose.

## How to build?

To build the firmware just type:

`make`

And to clean the build:

`make clean`

# How to customise?

In order to customise your ROM contents you have to edit the `src/rom_content.a65` source file. You can find the entry table structure
documentation in the source file. Maximum of 99 entries is allowed, anything above that will be ignored.

## Applesoft BASIC support

The onboard ROM loader program can also automatically load your Applesoft BASIC programs thanks to the dedicated branch of the
applesoft-lite project which has been modified to be compatible with the Apple-1 RAM/ROM Cartridge card:

http://github.com/flowenol/applesoft-lite

## How to install hardware?

Just put the board in right orientation (as marked on the PCB) in the Apple-1 expansion slot.
Or you can use the port expander if the expansion slot on the Apple-1 board is already occupied:

https://github.com/flowenol/Apple1ExpanderPcb

## PCB

The KiCad project files with board design and schematics can be found here:

http://github.com/flowenol/Apple1CartridgePcb


## Bill of materials

| name | part | quantity |
| --- | --- | --- |
| C1..C5  | Ceramic 100nF | 5 |
| C6      | Electrolytic 22uF | 1 |
| R1..R3  | 1K 0.5W       | 3 |
| BANK1   | 74LS74 dual D flip-flop DIP14 | 1 |
| DECODER1  | GAL22V10 SPLD (25ns or less) DIP24 | 1 |
| ROM1      | AT28C256 ROM or similar DIP-28 | 1 |
| RAM1,RAM2 | 62256 SRAM 100ns or less DIP-28 | 2 |
| MODE_SWITCH1 | 9x4mm SPDT switch | 1 |
