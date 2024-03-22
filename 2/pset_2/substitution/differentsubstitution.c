#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool check_letters(string test);
int rotate (int letter, int key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Must contain exactly 1 cla!\n");
        return 1;
    }

    bool correct_input_type = check_letters(argv[1]);
    bool correct_input_length;
    if (strlen(argv[1]) == 26)
    {
        correct_input_length = true;
    }
    else
    {
        correct_input_length = false;
    }

    if (correct_input_type != true && correct_input_length != true)
    {
        printf("Must contain exactly 26 letters\n");
        return 1;
    }
    string p_text = get_string("Plain text: ");
    int key[strlen(argv[1])];
    int p_text_nums[strlen(argv[1])];
    int c_text_nums[strlen(argv[1])];
    char c_text[strlen(argv[1])];

    printf("Cypher text: ");

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        key[i] = (int) argv[1][i];
        if (key[i] <= 90)
        {
            key[i] = key[i] - 90 + 26;
        }
        else if (key[i] <= 122)
        {
            key[i] = key[i] - 122 + 26;
        }
    }

    int right_key_num;
    for (int i = 0; i < strlen(p_text); i++)
    {
        if (isalpha(p_text[i]) != 0)
        {
            p_text_nums[i] = (int) p_text[i];

            if (isupper(p_text_nums[i]) != 0)
            {
                right_key_num = p_text_nums[i] - 65;
            }
            else if (isupper(p_text[i]) == false)
            {
                right_key_num = p_text_nums[i] - 97;
            }

            c_text_nums[i] = rotate(p_text_nums[i], key[right_key_num]);
            c_text[i] = (char) c_text_nums[i];
        }
        else
        {
            c_text[i] = p_text[i];
        }
        printf("%c", c_text[i]);
    }
    printf("\n");
}



bool check_letters(string test)
{
    int correctness = 0; //counts correct input (letters)
    for (int i = 0; i < strlen(test); i++)
    {
        if (isalpha(test[i]) == true)
        {
            correctness += 1;
        }
    }
    if (correctness == strlen(test))
    {
        return true;
    }
    else
    {
        return false;
    }

}

int rotate (int p_letter, int key) //rotates letter by key places
{
    int c_letter = p_letter + key;
    while ((c_letter >= 90 && c_letter <= 122)|| (c_letter >= 122 && c_letter >= 97))
    {
        c_letter += -26;
    }
    return c_letter;
}