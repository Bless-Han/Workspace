#ifndef STOCK00_H_
#define STOCK00_H_
#include <string>

class Stock
{
    private:
        std::string company;
        long shares;
        double share_val;
        double total_val;
        void set_tot() { total_val = shares * share_val; }
    public:
        Stock();
        Stock(const std::string & co, long n = 0, double pr = 0.0);
        ~Stock();
        void buy(long num, double price);
        void sell(long num, double price);
        void update(double price);
        void show() const;
        const Stock & topval(const Stock & s) const;
        std::string get_company();
        long get_shares();
        double get_share_val();
        double get_total_val();
};

#endif