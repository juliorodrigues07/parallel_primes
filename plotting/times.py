import matplotlib.pyplot as plt
from seaborn import barplot
from os import getcwd


def plot_time(buffer, primes, mixed, composites):
    
    plt.grid()
    plt.title("Tempo de Execução entre Entradas")
    plt.xlabel('Quantidade de Processos')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(buffer)
    
    plt.plot(buffer, primes, color='g', label='prime.txt')
    plt.plot(buffer, composites, color='y', label='composite.txt')
    plt.plot(buffer, mixed, color='r', label='mixed.txt')
    plt.legend(loc='best')
    
    plt.savefig(f'{getcwd()}/parallel.svg', format='svg')
    plt.show()


def plot_by_instance(buffer, primes, instance_name):

    plt.grid()
    plt.title(f'Tempo de Execução ({instance_name})')
    plt.xlabel('Quantidade de Processos')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.xticks(buffer)

    plt.plot(buffer, primes, color='r')

    size = len(instance_name) - 4
    plt.savefig(f'{getcwd()}/{instance_name[:size]}.svg', format='svg')
    plt.show()


def plot_sequential(measures):

    fig, ax = plt.subplots(figsize=(12, 8))
    barplot(x=['prime.txt', 'composite.txt', 'mixed.txt'], y=measures, palette='Blues')

    ax.set_title('Tempo de Processamento entre Instâncias', fontsize=18)
    ax.set_ylabel("Tempo de Execução (segundos)", fontsize=14)
    ax.set_xlabel("Instância", fontsize=14)

    ax.grid(which='both')
    ax.grid(which='minor', alpha=0.8)
    ax.grid(which='major', alpha=0.8)
    plt.show()

    fig.savefig(f'{getcwd()}/sequential.svg', format='svg')

def main():

    buffer = [1, 2, 3, 4]

    primes = [0.044, 0.035, 0.02, 0.025]
    plot_by_instance(buffer, primes, 'prime.txt')

    composites = [430, 243, 187, 154]
    plot_by_instance(buffer, composites, 'composite.txt')

    mixed = [242, 129, 103, 82]
    plot_by_instance(buffer, mixed, 'mixed.txt')

    plot_time(buffer, primes, mixed, composites)

    sequential = [0.044, 242, 430]
    plot_sequential(sequential)


if __name__ == '__main__':
    main()
