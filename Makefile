cartridge.bin:
	xa -W -C -v -O ASCII -c src/cartridge.a65 -l cartridge.label -o cartridge.bin

clean:
	rm cartridge.bin cartridge.label
