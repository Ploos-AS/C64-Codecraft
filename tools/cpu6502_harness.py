#!/usr/bin/env python3
"""Minimal deterministic 6502/6510 CPU/RAM harness for C64 Codecraft labs."""

from dataclasses import dataclass

@dataclass
class CPU:
    mem: bytearray
    pc: int
    a: int = 0
    x: int = 0
    y: int = 0
    sp: int = 0xff
    p: int = 0x20
    instructions: int = 0

    def fetch(self):
        v = self.mem[self.pc]
        self.pc = (self.pc + 1) & 0xffff
        return v

    def set_zn(self, v):
        self.p = (self.p & ~0x82) | (0x80 if v & 0x80 else 0) | (0x02 if v == 0 else 0)

    def step(self):
        op = self.fetch()
        self.instructions += 1
        if op == 0xa9:  # LDA #imm
            self.a = self.fetch(); self.set_zn(self.a)
        elif op == 0xa5:  # LDA zp
            self.a = self.mem[self.fetch()]; self.set_zn(self.a)
        elif op == 0xa6:  # LDX zp
            self.x = self.mem[self.fetch()]; self.set_zn(self.x)
        elif op == 0xa2:
            self.x = self.fetch(); self.set_zn(self.x)
        elif op == 0x85:  # STA zp
            self.mem[self.fetch()] = self.a
        elif op == 0x8d:  # STA abs
            lo, hi = self.fetch(), self.fetch()
            self.mem[(hi << 8) | lo] = self.a
        elif op == 0x0a:  # ASL A
            carry = 1 if self.a & 0x80 else 0
            self.a = (self.a << 1) & 0xff
            self.p = (self.p & ~0x01) | carry; self.set_zn(self.a)
        elif op == 0xbd:
            lo, hi = self.fetch(), self.fetch()
            self.a = self.mem[(((hi << 8) | lo) + self.x) & 0xffff]; self.set_zn(self.a)
        elif op == 0x9d:
            lo, hi = self.fetch(), self.fetch()
            self.mem[(((hi << 8) | lo) + self.x) & 0xffff] = self.a
        elif op == 0xe8:
            self.x = (self.x + 1) & 0xff; self.set_zn(self.x)
        elif op == 0xe0:
            v = self.fetch(); r = (self.x - v) & 0xff
            self.p = (self.p & ~0x83) | (1 if self.x >= v else 0) | (0x80 if r & 0x80 else 0) | (0x02 if r == 0 else 0)
        elif op == 0xd0:
            off = self.fetch()
            if not self.p & 0x02:
                self.pc = (self.pc + (off - 256 if off & 0x80 else off)) & 0xffff
        elif op == 0x60:
            return False
        else:
            raise RuntimeError(f'unsupported opcode {op:02x} at {(self.pc - 1) & 0xffff:04x}')
        return True

    def run(self, limit=10000):
        while self.instructions < limit:
            if not self.step():
                return
        raise RuntimeError('instruction budget exceeded')

def load_prg(path):
    data = open(path, 'rb').read()
    if len(data) < 3:
        raise ValueError('PRG too short')
    load = data[0] | (data[1] << 8)
    mem = bytearray(65536)
    mem[load:load + len(data) - 2] = data[2:]
    return mem
