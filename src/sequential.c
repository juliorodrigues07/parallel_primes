#include <time.h>
#include "data_management.h"
#include "divisors.h"

int main(int argc, char **argv) {

    if (argc != 2) {
        fprintf(stderr, "Incorrect number of arguments.\n");
        fprintf(stderr, "Usage: %s <path/to/file>\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    char *file_name = argv[1];
    int input_size = get_input_size(file_name);

    int *values = (int *) malloc (input_size * sizeof(int));
    read_file(file_name, values, input_size);

    // Could also store the results overwriting the input array
    int *results = (int *) malloc (input_size * sizeof(int));

    clock_t begin = clock();
    for (int i = 0; i < input_size; i++)
        results[i] = count_divisors(values[i]);
    clock_t end = clock();

    printf("Processing time: %0.3lfs\n", (double) (end - begin) / CLOCKS_PER_SEC);

    free(results);
    free(values);
    return 0;
}
