import random

def simulate_fibonacci_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets):
    wins = 0
    final_bankrolls = []

    for _ in range(num_sets):
        bankroll = initial_bankroll
        fib_sequence = [initial_bet, initial_bet]  # Start the Fibonacci sequence with the first two elements
        fib_index = 0  # Start at the first element in the Fibonacci sequence
        bet = fib_sequence[fib_index]

        for _ in range(num_rounds):
            # Simulate a roulette spin with a 47.2% chance to win and 52.8% chance to lose
            outcome = random.choices(['win', 'lose'], weights=[47.2, 52.8])[0]

            if outcome == 'win':
                bankroll += bet
                # Move back two steps in the Fibonacci sequence, ensuring we don't go below index 0
                fib_index = max(0, fib_index - 2)
                bet = fib_sequence[fib_index]
            else:
                bankroll -= bet
                # Move to the next number in the Fibonacci sequence
                if fib_index + 1 < len(fib_sequence):
                    fib_index += 1
                else:
                    fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
                    fib_index += 1
                bet = fib_sequence[fib_index]

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
num_sets = 10000000 # Number of sets to simulate

# Run the simulation
win_percentage, bankroll_range, final_bankrolls = simulate_fibonacci_with_edge_and_tracking(initial_bankroll, initial_bet, num_rounds, num_sets)

# Display results
print(f"Win Percentage: {win_percentage:.2f}%")
print(f"Final Bankroll Range: ${bankroll_range[0]} to ${bankroll_range[1]}")
