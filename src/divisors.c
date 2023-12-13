#include "include/divisors.h"

int count_divisors (int value) {

    if (value == 1)
        return 1;
    else {
        int divisors = 2;
        int square = sqrt(value);
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

        while (i <= limit) {

            // If checked as far as square root of N, and N doesn't have a divisor greater than 1, then it must be prime
            if (i > square && divisors == 2)
                return 2;
            else {
                if (value % i == 0)
                    divisors++;
            }
            i += step;
        }
        return divisors;
    }
}
