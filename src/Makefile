all: data_management.o
	../../../../openmpi/bin/mpicc data_management.o main.c -o primes

data_management.o: data_management.h
	../../../../openmpi/bin/mpicc -c data_management.c

clean:
	rm -rf *.o
	rm -rf primes

shared_run:
	../../../../openmpi/bin/mpirun -np 4 ./primes ../instances/instance_1.txt

distributed_run:
	../../../../openmpi/bin/mpirun -np 4 --hostfile ../hosts.txt ./primes ../instances/instance_1.txt