from pathlib import Path
import sys

sys.path.insert(0, "tools")
from vice_machine_runner import ViceBinaryMonitorBackend, assert_memory, qualify

prg = Path("labs/00-intro/08-fill-row/build/fill-row.prg")
payload = prg.read_bytes()
print(f"Lab 00.08 PRG bytes: {payload.hex()}")

result = qualify(
    prg,
    backend=ViceBinaryMonitorBackend(
        expected_addresses=(0x0400, 0x0427, 0xD800, 0xD827),
        stop_address=0x0821,
        port=6503,
        rom_dir=Path("build/open-roms"),
    ),
)
observed = result["observation"].memory
print(
    f"Lab 00.08 VICE state: "
    f"0400={observed[0x0400]:02x} 0427={observed[0x0427]:02x} "
    f"D800={observed[0xD800]:02x} D827={observed[0xD827]:02x}"
)

assert_memory(
    result["observation"],
    {0x0400: 0x01, 0x0427: 0x01, 0xD800: 0x0E, 0xD827: 0x0E},
    masks={0xD800: 0x0F, 0xD827: 0x0F},
)
