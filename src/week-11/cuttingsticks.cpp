#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int minimal_cut_cost(int length, vector<int> &cuts)
{
    cuts.insert(cuts.begin(), 0);
    cuts.push_back(length);
    int cuts_size = cuts.size();

    vector<vector<int>> table(cuts_size, vector<int>(cuts_size, INT_MAX));

    for (int i = 0; i < cuts_size - 1; i++)
    {
        table[i][i + 1] = 0;
    }

    for (int length = 2; length < cuts_size; length++)
    {
        for (int i = 0; i < cuts_size - length; i++)
        {
            int j = i + length;
            for (int k = i + 1; k < j; k++)
            {
                table[i][j] = min(table[i][j], table[i][k] + table[k][j] + cuts[j] - cuts[i]);
            }
        }
    }

    return table[0][cuts_size - 1];
}

int main()
{
    int length;
    while (cin >> length && length != 0)
    {
        int n;
        cin >> n;
        vector<int> cuts(n);

        for (int i = 0; i < n; i++)
        {
            cin >> cuts[i];
        }

        int result = minimal_cut_cost(length, cuts);
        cout << "The minimum cutting is " << result << "." << endl;
    }
}