#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{

    int array[200] = {};

    string a;
    string b;

    cin >> a;
    cin >> b;

    int aposi = a.length() - 1, bposi = b.length() - 1;
    for (int i = bposi; i >= 0; i--)
    {

        for (int j = aposi; j >= 0; j--)
        {
            int answerposi = 199 - (aposi - j) - (bposi - i);

            // cout<<"i "<<i<< " j "<<j <<endl;

            int x = (a[j] - '0') * (b[i] - '0');

            array[answerposi] += x;
            //cout << "array[answerposi] " << array[answerposi] << endl;

            int k = answerposi;
            while (array[k] > 9)
            {
                int r = array[k] % 10;
                int c = array[k] / 10;
                array[k] = r;
                array[k - 1] += c;
                k--;
            }
        }
    }
    bool t = false;
    for (int i = 0; i < 200; i++)
    {
        if (array[i] > 0)
            t = true;
        if (t)
            cout << array[i];
    }
    if (t == false)
        cout << 0;
    cout << endl;



    return 0;
}