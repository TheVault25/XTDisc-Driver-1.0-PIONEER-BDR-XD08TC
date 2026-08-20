"""Central XTDisc format values for the driver project."""

# Current design value from the XTDisc specification work.
BIT_SIZE_NM = 130

# These values are intentionally undefined until the XTDisc physical format
# is finalized. Do not replace them with guessed values.
INNER_RECORDING_RADIUS_MM = None
OUTER_RECORDING_RADIUS_MM = None
TRACK_PITCH_NM = None
USER_DATA_BITS_PER_BYTE = None
ONE_X_MB_PER_S = None


def describe() -> dict[str, object]:
    return {
        "bit_size_nm": BIT_SIZE_NM,
        "inner_recording_radius_mm": INNER_RECORDING_RADIUS_MM,
        "outer_recording_radius_mm": OUTER_RECORDING_RADIUS_MM,
        "track_pitch_nm": TRACK_PITCH_NM,
        "user_data_bits_per_byte": USER_DATA_BITS_PER_BYTE,
        "one_x_mb_per_s": ONE_X_MB_PER_S,
    }
