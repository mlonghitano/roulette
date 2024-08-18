import random

def simulate_1326_system_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets):
    wins = 0
    final_bankrolls = []

    for _ in range(num_sets):
        bankroll = initial_bankroll
        bet_sequence = [1, 3, 2, 6]  # The 1-3-2-6 sequence
        sequence_index = 0  # Start at the first bet in the sequence
        bet = bet_sequence[sequence_index] * initial_bet

        for _ in range(num_rounds):
            # Simulate a roulette spin with a 47.2% chance to win and 52.8% chance to lose
            outcome = random.choices(['win', 'lose'], weights=[47.2, 52.8])[0]

            if outcome == 'win':
                bankroll += bet
                sequence_index += 1
                if sequence_index >= len(bet_sequence):
                    # If the end of the sequence is reached, reset to the start
                    sequence_index = 0
                bet = bet_sequence[sequence_index] * initial_bet
            else:
                bankroll -= bet
                # Reset to the beginning of the sequence after a loss
                sequence_index = 0
                bet = bet_sequence[sequence_index] * initial_bet

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
initial_bet = 1600
num_rounds = 10
num_sets = 10000000  # Number of sets to simulate

# Run the simulation
win_percentage, bankroll_range, final_bankrolls = simulate_1326_system_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets)

# Display results
print(f"Win Percentage: {win_percentage:.2f}%")
print(f"Final Bankroll Range: ${bankroll_range[0]} to ${bankroll_range[1]}")
