"""XTDisc Driver 1.0 development interface.

Target hardware: PIONEER BDR-XD08TC USB Device.

This is a safe user mode development utility. It identifies the target
optical drive through Windows and reports its basic identity. It does not
replace the Windows kernel optical storage driver and does not issue
undocumented Pioneer commands.
"""

import platform
import subprocess
import sys

TARGET = "PIONEER BDR-XD08TC"


def find_target_drive() -> list[str]:
    """Return Windows optical drive descriptions containing the target name."""
    if platform.system() != "Windows":
        return []

    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "Get-CimInstance Win32_CDROMDrive | Select-Object -ExpandProperty Name",
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return []

    names = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return [name for name in names if TARGET.lower() in name.lower()]


def main() -> int:
    print("XTDisc Driver 1.0")
    print(f"Target: {TARGET}")
    print()

    if platform.system() != "Windows":
        print("This development utility is intended for Windows.")
        return 1

    drives = find_target_drive()
    if not drives:
        print("PIONEER BDR-XD08TC was not detected.")
        print("Connect the drive and try again.")
        return 2

    print("PIONEER BDR-XD08TC detected:")
    for name in drives:
        print(f"  {name}")

    print()
    print("XTDisc format support is not enabled yet.")
    print("The XTDisc physical format is still in development.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
