#include <stdio.h>
#include <cs50.h>

int
main(void)
{

    int mf, fm, ff, mm, total;
    
    //get mf
    do
    {
        printf("M spotting F: ");
        mf = GetInt();
    }
    while(mf < 0);
    
    // get fm
    do
    {
        printf("F spotting M: ");
        fm = GetInt();
    }
    while(fm < 0);
    
    //get ff
    do
    {
        printf("F spotting F: ");
        ff = GetInt();
    }
    while(ff < 0);
    
    //get mm
    do
    {
        printf("M spotting M: ");
        mm = GetInt();
    }
    while(mm < 0);
    
    //calculate total
    total = mf + fm + ff + mm;
    
    //calculate percentage & num of #'s
    mf = ( (float)mf/total ) * 80;
    fm = ( (float)fm/total ) * 80;
    ff = ( (float)ff/total ) * 80;
    mm = ( (float)mm/total ) * 80;
    
    //check
    if ( mf + fm + ff + mm > 80 )
        printf("Wtf? Reload chart plz");
    
    //the chart
    printf("\nWho is Spotting Whom?\n\n");
    printf("M spotting F\n");
    
    while( mf > 0 )
    {
        printf("#");
        mf--;
    }
    
    printf("\n");
    printf("F spotting M\n");
    
    while ( fm > 0 )
    {
        printf("#");
        fm--;
    }
    
    printf("\n");
    printf("F spotting F\n");
    
    while ( ff > 0 )
    {
        printf("#");
        ff--;
    }
    
    printf("\n");
    printf("M spotting M\n");
    
    while ( mm > 0 )
    {
        printf("#");
        mm--;
    }
    printf("\n");
}         
