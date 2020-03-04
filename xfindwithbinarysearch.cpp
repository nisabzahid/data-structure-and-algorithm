#include <iostream>

using namespace std;
#define ll long long
//finding the squire root of a number x throught binary search

int findx(ll y, ll a, ll b, ll c, ll d, ll left, ll right)
{

    long long x = (left + right) / 2;
   // cout<<" x "<<x<<endl;

    long long value = (a * (x * x * x)) + (b * (x * x)) + (c * (x)) + d;
   // cout<<value<<" value "<<endl;
    if (y == value)
        return x;
    else
    {

        if ((value) < y)
            left = x + 1;
        else
            right = x - 1;
        //cout << left << " " << right << " x " << x << endl;

        return findx(y, a, b, c, d, left, right);
    }
}

int main()
{
    long long a, b, c, d, x, y, left, right;
    //scanf("%lld%lld%lld%lld%lld", &y, &a, &b, &c, &d);

    cin >> y >> a >> b >> c >> d;
    left = 0, right = 10;

    printf("%d", findx(y, a, b, c, d, left, right));
    cout << endl;

    return 0;
}