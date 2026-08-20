"""Placeholder for the future XTDisc sector reader.

The reader will only be implemented after the XTDisc sector format,
error correction and command interface are finalized.
"""


def read_sector(sector: int) -> bytes:
    """Read one XTDisc sector.

    Not implemented in version 1.0 because the XTDisc sector format and
    hardware command path have not yet been finalized.
    """
    if sector < 0:
        raise ValueError("sector must be zero or greater")
    raise NotImplementedError("XTDisc sector reading is not implemented yet")
