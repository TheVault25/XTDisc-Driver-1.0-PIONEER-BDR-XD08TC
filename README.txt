XTDisc Driver 1.0
PIONEER BDR-XD08TC

Purpose
This project is the starting point for XTDisc support on the PIONEER BDR-XD08TC USB optical drive.

Important
Version 1.0 is a development driver project. It does not yet make a Windows installation package or make the Pioneer drive read an unfinished XTDisc format. The XTDisc physical format, recording structure, sector layout, error correction and final spindle speed specification are still being defined.

Supported hardware
PIONEER BDR-XD08TC USB Device

What is planned
1. Detect the connected Pioneer drive.
2. Confirm that the connected device is the expected drive.
3. Detect inserted media.
4. Identify XTDisc media when the XTDisc format is finalized.
5. Read XTDisc sectors.
6. Use the XTDisc RPM control defined by the final format.
7. Support XTDisc data transfer to Windows.
8. Provide an installer for the finished Windows driver.

Current XTDisc design information
Bit size: 130 nm

The 130 nm value is currently being used for physical data-rate calculations. It is not yet enough to define a complete disc format. The final recording method, track pitch, recording radius, sector structure, error correction and user-data efficiency still need to be specified.

Drive specific information
The BDR-XD08TC is the only drive targeted by this version because it is the drive available for development and testing.

A real Windows kernel driver must use the Windows storage and optical-drive interfaces supported by the operating system. The project must not invent undocumented Pioneer commands. Any Pioneer specific command needed for XTDisc support must be verified against the actual drive before being used.

Installation
There is no finished Windows EXE installer in version 1.0 yet. Do not install an unsigned or unverified kernel driver as a replacement for the normal Windows optical-drive driver.

Development
The first development stage is to communicate with the BDR-XD08TC through its normal USB optical-drive interface and establish reliable media detection and read testing. XTDisc-specific commands will be added only after the physical format and command interface are defined.

Planned files
xtdisc_driver.py       Development interface and drive detection
xtdisc_reader.py       Future XTDisc sector reader
xtdisc_format.py       XTDisc format definitions
installer.ps1          Future Windows installer script

Testing
Test with a normal optical disc first. XTDisc support must not be claimed until an actual XTDisc test disc exists and can be read reliably.

Project status
Development version 1.0
Target drive: PIONEER BDR-XD08TC
XTDisc format status: In development
