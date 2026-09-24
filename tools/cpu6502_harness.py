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

    def write(self, addr, value):
        addr &= 0xffff
        if 0xd000 <= addr <= 0xdfff:
            raise RuntimeError(f'C64 I/O write {addr:04x} is outside CPU/RAM qualification')
        self.mem[addr] = value & 0xff

    def step(self):
        op = self.fetch()
        self.instructions += 1
        if op == 0xa0:  # LDY #imm
            self.y = self.fetch(); self.set_zn(self.y)
        elif op == 0xa9:  # LDA #imm
            self.a = self.fetch(); self.set_zn(self.a)
        elif op == 0xa5:  # LDA zp
            self.a = self.mem[self.fetch()]; self.set_zn(self.a)
        elif op == 0xa6:  # LDX zp
            self.x = self.mem[self.fetch()]; self.set_zn(self.x)
        elif op == 0xa2:
            self.x = self.fetch(); self.set_zn(self.x)
        elif op == 0x85:  # STA zp
            self.write(self.fetch(), self.a)
        elif op == 0x8d:  # STA abs
            lo, hi = self.fetch(), self.fetch()
            self.write((hi << 8) | lo, self.a)
        elif op == 0x4a:  # LSR A
            carry = self.a & 1; self.a >>= 1
            self.p = (self.p & ~0x01) | carry; self.set_zn(self.a)
        elif op == 0x0a:  # ASL A
            carry = 1 if self.a & 0x80 else 0
            self.a = (self.a << 1) & 0xff
            self.p = (self.p & ~0x01) | carry; self.set_zn(self.a)
        elif op == 0x18:  # CLC
            self.p &= ~0x01
        elif op == 0x65:  # ADC zp
            v = self.mem[self.fetch()]; c = self.p & 1; total = self.a + v + c; result = total & 0xff
            overflow = (~(self.a ^ v) & (self.a ^ result) & 0x80) != 0
            self.p = (self.p & ~0x41) | (1 if total > 0xff else 0) | (0x40 if overflow else 0)
            self.a = result; self.set_zn(self.a)
        elif op == 0x69:  # ADC #imm (binary mode)
            v = self.fetch(); total = self.a + v + (self.p & 1)
            result = total & 0xff
            overflow = (~(self.a ^ v) & (self.a ^ result) & 0x80) != 0
            self.p = (self.p & ~0x41) | (1 if total > 0xff else 0) | (0x40 if overflow else 0)
            self.a = result; self.set_zn(self.a)
        elif op == 0x49:  # EOR #imm
            self.a ^= self.fetch(); self.set_zn(self.a)
        elif op == 0xb1:  # LDA (zp),Y
            zp = self.fetch(); lo = self.mem[zp]; hi = self.mem[(zp + 1) & 0xff]
            self.a = self.mem[(((hi << 8) | lo) + self.y) & 0xffff]; self.set_zn(self.a)
        elif op == 0xad:  # LDA abs
            lo, hi = self.fetch(), self.fetch()
            self.a = self.mem[(hi << 8) | lo]; self.set_zn(self.a)
        elif op == 0xb9:  # LDA abs,Y
            lo, hi = self.fetch(), self.fetch(); self.a = self.mem[(((hi << 8) | lo) + self.y) & 0xffff]; self.set_zn(self.a)
        elif op == 0xbd:
            lo, hi = self.fetch(), self.fetch()
            self.a = self.mem[(((hi << 8) | lo) + self.x) & 0xffff]; self.set_zn(self.a)
        elif op == 0x84:  # STY zp
            self.mem[self.fetch()] = self.y
        elif op == 0x91:  # STA (zp),Y
            zp = self.fetch(); base = self.mem[zp] | (self.mem[(zp + 1) & 0xff] << 8)
            self.write((base + self.y) & 0xffff, self.a)
        elif op == 0x99:  # STA abs,Y
            lo, hi = self.fetch(), self.fetch()
            self.write((((hi << 8) | lo) + self.y) & 0xffff, self.a)
        elif op == 0x8c:  # STY abs
            lo, hi = self.fetch(), self.fetch(); self.write((hi << 8) | lo, self.y)
        elif op == 0xc0:  # CPY #imm
            v = self.fetch(); r = (self.y - v) & 0xff
            self.p = (self.p & ~0x83) | (1 if self.y >= v else 0) | (0x80 if r & 0x80 else 0) | (0x02 if r == 0 else 0)
        elif op == 0xc6:  # DEC zp
            a = self.fetch(); self.mem[a] = (self.mem[a] - 1) & 0xff; self.set_zn(self.mem[a])
        elif op == 0xe6:  # INC zp
            a = self.fetch(); self.mem[a] = (self.mem[a] + 1) & 0xff; self.set_zn(self.mem[a])
        elif op == 0xc8:  # INY
            self.y = (self.y + 1) & 0xff; self.set_zn(self.y)
        elif op == 0x88:  # DEY
            self.y = (self.y - 1) & 0xff; self.set_zn(self.y)
        elif op == 0x10:  # BPL
            off = self.fetch()
            if not self.p & 0x80:
                self.pc = (self.pc + (off - 256 if off & 0x80 else off)) & 0xffff
        elif op == 0x20:  # JSR
            lo, hi = self.fetch(), self.fetch(); ret = (self.pc - 1) & 0xffff
            self.mem[0x100 + self.sp] = (ret >> 8) & 0xff; self.sp = (self.sp - 1) & 0xff
            self.mem[0x100 + self.sp] = ret & 0xff; self.sp = (self.sp - 1) & 0xff
            self.pc = (hi << 8) | lo
        elif op == 0x9d:
            lo, hi = self.fetch(), self.fetch()
            self.write((((hi << 8) | lo) + self.x) & 0xffff, self.a)
        elif op == 0xca:  # DEX
            self.x = (self.x - 1) & 0xff; self.set_zn(self.x)
        elif op == 0xe8:  # INX
            self.x = (self.x + 1) & 0xff; self.set_zn(self.x)
        elif op == 0x8a:  # TXA
            self.a = self.x; self.set_zn(self.a)
        elif op == 0xaa:  # TAX
            self.x = self.a; self.set_zn(self.x)
        elif op == 0xa8:  # TAY
            self.y = self.a; self.set_zn(self.y)
        elif op == 0x29:  # AND #imm
            self.a &= self.fetch(); self.set_zn(self.a)
        elif op == 0x86:  # STX zp
            self.write(self.fetch(), self.x)
        elif op == 0xc9:  # CMP #imm
            v = self.fetch(); r = (self.a - v) & 0xff
            self.p = (self.p & ~0x83) | (1 if self.a >= v else 0) | (0x80 if r & 0x80 else 0) | (0x02 if r == 0 else 0)
        elif op == 0xf0:  # BEQ
            off = self.fetch()
            if self.p & 0x02:
                self.pc = (self.pc + (off - 256 if off & 0x80 else off)) & 0xffff
        elif op == 0xe0:
            v = self.fetch(); r = (self.x - v) & 0xff
            self.p = (self.p & ~0x83) | (1 if self.x >= v else 0) | (0x80 if r & 0x80 else 0) | (0x02 if r == 0 else 0)
        elif op == 0x4c:  # JMP abs
            lo, hi = self.fetch(), self.fetch(); self.pc = (hi << 8) | lo
        elif op == 0xb0:  # BCS
            off = self.fetch()
            if self.p & 0x01:
                self.pc = (self.pc + (off - 256 if off & 0x80 else off)) & 0xffff
        elif op == 0xd0:
            off = self.fetch()
            if not self.p & 0x02:
                self.pc = (self.pc + (off - 256 if off & 0x80 else off)) & 0xffff
        elif op == 0x60:  # RTS; empty stack means harness stop
            if self.sp == 0xff:
                return False
            self.sp = (self.sp + 1) & 0xff; lo = self.mem[0x100 + self.sp]
            self.sp = (self.sp + 1) & 0xff; hi = self.mem[0x100 + self.sp]
            self.pc = (((hi << 8) | lo) + 1) & 0xffff
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
