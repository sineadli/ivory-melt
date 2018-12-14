'''
The user enters three numbers, which are then transferred from one to another (printed out) until all have the same amount.
Sinead Li, Magda Ellis, Kate Ferrence, Grace Amjad.
12/13/18
'''

#include <cs50.h>
#include <ctype.h>
#include <libgen.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

float num_1, num_2, num_3;
bool stop;

void transfer();

int main()
{
    num_1 = get_float("Enter the first number: ");
    num_2 = get_float("Enter the second number: ");

    do {
    num_3 = get_float("Enter the third number: ");
    } while ((int)(num_1 + num_2 + num_3) % 3 != 0);

    while((num_1 != num_2) && (num_2 != num_3)){
        transfer();
        printf("\nFirst number: %f\nSecond number: %f\nThird number: %f\n", num_1, num_2, num_3);
    }
};

void transfer(){
    float temp_1 = num_1;
    float temp_2 = num_2;

    num_1 = (num_1 / 2) + (num_3 / 2);
    num_2 = (num_2 / 2) + (temp_1 / 2);
    num_3 = (num_3 / 2) + (temp_2 / 2);
}
