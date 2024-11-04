#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

pair<int, vector<int>> calculate_subsequence(const vector<int> &sequence)
{
    if (sequence.empty())
    {
        return {0, {}};
    }

    int n = sequence.size();
    vector<int> tail;
    vector<int> previous(n, -1);
    vector<int> indices(n, -1);

    for (int i = 0; i < n; ++i)
    {
        auto iterator = lower_bound(tail.begin(), tail.end(), sequence[i]);
        int idx = distance(tail.begin(), iterator);

        if (iterator == tail.end())
        {
            tail.push_back(sequence[i]);
        }
        else
        {
            *iterator = sequence[i];
        }

        indices[idx] = i;
        if (idx > 0)
        {
            previous[i] = indices[idx - 1];
        }
    }

    int max_length = tail.size();
    vector<int> solution;
    for (int i = indices[max_length - 1]; i >= 0; i = previous[i])
    {
        solution.push_back(sequence[i]);
    }

    reverse(solution.begin(), solution.end());

    return {max_length, solution};
}

int main()
{
    vector<int> sequence;
    int number;

    while (cin >> number)
    {
        sequence.push_back(number);
    }

    auto [length, solution] = calculate_subsequence(sequence);

    cout << length << endl;
    cout << '-' << endl;

    for (const int &element : solution)
    {
        cout << element << endl;
    }

    return 0;
}