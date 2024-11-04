#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>

using namespace std;

int N10_VALUE = 10;
int N5_VALUE = 5;
int N1_VALUE = 1;
int SODA_COST = 8;

int calculate_minimal_coins_to_buy_soda(
    int soda_amount,
    int n1_amount,
    int n5_amount,
    int n10_amount)
{
    vector<vector<vector<int>>> memo(152, vector<vector<int>>(155, vector<int>(52, -1)));
    memo[0][n5_amount][n10_amount] = 0;
    int coins_sum = n10_amount * 10 + n5_amount * 5 + n1_amount;

    for (int i = 0; i < soda_amount; i++)
    {
        int left_coins = coins_sum - i * SODA_COST;

        for (int j = 0; j <= n5_amount + n10_amount; ++j)
        {
            for (int k = 0; k <= n10_amount; ++k)
            {
                if (memo[i][j][k] == -1)
                    continue;

                int remaining = left_coins - j * 5 - k * 10;

                // caso 1 : moeda de 10
                if (k >= 1)
                {
                    if (memo[i + 1][j][k - 1] == -1)
                        memo[i + 1][j][k - 1] = 1e7;
                    memo[i + 1][j][k - 1] = min(memo[i + 1][j][k - 1], 1 + memo[i][j][k]);
                }

                // caso 2 : uma moeda de 10 e três moedas de 1
                if (k >= 1 && remaining >= 3)
                {
                    if (memo[i + 1][j + 1][k - 1] == -1)
                        memo[i + 1][j + 1][k - 1] = 1e7;
                    memo[i + 1][j + 1][k - 1] = min(memo[i + 1][j + 1][k - 1], 4 + memo[i][j][k]);
                }

                // caso 3 : duas moedas de 5
                if (j >= 2)
                {
                    if (memo[i + 1][j - 2][k] == -1)
                        memo[i + 1][j - 2][k] = 1e7;
                    memo[i + 1][j - 2][k] = min(memo[i + 1][j - 2][k], 2 + memo[i][j][k]);
                }

                // caso 4 : uma moeda de 5 e três de 1
                if (remaining >= 3 && j >= 1)
                {
                    if (memo[i + 1][j - 1][k] == -1)
                        memo[i + 1][j - 1][k] = 1e7;
                    memo[i + 1][j - 1][k] = min(memo[i + 1][j - 1][k], 4 + memo[i][j][k]);
                }

                // caso 5 : usa oito moedas de 1
                if (remaining >= SODA_COST)
                {
                    if (memo[i + 1][j][k] == -1)
                        memo[i + 1][j][k] = 1e7;
                    memo[i + 1][j][k] = min(memo[i + 1][j][k], SODA_COST + memo[i][j][k]);
                }
            }
        }
    }

    int best = 1e7;
    for (int j = 0; j <= n5_amount + n10_amount; ++j)
    {
        for (int k = 0; k <= n10_amount; ++k)
        {
            if (memo[soda_amount][j][k] == -1)
                continue;
            best = min(best, memo[soda_amount][j][k]);
        }
    }
    return best;
}

int main()
{
    int test_cases;
    cin >> test_cases;

    while (test_cases--)
    {
        int soda_amount, n1_amount, n5_amount, n10_amount;
        cin >> soda_amount >> n1_amount >> n5_amount >> n10_amount;
        int result = calculate_minimal_coins_to_buy_soda(
            soda_amount,
            n1_amount,
            n5_amount,
            n10_amount);
        cout << result << endl;
    }

    return 0;
}