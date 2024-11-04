def calculate_winning_streak(bets):
    max_current = max_global = 0
    for bet in bets:
        max_current = max(bet, max_current + bet)
        max_global = max(max_global, max_current)

    return max_global

while True:
    entry = input()
    if entry == "0": break

    bets = list(map(int, input().split()))
    max_gain = calculate_winning_streak(bets)

    if max_gain > 0:
        print(f"The maximum winning streak is {max_gain}.")
    else:
        print("Losing streak.")
