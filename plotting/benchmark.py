from times import plot_sequential
import matplotlib.pyplot as plt
from os import getcwd
import numpy as np


def plot_shared(buffer, strat1, strat2):

    plt.grid()
    plt.title("Tempo de Execução em Memória Compartilhada")
    plt.xlabel(f'Quantidade de Threads/Processos')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(buffer)

    plt.plot(buffer, strat1, color='g', label='OpenMP')
    plt.plot(buffer, strat2, color='r', label='Open MPI')
    plt.legend(loc='best')

    plt.savefig(f'{getcwd()}/parallel_shared.svg', format='svg')
    plt.show()


def plot_distributed(buffer, strat1, strat2):

    plt.grid()
    plt.title("Tempo de Execução em Memória Distribuída (6 threads)")
    plt.xlabel(f'Quantidade de Máquinas')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(buffer)

    plt.plot(buffer, strat1, color='g', label='Open MPI')
    plt.plot(buffer, strat2, color='r', label='Híbrido (OpenMP + MPI)')
    plt.legend(loc='best')

    plt.savefig(f'{getcwd()}/parallel_distributed.svg', format='svg')
    plt.show()


def main():

    buffer = [2, 3, 4, 5, 6]

    sequential = [0.04, 290, 550]
    plot_sequential(sequential)

    shared_omp = [155, 107, 80, 66, 62]
    shared_mpi = [144, 102, 76, 63, 59]
    plot_shared(buffer, shared_omp, shared_mpi)

    dist_mpi = [31, 22, 17, 16, 13]
    dist_hyb = [np.nan, 24, 17, 17, 14]
    plot_distributed(buffer, dist_mpi, dist_hyb)


if __name__ == '__main__':
    main()
