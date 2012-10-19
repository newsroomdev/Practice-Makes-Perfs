#include <stdio.h>
#include <cs50.h>
#include <math.h>

int
main(void)
{
float change;
int counter = 0, coins;
    //get change
    do
    {
        printf("How much change is owed?\n");
        change = GetFloat();    
    }
    while (change <= 0);
    
    //convert to coins
    coins = round(change * 100);
    
    //count up quarters
    while (coins >= 25)
    {
        coins -= 25;
        counter++;   
    }
    
    //count up dimes
    while (coins >= 10)
    {
        coins -= 10;
        counter++;
    }
    
    //count up nickels
    while (coins >= 5)
    {
        coins -= 5;
        counter++;
    }
    
    //count up pennies
    while (coins >= 1)
    {
        coins -= 1;
        counter++;
    }
    
    //print out total number of coins
    printf("%d\n", counter);
}
