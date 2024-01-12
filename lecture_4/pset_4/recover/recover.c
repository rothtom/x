#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("2 cla only!\n");
        return 1;
    }

    FILE *file = fopen(argv[1], "r");

    if (file == NULL)
    {
        printf("couldn't open %s", argv[1]);
        return 1;
    }
    char *x[512];
    char *first_3_bytes[3] = {"ff", "d8", "ff"};
    char *fourth_byte [16] = {"e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "ea", "eb", "ec", "ed", "ee", "ef"};
    int picture_coordinates[50][2];
    int picture_count = 0;
    while(fread(&x, 1, 512, file) == 512)
    {
        int correct_start = 0;
        for (int i = 0; i < 3; i++)
        {
            printf("%s", x[0]);
            printf("%s", first_3_bytes[0]);
            if (strcmp(first_3_bytes[i], x[i]))
            {
                correct_start++;
            }
        }
        for (int i = 0; i < 16; i++)
        {
            if (strcmp(fourth_byte[i], x[3]))
            {
                correct_start++;
            }
        }
        if (correct_start == 4)
        {


            picture_count++;
        }

    }
    printf("%i\n", picture_count);
}