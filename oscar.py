import random

def simulate_oscars_grind_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets):
    wins = 0
    final_bankrolls = []

    for _ in range(num_sets):
        bankroll = initial_bankroll
        bet = initial_bet
        profit_goal = initial_bet  # The goal is to make a profit equal to the initial bet
        profit = 0  # Current profit within the series

        for _ in range(num_rounds):
            if profit >= profit_goal:
                # If the profit goal is met, stop the simulation for this set
                break

            # Simulate a roulette spin with a 47.2% chance to win and 52.8% chance to lose
            outcome = random.choices(['win', 'lose'], weights=[47.2, 52.8])[0]

            if outcome == 'win':
                bankroll += bet
                profit += bet
                # Increase the bet by one unit only if the profit goal hasn't been reached
                if profit < profit_goal:
                    bet += initial_bet
                # Ensure that the bet doesn't exceed the profit goal
                if bet > (profit_goal - profit):
                    bet = profit_goal - profit
            else:
                bankroll -= bet
                profit -= bet
                # Keep the bet the same after a loss
                bet = max(initial_bet, bet)

            # If bankroll drops below the current bet, stop the simulation
            if bankroll < bet:
                break

        # Track the final bankroll value
        final_bankrolls.append(bankroll)

        # Determine if this set is a win
        if bankroll > initial_bankroll:
            wins += 1

    # Calculate win percentage and bankroll range
    win_percentage = (wins / num_sets) * 100
    bankroll_range = (min(final_bankrolls), max(final_bankrolls))

    return win_percentage, bankroll_range, final_bankrolls

# Set your parameters
initial_bankroll = 1000
initial_bet = 150
num_rounds = 30
num_sets = 1000000  # Number of sets to simulate

# Run the simulation
win_percentage, bankroll_range, final_bankrolls = simulate_oscars_grind_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets)

# Display results
print(f"Win Percentage: {win_percentage:.2f}%")
print(f"Final Bankroll Range: ${bankroll_range[0]} to ${bankroll_range[1]}")
