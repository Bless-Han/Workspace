#include <iostream>
#include "stock00.h"
int main()
{
    Stock fluffy_the_cat;
    // Stock fluffy_the_cat("NanoSmart", 20, 12.50);
    // fluffy_the_cat.acquire("NanoSmart", 20, 12.50);
    fluffy_the_cat.show();
    {
        Stock temp("test");
    }
    fluffy_the_cat.buy(15, 18.125);
    fluffy_the_cat.show();
    fluffy_the_cat.sell(400, 20.00);
    fluffy_the_cat.show();
    fluffy_the_cat.buy(300000, 40.125);
    fluffy_the_cat.show();
    fluffy_the_cat.sell(300000, 0.125);
    fluffy_the_cat.show();
    return 0;
}