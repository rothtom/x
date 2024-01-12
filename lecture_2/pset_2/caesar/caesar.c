#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int k;

bool only_digits (string test);
int rotate (int start_letter);

int main(int argc, string argv[])
{
        bool correct_input = only_digits(argv[1]);
    if (correct_input != true)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    if (argc != 2)
    {
        printf("Wrong input length!\n");
        return 1;
    }

    k = -48;
    int h = 0;
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        k = k + argv[1][h];
        h++;
        printf("%i\n", k);
    }

    string plain_input = get_string("Plain text: ");

    while (k > 26)
    {
        k = k / 26;
    }

    int p_text_length = strlen(plain_input);
    int p_text[p_text_length];
    int c_text[p_text_length];

    for (int i = 0;i < p_text_length; i++)
    {
        p_text[i] = (int) plain_input[i];
    }
    bool upper;
    int j = 0;
    printf("Cypher text: ");
    while (plain_input[j] != '\0')
    {
        if ((p_text[j] >= 65 && p_text[j] <= 90)||(p_text[j] >= 97 && p_text[j] <= 122))
        {
            if (isupper(plain_input[j]) == true) //check if upper
            {
                upper = true;
            }
            else
            {
                upper = false;
            }

            if (upper == true)
            {
                p_text[j] = tolower(p_text[j]);
                c_text[j] = rotate(p_text[j]);
                c_text[j] = toupper(c_text[j]);
            }
            else
            {
                c_text[j] = rotate(p_text[j]);
            }
        printf("%c", c_text[j]);
        j++;
        }
    }
    printf("\n");
}

int rotate (int starting_letter)
{
    int resulting_letter = starting_letter + k;
    while (resulting_letter > 122)
    {
        resulting_letter += -26;
    }
    return resulting_letter;
}

    bool only_digits(string test)
{
    bool digit = false;
    for(int i = 0; i < strlen(test); i++)
    {
        if(isdigit(test[i]))
        {
            digit = true;
        }
    }
    return digit;
}
