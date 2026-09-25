from pathlib import Path
import sys

sys.path.insert(0, "tools")
from vice_machine_runner import AssertionMismatch, ViceBinaryMonitorBackend, assert_memory, qualify

prg = Path("labs/00-intro/08-fill-row/build/fill-row.prg")
payload = prg.read_bytes()
print(f"Lab 00.03 PRG bytes: {payload.hex()}")
print("Lab 00.03 expected code @0810: a200a9019d0004a90e9d800e8e028d0f")

result = qualify(
    prg,
    expected_memory={},
    backend=ViceBinaryMonitorBackend(rom_dir=Path("build/open-roms")),
)
observed = result["observation"].memory
print(f"Lab 00.08 VICE state: D020={observed[0xD020]:02x} D021={observed[0xD021]:02x}")

assert_memory(
    result["observation"],
    {0xD020: 0x05, 0xD021: 0x00},
    masks={0xD020: 0x0F, 0xD021: 0x0F},
)
try:
    assert_memory(result["observation"], {0xD020: 0x06}, masks={0xD020: 0x0F})
except AssertionMismatch:
    print("Lab 00.03 negative hardware assertion: PASS")
else:
    raise SystemExit("intentional wrong VIC-II expectation unexpectedly passed")
