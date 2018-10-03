# ivory-melt
For Mx. Collins' AP Computer Science Principles class.

// A super dumb chatbot.
// Sinead Li, 10/3

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

// Declare my function RESPOND.
int respond(string e);

int main()
{
// The user inputs a string moved to RESPOND.
    string e;
    printf("Hello!\n");
    e = get_string("Do you want to hear a joke? (yes/no)\n");
    int r = respond(e);
// If the user said "No".
    if (r == 0)
    {
        printf("Bah, you're no fun.\n");
    }
// If the user said "Yes".
    else
    {
        printf("I bought a ceiling fan the other day.\n");
        printf("Complete waste of money. He just stands there applauding and saying \"Ooh, I love how smooth it is.\"\n");
    };
}

// RESPOND processes the input.
int respond(string e)
{
  int r, l;
// Any capitalization of input is fine.
  l = strlen(e);
  for (int i = 0; i < l; i++)
  {
      e[i] = toupper(e[i]);
  }
// If the user said "No", r = 0 moved to MAIN.
  r = strcmp(e, "NO");
  return r;
}
