#include <iostream>
#include <cmath>

using std::cout;
using std::cin;

int main()
{
    for (int row = 1; row <= 11; row++)
    {
        // for height x triangle, choose height*2 - 1 = row
        for (int hashNum = 1; hashNum <= 6-abs(6-row); hashNum++)
        {
            cout << "#";
        }
        cout << "\n";
    }
}
