from pathlib import Path
import sys

sys.path.insert(0, "tools")
from vice_machine_runner import ViceBinaryMonitorBackend, assert_memory, qualify

prg = Path("labs/07-bitmap-high-colour/04-bitmap-raster-splits/build/bitmap-raster-splits.prg")
payload = prg.read_bytes()
print(f"Lab 07.04 PRG bytes: {payload.hex()}")

top = qualify(
    prg,
    backend=ViceBinaryMonitorBackend(
        expected_addresses=(0xD012, 0xD020),
        stop_address=0x081C,
        port=6506,
        rom_dir=Path("build/open-roms"),
    ),
)
print(
    "Lab 07.04 top split: "
    f"D012={top['observation'].memory[0xD012]:02x} "
    f"D020={top['observation'].memory[0xD020]:02x}"
)
assert_memory(
    top["observation"],
    {0xD012: 0x60, 0xD020: 0x06},
    masks={0xD020: 0x0F},
)

bottom = qualify(
    prg,
    backend=ViceBinaryMonitorBackend(
        expected_addresses=(0xD012, 0xD020),
        stop_address=0x0828,
        port=6507,
        rom_dir=Path("build/open-roms"),
    ),
)
print(
    "Lab 07.04 bottom split: "
    f"D012={bottom['observation'].memory[0xD012]:02x} "
    f"D020={bottom['observation'].memory[0xD020]:02x}"
)
assert_memory(
    bottom["observation"],
    {0xD012: 0xC0, 0xD020: 0x0E},
    masks={0xD020: 0x0F},
)
