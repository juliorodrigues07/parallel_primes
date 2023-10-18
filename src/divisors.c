#include "divisors.h"

int count_divisors (int value) {

    if (value == 1)
        return 1;
    else {
        int divisors = 2;

        for (int i = 2; i <= value / 2; i++) {

            int square = sqrt(value);
            // If checked as far as square root of N, and N doesn't have a divisor greater than 1, then it must be prime
            if (i == square && divisors == 2)
                return 2;
            else {
                if (value % i == 0)
                    divisors++;
            }
        }

        return divisors;
    }
}