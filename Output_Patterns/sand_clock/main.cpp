#include <iostream>

using std::cout;
using std::cin;

int main()
{
    int row, space, hash;
    int n = 5;

    // Facing Downwards
    for (row = n; row >= 1; row--)
    {
        for (space = 1; space <= n-row; space++)
        {
            cout << " ";
        }

        for (hash = 1; hash <= row*2; hash++)
        {
            cout << "#";
        }

        cout << "\n";
    }

    for (row = 1; row <= n; row++)
    {
        for (space = 1; space <= n-row; space++)
        {
            cout << " ";
        }

        for (hash = 1; hash <= row*2; hash++)
        {
            cout << "#";
        }
        cout << "\n";
    }

}