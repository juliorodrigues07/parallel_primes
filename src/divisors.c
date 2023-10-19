#include "divisors.h"

#define EVEN 1
#define ODD 2

int count_divisors (int value) {

    if (value == 1)
        return 1;
    else {
        int divisors = 2;
        int square = sqrt(value);
        int limit = value / 2;

        // Odd numbers aren't divisible by even numbers
        int step = (value % 2 == 0) ? EVEN : ODD;

        for (int i = 2; i <= limit; i += step) {

            // If checked as far as square root of N, and N doesn't have a divisor greater than 1, then it must be prime
            if (i > square && divisors == 2)
                return 2;
            else {
                if (value % i == 0)
                    divisors++;
            }
        }
        return divisors;
    }
}