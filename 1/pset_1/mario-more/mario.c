#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int input = get_int("Wdgth: ");

    for (int i = 0; i < input; i++)
    {
        int j;
        for (j = 0; j < input - i - 1; j++)
        {
            printf(" ");
        }

        for (int k = 0; k < input - j; k++)
        {
            printf("#");
        }

        printf("  ");

        for (int l = 0; l < input - j; l++)
        {
            printf("#");
        }

        printf("\n");
    }
}
