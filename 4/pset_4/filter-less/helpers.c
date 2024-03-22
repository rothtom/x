#include "helpers.h"
#include <stdio.h>
int runde(int number);
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int score = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
            score = runde(score);
            image[i][j].rgbtBlue = score;
            image[i][j].rgbtGreen = score;
            image[i][j].rgbtRed = score;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int color[3];
            color[0] = image[i][j].rgbtRed * 0.393 + image[i][j].rgbtGreen * 0.769 + image[i][j].rgbtBlue * 0.189;
            color[1]  = image[i][j].rgbtRed * 0.349 + image[i][j].rgbtGreen * 0.686 + image[i][j].rgbtBlue * 0.168;
            color[2]  = image[i][j].rgbtRed * 0.272 + image[i][j].rgbtGreen * 0.534 + image[i][j].rgbtBlue * 0.131;
            for (int k = 0; k < 3; k++)
            {
                if (color[k] % 1 >= 0.5)
                {
                    color[k] += (color[k] % 1);
                }
                else if (color[k] < 0.5)
                {
                    color[k] += - (color[k] % 1);
                }
                color[k] = (int) color[k];
            }
            image[i][j].rgbtRed = (int) color[0];
            image[i][j].rgbtGreen = (int) color[1];
            image[i][j].rgbtBlue = (int) color[2];
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int half = (height / 2) + 1;
    for (int i = 0; i < half; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image [height - i][j];
            image[height - i][j] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE rimage[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            rimage[i][j] = image[i][j];
        }
    }
    for (int i = 1; i < height - 1; i++)
    {
        for (int j = 1; j < width - 1; j++)
        {
            int avg[3];
            for (int a = 0; a < 3; a++)
            {
                avg[a] = 0;
            }
            for (int r = 0; r < 3; r++)
            {
                for (int c = 0; c < 3; c++)
                {
                   avg[0] += rimage[i - 1 + r][j - 1 + c].rgbtRed;
                   avg[1] += rimage[i - 1 + r][j - 1 + c].rgbtGreen;
                   avg[2] += rimage[i - 1 + r][j - 1 + c].rgbtBlue;
                }
            }
            for (int a = 0; a < 3; a++)
            {
                avg[a] = avg[a] / 9.0;
                avg[a] = runde(avg[a]);
                if (a == 0)
                {
                    image[i][j].rgbtRed = avg[a];
                }
                else if (a == 1)
                {
                    image[i][j].rgbtGreen = avg[a];
                }
                else if (a == 2)
                {
                    image[i][j].rgbtBlue = avg[a];
                }
            }

        }
    }
    return;
}


int runde(int number)
{
    if (number % 1 >= 0.5)
    {
        number = number + (number % 1);
    }
    else if (number % 1 < 0.5)
    {
        number = number - (number % 1);
    }
    return number;
}