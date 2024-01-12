#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int years = 1;
    int population;
    // TODO: Prompt for end size
    for(population = 2000; population <= 1000000; population = population * 1.2)
    {
    // TODO: Calculate number of years until we reach threshold
    years += 1;
    printf("%d,people after, %d, years\n",population ,years);
    }
    // TODO: Print number of years
    years+=1;
    printf("Population is has reached over 1 Mio. people after %d years \n" ,years);
}
