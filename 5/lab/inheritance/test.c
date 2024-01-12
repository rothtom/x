#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main (void)
{
    srand(time(0));
    int r = rand();
    printf("%i\n", r%3);
}