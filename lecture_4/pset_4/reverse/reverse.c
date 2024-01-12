#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

#include "wav.h"

bool check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Use exactly 2 cla!\n");
        return 1;
    }

    //if (check_format() != true)
    //{
    //    printf("Wrong file format of input file!\n");
    //    return 2;
    //}


    // Open input file for reading
    // TODO #2
    char *infile = argv[1];
    char *outfile = argv[2];

    // Open input file
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 1;
    }

    // Open output file
    FILE *outptr = fopen(outfile, "r");
    if (outptr == NULL)
    {
        printf("couldn't open %s\n", outfile);
        return 1;
    }

    // Read header
    // TODO #3
    char *header = malloc(44);

    for (int i = 0; i < 44; i++)
    {
        int fpointer = fseek(inptr, (i - 1) * sizeof(char), SEEK_SET);
        printf("%i\n", fpointer);
        fread(header[i], sizeof(char), 1, fpointer);
        printf("Whats there: %c\n", header[i]);
    }


    WAVHEADER.

    // Use check_format to ensure WAV format
    // TODO #4

    // Open output file for writing
    // TODO #5

    // Write header to file
    // TODO #6

    // Use get_block_size to calculate size of block
    // TODO #7

    // Write reversed audio to file
    // TODO #8
}

bool check_format(WAVHEADER header)
{
    // TODO #4
    return 0;
}

int get_block_size(WAVHEADER header)
{
    // TODO #7
    return 0;
}