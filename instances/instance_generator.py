from Cryptodome.Random.random import getrandbits
from Cryptodome.Random.random import randint
from Cryptodome.Util.number import getPrime
from Cryptodome.Util.number import isPrime
from argparse import ArgumentParser
from datetime import datetime
from os import getcwd
from sys import argv


def generate_instances():

    argpar = ArgumentParser()
    argpar.add_argument("-l", "--length", type=int, default=2, help="Generated numbers maximum length in bits.")
    argpar.add_argument("-n", "--quantity", type=int, default=1, help="Amount of numbers to be generated.")
    args = vars(argpar.parse_args())

    if args['length'] <= 1:
        print(f'Maximum length in bits must be greater than one!')
        exit(127)

    if args['quantity'] <= 0:
        print(f'Amount of numbers must be greater than zero!')
        exit(128)

    size = args['length']
    n = args['quantity']

    now = datetime.now()
    file_name = f'Instance - {str(now.date())} | {str(now.hour)}:{str(now.minute)}:{str(now.second)}'

    with open(f'{getcwd()}/{file_name}.txt', 'w') as instance_file:

        for i in range(n):
            number_type = randint(0, 1)

            if number_type == 0:
                generate = getrandbits(size)

                while isPrime(generate):
                    generate = getrandbits(size)

                instance_file.write(f'{generate}\n')
            else:
                generate = getPrime(size)
                instance_file.write(f'{generate}\n')


if __name__ == '__main__':
    generate_instances()
