#include <cs50.h>
#include <stdio.h>


void left_side(int input,int i);
int main(void)
{
    //prompt user input
    int input = get_int("Enter height: ");
    int i;
    for(i = 0; i < input; i++)
    {
        left_side(input, i);





        printf("\n");
    }

}


void left_side(int input,int i)
{
    int j;
    for(j = 0; j < input - i - 1; j++)
    {
        printf(" ");
    }

    for(int k = 0; k < input - j; k++)
    {
        printf("#");
    }

}