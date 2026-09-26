from pathlib import Path
import sys

sys.path.insert(0, "tools")
from vice_machine_runner import ViceBinaryMonitorBackend, assert_memory, qualify

prg = Path("labs/07-bitmap-high-colour/04-bitmap-raster-splits/build/bitmap-raster-splits.prg")
payload = prg.read_bytes()
print(f"Lab 07.04 PRG bytes: {payload.hex()}")

# The polling loop exits only after VIC-II raster $D012 matched $60.
# Stop at the first instruction after STA $D020 and verify the visible state.
top = qualify(
    prg,
    backend=ViceBinaryMonitorBackend(
        expected_addresses=(0xD020,),
        stop_address=0x081C,
        entry_address=0x0810,
        port=6506,
        rom_dir=Path("build/open-roms"),
    ),
)
print(f"Lab 07.04 top split: D020={top['observation'].memory[0xD020]:02x}")
assert_memory(top["observation"], {0xD020: 0x06}, masks={0xD020: 0x0F})

# The second polling loop exits only after VIC-II raster $D012 matched $C0.
# Stop immediately before RTS, after the bottom colour has been written.
bottom = qualify(
    prg,
    backend=ViceBinaryMonitorBackend(
        expected_addresses=(0xD020,),
        stop_address=0x0828,
        entry_address=0x0810,
        port=6507,
        rom_dir=Path("build/open-roms"),
    ),
)
print(f"Lab 07.04 bottom split: D020={bottom['observation'].memory[0xD020]:02x}")
assert_memory(bottom["observation"], {0xD020: 0x0E}, masks={0xD020: 0x0F})
