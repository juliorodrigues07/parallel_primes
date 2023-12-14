[![C99](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf)
# Identifying Primes with Parallel Computing
Implementation of a master-slave hybrid parallel program (shared and distributed memory) to identify prime numbers in an array, utilizing Open MPI and OpenMP libraries (PAs 1 and 3 from Parallel Computing course - DCOMP - UFSJ).

# Requirements

- [GCC](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/) compiler:

      sudo apt install gcc
  
- [OpenMP](https://www.openmp.org/) library:

      sudo apt install libomp-dev

- [Open MPI](https://www.open-mpi.org/doc/) library;
  
- [gprof](https://ftp.gnu.org/old-gnu/Manuals/gprof-2.9.1/html_mono/gprof.html) tool;

- To install all dependencies:

      ./install_dependencies.sh

# Optional Requirements

- [Python3](https://python.org) and [pip](https://pip.pypa.io/en/stable/installation/) package manager:

      sudo apt install python3 python3-pip build-essential python3-dev

- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html) library:
 
      pip install pycryptodomex

- [Matplotlib](https://matplotlib.org/) library:
 
      pip install matplotlib
       
- [seaborn](https://seaborn.pydata.org/) library:
 
      pip install seaborn

# Compilation

Execute the following command to compile the source code:

    make

# Execution

You can alter the parameters, such as the instance file and number of processes in the _Makefile_. For distributed running, first you may need to gain remote acess to the machines in your network by generating a private key with the following commands:

    ssh-keygen
    ssh-copy-id <IP_address>
    ssh <IP_address>

Also, you may need to change parameters in the hostfile (_hosts.txt_), such as IP addresses and number of slots (CPU cores).

## Sequential

To execute the sequential version with or without profiling, run the following respective commands:

- Without profiling:

      make sequential

- With profiling (**gprof**):

      make with_prof

## OpenMP

- To execute the program's parallel version with shared memory and OpenMP (You may need to alter the number of threads in the source code - _divisors.h_), run the following commands:

      make sh_omp

## Open MPI

### Shared

- Run the following command for executing the program in an unique multicore machine with shared memory:

      make shared_run

### Distributed

- Run the following command for executing the program in multiple machines with distributed memory:

      make distributed_run

## Hybrid (OpenMP and Open MPI)

- Run the following for executing the parallel program in multiple machines (Distributed memory - MPI | Shared memory - OpenMP):

      make hybrid

# Optional Running

## Instance Generator

Inside _instances_ directory, you can generate your own instances by executing the command using the following template: `python3 instance_generator.py --length <number> --quantity <number>`

- Example: Generating an instance file with 10000 numbers, 30 bits long:

      python3 instance_generator.py -l 30 -n 10000

## Time graphics

Inside _plotting_ directory, you can generate the time graphics presented in this works report by running the following commmand:

    python3 times.py

Also, you can generate the graphics that compares execution time between the two libraries (OpenMP and Open MPI) with shared and distributed memory, just by running the following commmand:

    python3 benchmark.py
