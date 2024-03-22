#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int count_letters (string text);
int count_words (string text);
int count_sentences (string text);

int main(void)
{
    string text = get_string("Write text here! ");

    int sentences = count_sentences(text);
    printf("Sentences: %i\n", sentences);

    int words = count_words(text);
    printf("Words: %i\n", words);

    int letters = count_letters(text);
    printf("Letters: %i\n", letters);


    int L = (letters * 100) / words;
    int S = (sentences * 100) / words;


    int index = 0.0588 * L - 0.296 * S - 15.8;

    if (index % 1 >= 5)
    {
        index += 1 - (index % 1);
    }
    else
    {
        index += (index % 1);
    }

    if (index > 16)
    {
        string s_index = "16+";
        printf("Grade: %s", s_index);
    }
    else if (index < 1)
    {
        string s_index = "Before 1";
        printf("Grade: %s", s_index);
    }
    else
    {
        printf("Grade: %i", index);
    }
    printf("\n");
}





int count_letters (string text)
{
    int letters = 0;
    int i = 0;
    while (text[i] != '\0')
    {
        if (tolower (text[i]) >= 97 && tolower (text[i]) <= 122)
        {
            letters++;
        }
        i++;
    }
    return letters;
}



int count_words (string text)
{
    int words = 1; //because it doesnt end with ' '
    int i = 0;
    while (text[i] != '\0')
    {
        if (text[i] == ' ')
        {
            words++;
        }
        i++;
    }
    return words;
}

int count_sentences (string text)
{
    int sentences = 0;
    int i = 0;
    while (text[i] != '\0')
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences++;
        }
        i++;
    }
    return sentences;
}