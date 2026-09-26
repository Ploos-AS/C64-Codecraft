from pathlib import Path
import sys

sys.path.insert(0, "tools")
from vice_machine_runner import ViceBinaryMonitorBackend, assert_memory, qualify

prg = Path("labs/07-bitmap-high-colour/02-multicolor-bitmap-data/build/multicolor-bitmap-data.prg")
payload = prg.read_bytes()
print(f"Lab 07.02 PRG bytes: {payload.hex()}")

addresses = (0x2000, 0x2001, 0x2006, 0x2007, 0x0400, 0xD800, 0xD021)
result = qualify(
    prg,
    backend=ViceBinaryMonitorBackend(
        expected_addresses=addresses,
        stop_address=0x082B,
        port=6505,
        rom_dir=Path("build/open-roms"),
    ),
)
observation = result["observation"]
observed = observation.memory
print(
    "Lab 07.02 VICE state: "
    f"2000={observed[0x2000]:02x} 2001={observed[0x2001]:02x} "
    f"2006={observed[0x2006]:02x} 2007={observed[0x2007]:02x} "
    f"0400={observed[0x0400]:02x} D800={observed[0xD800]:02x} "
    f"D021={observed[0xD021]:02x}"
)

assert_memory(
    observation,
    {
        0x2000: 0x1B,
        0x2001: 0x6C,
        0x2006: 0x6C,
        0x2007: 0x1B,
        0x0400: 0x26,
        0xD800: 0x0E,
        0xD021: 0x00,
    },
    masks={0xD800: 0x0F, 0xD021: 0x0F},
)
