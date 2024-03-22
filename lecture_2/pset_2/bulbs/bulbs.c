#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string message = get_string("Message: ");
    int k = strlen(message);
    int decimal[k];

    for (int i = 0; i < k; i++)
    {
        decimal[i] = (int) message[i];
        // printf("%i\n", decimal[i]);

        int p = 8;
        int bin_num[p];
        int j = 0;
        while (decimal[i] > 0)
        {
            if (decimal[i] > pow(2, p))
            {
                decimal[i] = decimal[i] - pow(2, p);

                bin_num[j] = 1;
            }
            else
            {
                bin_num[j] = 0;
            }
            j++;
            p += -1;
            // printf("Bin: %i\n", bin_num[j]);
        }
        for (int b = 0; b < 8; b++)
        {
            print_bulb(bin_num[b]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}