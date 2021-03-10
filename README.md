![apple1cartridge](/apple1cartridge.jpg)

# apple1cartridge

This repository contains firmware files for the "Apple-1 RAM/ROM Cartridge" expansion card for the Apple-1 computer.

## Description

This project aims to equip Apple-1 users with a quick way to expand RAM capacity in their systems up to 52 KB and to simultaneously
store Apple-1 programs in ~30KB of on-board ROM, which can be banked in and out via software. The on-board ROM also contains a loader
program which is capable of loading programs spanning across noncontinuous memory locations. You can either use a default loader program `4000R`, which displays the list of all available program entries, or the fast loader program `4300R`, which loads the
specific program entry automatically.

The A1C expansion card allows to completely disable the ROM/loader functionality (via physical switch) which takes up to 2 KB of
memory (`$4000-$47FF`) and to provide continuous 44KB wide RAM address space instead (`$1000-$BFFF`).

## Memory map

With physical switch in ROM mode:

| address | function |
| --- | --- |
| `$0000` | program entry to load via the fast loader program |
| `$1000-$3FFF` | RAM region #1 |
| `$4000` | the start address of the on-board loader program |
| `$4300` | the start address of the fast loader program |
| `$47F8-$47FF` | write to these memory locations causes ROM to be banked in or out depending on the least significant bit of the address, A0=0 - ROM banked out, A0=1 - ROM banked in  |
| `$4800-$BFFF` | RAM region #2 when ROM banked out |
| `$4800-$BFFF` | ROM with program contents when ROM banked in |

With physical switch in RAM mode:

| address | function |
| --- | --- |
| `$1000-$BFFF` | RAM region |

## Contents

The contents of this repository are as following:

* inc/ - contains Apple-1 programs in binary format, the package is downloadable [here](https://drive.google.com/file/d/1G0ycKSszlr45RE8Rp6eW-0qxz4MS9qDN/view?usp=sharing)
* mapping/ - contains EQN and JED files for GAL22V10 based address decoder
* scripts/ - a bunch of useful python scripts which allow conversion from binary to Woz monitor format and vice versa
* src/ - contains the 6502 assembly sources for the on-board ROM loader programs

## Requirements

You need the following to successfully build and install the firmware:

* [xa](https://www.floodgap.com/retrotech/xa/) cross assembler
* Some software capable of translating the EQN files into JED's. I used for this purpose the DOS based EQN2JED from OPALjr PLD Development Package. This is only required if you wish to make some changes to the GAL based address decoder. The default JED file should be fine for most users.
* EEPROM programmer. I used [TL866](http://autoelectric.cn/EN/TL866_main.html) programmer for this purpose.

## How to build?

To build the firmware just type:

`make`

And to clean the build:

`make clean`

# How to customise?

In order to customise your ROM contents you have to edit the `src/rom_content.a65` source file. You can find the entry table structure
documentation in the source file. Maximum of 99 entries is allowed, anything above that will be ignored.

## PCB

The KiCad project files with board design and schematics can be found here:

http://github.com/flowenol/Apple1CartridgePcb

## Applesoft BASIC support

The onboard ROM loader program can also automatically load your Applesoft BASIC programs thanks to the branch of the
applesoft-lite project which has been modified to make use of the RAM/ROM expansion card:

http://github.com/flowenol/applesoft-lite

## How to install hardware?

Just put the board in right orientation (as marked on the PCB) in the Apple-1 expansion slot.
Or you can use the port expander if the expansion slot on the Apple-1 board is already occupied:

https://github.com/flowenol/Apple1ExpanderPcb
