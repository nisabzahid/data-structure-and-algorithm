#include <iostream>

using namespace std;

void digit(int n)
{

    if (n < 0)
        n = -1 * n;
    if (n / 10)
    {
        digit(n / 10);
    }
    cout << n % 10 << endl;
}

int main()
{

    digit(1011210191);
    return 0;
}