import random

def simulate_reverse_martingale_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets):
    wins = 0
    final_bankrolls = []

    for _ in range(num_sets):
        bankroll = initial_bankroll
        bet = initial_bet
        consecutive_wins = 0

        for _ in range(num_rounds):
            # Simulate a roulette spin with a 47.2% chance to win and 52.8% chance to lose
            outcome = random.choices(['win', 'lose'], weights=[47.2, 52.8])[0]

            if outcome == 'win':
                bankroll += bet
                consecutive_wins += 1
                if consecutive_wins == 3:
                    # After 3 consecutive wins, take the profit and reset to base bet
                    consecutive_wins = 0
                    bet = initial_bet
                else:
                    # Double the bet after a win
                    bet *= 2
            else:
                bankroll -= bet
                # Reset to base bet after a loss
                bet = initial_bet
                consecutive_wins = 0

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
initial_bankroll = 10000
initial_bet = 100
num_rounds = 7
num_sets = 1000000 # Number of sets to simulate

# Run the simulation
win_percentage, bankroll_range, final_bankrolls = simulate_reverse_martingale_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets)

# Display results
print(f"Win Percentage: {win_percentage:.2f}%")
print(f"Final Bankroll Range: ${bankroll_range[0]} to ${bankroll_range[1]}")
