#include<stdio.h>
#include<stdlib.h>
#include<time.h>
int main()
{
    int number,guess,nguesses=1;
    srand(time(0));
    number=rand()%100+1;      //generate a random number between 1 to 100
   // printf("\n the number is%d",number);
    do
    {
        printf(" guss the number between 1 to 100\n");
        scanf("%d",&guess);
        if (guess>number)
        {
            printf("\n lower number please");
        }
        else if (guess<number)
        {
            printf("\n higher number please");
        }
        else
        {
            printf("\n your gussed it in %d attempt",nguesses);
        }
        nguesses++;
        
    } while (guess!=number);
    
    
    return 0;
}