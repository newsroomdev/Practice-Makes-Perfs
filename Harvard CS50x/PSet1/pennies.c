#include <stdio.h>
#include <cs50.h>
#include <math.h>

int
main(void)
{
   //initialize variables
   long long t;
   long long p;
   
   //get the number of days
   do
   {
   printf("Days in month: ");
   t = GetInt();
   }
   while (t < 28 || t > 31);
   
   //get the number of pennies
   do
   {
   printf("Pennies on first day: ");
   p = GetLongLong();
   }
   while (p <= 0);
   
   //multiply by two a day, convert to dollars & print
   printf("$%.2f\n", ((pow(2, t)-1)*p)/100.0);
}
