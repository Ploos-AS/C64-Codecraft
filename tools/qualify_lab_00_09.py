from pathlib import Path
import sys

sys.path.insert(0, "tools")
from vice_machine_runner import ViceBinaryMonitorBackend, assert_memory, qualify

prg = Path("labs/00-intro/09-table-driven-screen/build/table-driven-screen.prg")
payload = prg.read_bytes()
print(f"Lab 00.09 PRG bytes: {payload.hex()}")

addresses = (0x0400, 0x0401, 0x0404, 0x0427, 0xD800, 0xD801, 0xD804, 0xD827)
result = qualify(
    prg,
    backend=ViceBinaryMonitorBackend(
        expected_addresses=addresses,
        stop_address=0x082C,
        port=6504,
        rom_dir=Path("build/open-roms"),
    ),
)
observation = result["observation"]
observed = observation.memory
print(
    "Lab 00.09 VICE state: "
    f"0400={observed[0x0400]:02x} 0401={observed[0x0401]:02x} "
    f"0404={observed[0x0404]:02x} 0427={observed[0x0427]:02x} "
    f"D800={observed[0xD800]:02x} D801={observed[0xD801]:02x} "
    f"D804={observed[0xD804]:02x} D827={observed[0xD827]:02x}"
)

assert_memory(
    observation,
    {
        0x0400: 0x01,
        0x0401: 0x02,
        0x0404: 0x04,
        0x0427: 0x01,
        0xD800: 0x01,
        0xD801: 0x07,
        0xD804: 0x08,
        0xD827: 0x07,
    },
    masks={0xD800: 0x0F, 0xD801: 0x0F, 0xD804: 0x0F, 0xD827: 0x0F},
)
