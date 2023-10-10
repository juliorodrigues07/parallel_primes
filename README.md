[![C99](https://img.shields.io/badge/C-00599C?style=for-the-badge&logo=c&logoColor=white)](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf)
# Identifying Primes with Parallel Computing
Implementation of a master-slave parallel program (shared and distributed) to identify prime numbers in an array, utilizing Open MPI library (PA 1 from Parallel Computing course - DCOMP - UFSJ).

# Requirements

- [GCC](https://gcc.gnu.org/onlinedocs/gcc-12.2.0/gcc/) compiler and [Open MPI](https://www.open-mpi.org/doc/) library;

- To install all dependencies:

      ./install_dependencies.sh

# Optional Requirements

- [Python3](https://python.org) and [pip](https://pip.pypa.io/en/stable/installation/) package manager:

      sudo apt install python3 python3-pip build-essential python3-dev

- [PyCryptodome](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html) library:
 
      pip install pycryptodomex

# Compilation

Execute the following command to compile the source code:

    make

# Execution

You can alter the parameters, such as the instance file and number of processes in the _Makefile_. For distributed running, first you may need to gain remote acess to the machines in your network by generating a private key with the following commands:

    ssh-keygen
    ssh-copy-id <IP_address>
    ssh <IP_address>

Also, you may need to change parameters in the hostfile (_hosts.txt_), such as IP addresses and number of slots (CPU cores).

## Shared

Run the following command for executing the program in an unique multicore machine:

    make shared_run

## Distributed

Run the following command for executing the program in multiple machines:

    make distributed_run

# Optional Running

## Instance Generator

Inside _instances_ directory, you can generate your own instances by executing the command using the following template: `python3 instance_generator.py --length <number> --quantity <number>`

- Example: Generating an instance file with 10000 numbers, 30 bits long:

      python3 instance_generator -l 30 -n 10000
