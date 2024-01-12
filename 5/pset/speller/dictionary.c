// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char *word;
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 27; //26 + 1 für apostroph

FILE *dictp = NULL;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO


    return true;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    int i = 0;
    int h = tolower(word[i]) - 'A' - 6;
    if (word[i] == 39)
    {
        return 26;
    }
    return h;
    i++;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    dictp = fopen(dictionary, "r");
    if (fopen(dictionary,"r") != NULL)
    {
        char dictletter;
        while (fread(&dictletter, sizeof(char), 1, dictp))
        {

            int j = hash(&dictletter);
            table[j] = malloc(sizeof(node));
            node *2ndletter = table[j]->next
            do
            {
                int i = 0;
                fread(&dictletter, sizeof(char), 1, dictp);
                table[j]->word[i] = dictletter;
                fseek(dictp, 1,SEEK_CUR);
                i++;
            }
            while(dictletter != '\n');
            printf("%c", table[j]->word[0]);
        }

    }
    else
    {
        return false;
    }
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    int words = 0;
    int index = 0;
    char letter;
    while (fread(&letter, sizeof(char), 1, dictp))
    {

        if (letter == '\n')
        {
            words++;
        }
        fseek(dictp, 1, SEEK_CUR);
        index++;
    }
    return words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    free(dictp);
    return false;
}
