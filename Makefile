USER = $(shell whoami)

all: data_management.o divisors.o
	/home/$(USER)/openmpi/bin/mpicc data_management.o divisors.o src/parallel.c -o hybrid -lgomp

data_management.o: src/include/data_management.h
	/home/$(USER)/openmpi/bin/mpicc -c src/data_management.c

divisors.o: src/include/divisors.h
	/home/$(USER)/openmpi/bin/mpicc -c -fopenmp src/divisors.c

clean:
	rm -rf *.o *.output *.out
	rm -rf sequential sh_omp sh_mpi dist_mpi hybrid saida.txt gmon.out

sequential:
	gcc -Wall src/sequential.c src/data_management.c src/divisors.c -lm -o sequential
	./sequential instances/mixed_1.txt

with_prof:
	gcc -Wall src/sequential.c src/data_management.c src/divisors.c -xpg -p -lm -o sequential
	./sequential instances/mixed_1.txt
	gprof sequential > report.output

shared_omp:
	gcc -Wall -fopenmp src/sequential.c src/data_management.c src/divisors.c -o sh_omp
	./sh_omp instances/mixed_1.txt

shared_mpi:
	/home/$(USER)/openmpi/bin/mpicc src/data_management.c src/divisors.c src/parallel.c -o sh_mpi
	/home/$(USER)/openmpi/bin/mpirun -np 4 ./sh_mpi instances/mixed_1.txt

distributed_mpi:
	/home/$(USER)/openmpi/bin/mpicc src/data_management.c src/divisors.c src/parallel.c -o dist_mpi
	/home/$(USER)/openmpi/bin/mpirun -np 4 --hostfile hosts.txt ./dist_mpi instances/mixed_1.txt

hybrid:
	/home/$(USER)/openmpi/bin/mpirun -np 4 --hostfile hosts.txt ./hybrid instances/mixed_1.txt

local_test:
	/home/$(USER)/openmpi/bin/mpirun -np 2 ./hybrid instances/mixed_1.txt
