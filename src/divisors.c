#include "include/divisors.h"

int count_divisors (int value) {

    if (value == 1)
        return 1;
    else {
        int divisors = 2;
        int limit = value / 2;

        int step, i;
        // Odd numbers aren't divisible by even numbers
        if (value % 2 == 0) {
            step = EVEN;
            i = 2;
        } else {
            step = ODD;
            i = 3;
        }

        int j;
        #pragma omp parallel for private(j) shared(limit, step, value) reduction(+:divisors) num_threads(N_THREADS)
        for (j = i; j <= limit; j += step) {
            if (value % j == 0)
                divisors++;
        }

        return divisors;
    }
}
