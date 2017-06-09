 ## fd -1 pts 
 
 
 #### fd.c
 ```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char buf[32];
int main(int argc, char* argv[], char* envp[]){
	if(argc<2){
		printf("pass argv[1] a number\n");
		return 0;
	}
	int fd = atoi( argv[1] ) - 0x1234;
	int len = 0;
	len = read(fd, buf, 32);
	if(!strcmp("LETMEWIN\n", buf)){
		printf("good job :)\n");
		system("/bin/cat flag");
		exit(0);
	}
	printf("learn about Linux file IO\n");
	return 0;

} 

```

#### you just have r 0x1234 and input LETMEWIN to get the flag !!!! :)
 
 ### 2) COllosion 
               4bytes - 1 int 
	       so spit the valu accordingly
### 3) BOF
             overflow and change the variable value
### 5) Random
             the program uses rand() without a seed , so it genrates same no always
### 6) mistake
          if(fd=read("passwd",'r')<0) this always retuerns fd=0 coz "<" has higher priority than "="
	  u can give password and validate the chall 
### 7) shellshock
          ths was bug 10 years ago , the bash usually  reads all varible marked as export as well as exported funcion into the stack , but the bug is it does not stops after pasrsing the exported funcion it as well as executes command after funcion delcreation 
	  
	  export evil='() {  :; }; /bin/sh'
	  if bash is called inside su-binary u get a previlage esclated shell 
[Refer here](https://unix.stackexchange.com/questions/157329/what-does-env-x-command-bash-do-and-why-is-it-insecure)


### 8) cmd1 
  In this que the program  overwrites path variavle to /**** which doesent exist and check for argv for (sh,tmp,flag) and excutes our cmd given in argv . In this we can  again restore PATH var by using export as this is bash - builtin command and then execute /bin/sh

### 9) cmd2 
  In this one the  program  filters  more words  (export,flag,=,PATH)
  so now u can use eval commnad which is also bash-builtin to execute  stuff 
  ./cmd2 "read f ; echo \$f; eval \$f ; cat *"  to get the flag
