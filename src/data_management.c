#include "data_management.h"

void read_file (char *file_name, int *values, int input_size) {

    FILE* input_file = fopen(file_name, "r");
    if (input_file == NULL) {
        perror("Failed opening file!\n");
        exit(EXIT_FAILURE);
    }

    // Reads the input file, putting its values in an array
    for (int i = 0; i < input_size; i++)
        fscanf(input_file, "%d\n", &values[i]);
    fclose(input_file);
}

void write_file (int *results, int output_size) {

    const char *file_name = "saida.txt";
    FILE* output_file = fopen(file_name, "w");

    if (output_file == NULL) {
        perror("An error occur creating the output file.\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < output_size; i++)
        fprintf(output_file, "%d\n", results[i]);
    fclose(output_file);
}

void save_execution_stats (double time) {

    const char *file_name = "time.txt";
    FILE* output_file = fopen(file_name, "w");

    if (output_file == NULL) {
        perror("An error occur creating the output file.\n");
        exit(EXIT_FAILURE);
    }

    fprintf(output_file, "Processing time: %0.3lfs\n", time);
    fclose(output_file);
}


int get_input_size (char *file_name) {

    int input_size;
    int length = (int) strlen(file_name);

    char *command = (char *) malloc ((length + 9) * sizeof(char));
    strcpy(command, "wc -l < ");

    // Gets the input size (how many lines the file has)
    FILE* file = popen(strcat(command, file_name), "r");
    fscanf(file, "%d", &input_size);
    pclose(file);

    free(command);
    return input_size;
}
