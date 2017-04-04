# Edit source walksat.c to set o/s dependent flags


CC = gcc -O3

all:	walksat

walksat: walksat.c
	$(CC)  walksat.c -lm -o walksat

install: walksat 
	cp walksat $(HOME)/bin/
	
clean:
	rm -f walksat

