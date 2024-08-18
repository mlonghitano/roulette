import random

def simulate_labouchere_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets):
    wins = 0
    final_bankrolls = []

    for _ in range(num_sets):
        bankroll = initial_bankroll
        sequence = [1, 2, 3, 4, 5]  # Starting sequence; can be adjusted
        bet = (sequence[0] + sequence[-1]) * initial_bet

        for _ in range(num_rounds):
            if len(sequence) == 0:
                # If the sequence is completely cancelled, stop the simulation
                break

            # Simulate a roulette spin with a 47.2% chance to win and 52.8% chance to lose
            outcome = random.choices(['win', 'lose'], weights=[47.2, 52.8])[0]

            if outcome == 'win':
                bankroll += bet
                # Cross out the first and last numbers in the sequence
                sequence.pop(0)  # Remove the first element
                if len(sequence) > 0:
                    sequence.pop(-1)  # Remove the last element if the sequence is not empty

            else:
                bankroll -= bet
                # Add the bet amount to the end of the sequence
                sequence.append(bet // initial_bet)

            # If the sequence is not empty, calculate the new bet
            if len(sequence) > 0:
                bet = (sequence[0] + sequence[-1]) * initial_bet

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
num_sets = 10000000  # Number of sets to simulate

# Run the simulation
win_percentage, bankroll_range, final_bankrolls = simulate_labouchere_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets)

# Display results
print(f"Win Percentage: {win_percentage:.2f}%")
print(f"Final Bankroll Range: ${bankroll_range[0]} to ${bankroll_range[1]}")
