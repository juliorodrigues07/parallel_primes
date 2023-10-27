USER = $(shell whoami)

all: data_management.o divisors.o
	/home/$(USER)/openmpi/bin/mpicc data_management.o divisors.o src/parallel.c -lm -o primes

data_management.o: src/include/data_management.h
	/home/$(USER)/openmpi/bin/mpicc -c src/data_management.c

divisors.o: src/include/divisors.h
	/home/$(USER)/openmpi/bin/mpicc -c src/divisors.c

clean:
	rm -rf *.o *.output *.out
	rm -rf primes sequential saida.txt gmon.out

sequential:
	gcc -Wall src/sequential.c src/data_management.c src/divisors.c -lm -o sequential
	./sequential instances/prime_1.txt

with_prof:
	gcc -Wall src/sequential.c src/data_management.c src/divisors.c -xpg -p -lm -o sequential
	./sequential instances/prime_1.txt
	gprof sequential > prime.output

shared_run:
	/home/$(USER)/openmpi/bin/mpirun -np 4 ./primes instances/prime_1.txt

distributed_run:
	/home/$(USER)/openmpi/bin/mpirun -np 4 --hostfile hosts.txt ./primes instances/prime_1.txt
