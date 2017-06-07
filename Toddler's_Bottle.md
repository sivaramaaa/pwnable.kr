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
