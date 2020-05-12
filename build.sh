#!/bin/sh

xa -W -C -v -O ASCII -c src/cartridge.xa -l cartridge.label -o cartridge.bin
xa -W -C -v -O ASCII -c src/cartridge_applesoft.xa -l cartridge_applesoft.label -o cartridge_applesoft.bin
