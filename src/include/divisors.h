#ifndef __DIVISORS__
#define __DIVISORS__

#include <omp.h>

# ifdef _OPENMP
#define N_THREADS 2
# else
#define N_THREADS 1
# endif

#define EVEN 1
#define ODD 2

int count_divisors(int value);

#endif
