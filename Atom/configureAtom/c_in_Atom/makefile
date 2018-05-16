# compiler,library,optional flags
CC=gcc
LIB= 
LIBDIR=/usr/local/lib
FCFLAGS=-O2 -lm -lcfitsio -lpthread

# main programs
PROGRAM=hello

# execute program and clean it
default: all
	./${PROGRAM}
	rm -f *.o *~  ${PROGRAM}



# program depends on other programs (something.o)
# dminv_test: 

# "make" builds all
all: $(PROGRAM)


%: %.o
	$(CC) $(FCFLAGS) -o $@ $^ $(LDFLAGS) -L$(LIBDIR)  $(LIB)
	

%.o: %.c
	$(CC) $(FCFLAGS) -c $< -L$(LIBDIR)  $(LIB)

# Utility targets
.PHONY: clean

clean:
	rm -f *.o *~
	
	
