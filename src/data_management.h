#ifndef __DATA_MANAGEMENT__
#define __DATA_MANAGEMENT__

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void read_file(char *file_name, int *values, int input_size);
void write_file(int *results, int output_size);
int get_input_size(char *file_name);
void save_execution_stats(double time);

#endif
