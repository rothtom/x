#include <cs50.h>
#include <math.h>
#include <stdio.h>

long card_number;
int digit_sum;
long this_digit;
int leftover_digit_sum;
int num_of_digits = 0;

int get_digit(int starting_digit);
int howmany_digits(long number);
int get_specific_digit(long number, int specific_digit);

int main(void)
{

    do
    {
        card_number = get_long("Whats your creditcard number?");
    }
    while (card_number <= 1000000000000);

    leftover_digit_sum = get_digit(1);
    digit_sum = get_digit(2);

    num_of_digits = howmany_digits(card_number);
    int first_digit = get_specific_digit(card_number, 1);
    int second_digit = get_specific_digit(card_number, 2);
    int first_two_digits = (first_digit * 10) + second_digit;
    printf("first two digits: %i\n", first_two_digits);

    printf("leftover digit sum: %i\n", leftover_digit_sum);
    printf("digit sum: %i\n", digit_sum);
    int overall_digit_sum = digit_sum + leftover_digit_sum;
    printf("Overall digit sum: %i\n", overall_digit_sum);

    if (overall_digit_sum % 10 == 0 && overall_digit_sum != 0)
    {
        bool checksum = true;
        if ((num_of_digits == 13 || num_of_digits == 16) && (first_two_digits == 40 || first_two_digits == 41 || first_two_digits== 42))
        {
            printf("sum of those digits: %i \n", overall_digit_sum);
            printf("Visa!\n");
            printf("valid!\n");
        }

        else if (checksum == false)
        {
            printf("invalid");
        }
    }
}

int get_digit(int starting_digit)
{
    digit_sum = 0;
    long d = pow(10, starting_digit - 1);
    do
    {
        // printf("d = %li\n", d);
        this_digit = card_number / d;
        int remainder_digit = this_digit % 10;
        d = d * 100;
        remainder_digit = remainder_digit * starting_digit; // only works with staring_digit = 1 or 2

        if (remainder_digit >= 10)
        {
            int remainder_digit_1 = remainder_digit % 10;
            int remainder_digit_2 = (remainder_digit / 10) % 10;
            digit_sum += remainder_digit_1 + remainder_digit_2;
        }
        else
        {
            digit_sum += remainder_digit;
        }

        printf("this digit: %li \n", this_digit);
        printf("remainder digit: %i \n", remainder_digit);
    }
    while (this_digit >= 10);

    return digit_sum;
}

int howmany_digits(long number)
{
    num_of_digits = 1;
    long d = 10;

    do
    {
        number = number / d;
        num_of_digits += 1;
    }
    while (number >= 10);

    printf("num of digits: %i\n", num_of_digits);

    return num_of_digits;
}

int get_specific_digit(long number, int specific_digit)
{
    int z;
    long d = 1;
    for (int i = 0; i < num_of_digits - specific_digit; i++)
    {
        d = d * 10;
        z = (number / d) % 10;
    }
    return z;
}