all: data_management.o divisors.o
	../../../../openmpi/bin/mpicc data_management.o divisors.o parallel.c -lm -o primes

data_management.o: data_management.h
	../../../../openmpi/bin/mpicc -c data_management.c

divisors.o: divisors.h
	../../../../openmpi/bin/mpicc -c divisors.c

clean:
	rm -rf *.o
	rm -rf primes
	rm saida.txt

shared_run:
	../../../../openmpi/bin/mpirun -np 4 ./primes ../instances/instance_1.txt

distributed_run:
	../../../../openmpi/bin/mpirun -np 4 --hostfile ../hosts.txt ./primes ../instances/instance_1.txt