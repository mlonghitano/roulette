import random

def simulate_martingale_with_edge(initial_bankroll, initial_bet, num_rounds):
    bankroll = initial_bankroll
    bet = initial_bet
    results = []

    for _ in range(num_rounds):
        # Simulate a roulette spin with a 47.2% chance to win and 52.8% chance to lose
        outcome = random.choices(['win', 'lose'], weights=[47.2, 52.8])[0]

        if outcome == 'win':
            bankroll += bet
            bet = initial_bet  # Reset to the initial bet
        else:
            bankroll -= bet
            bet *= 2  # Double the bet after a loss

        # Track the results of each round
        results.append((outcome, bet, bankroll))

        # If bankroll drops below the current bet, stop the simulation
        if bankroll < bet:
            print("Bankroll exhausted, cannot continue the strategy.")
            break

    return results

# Set your parameters
initial_bankroll = 1000
initial_bet = 10
num_rounds = 7

# Run the simulation
simulation_results = simulate_martingale_with_edge(initial_bankroll, initial_bet, num_rounds)

# Print the results
for round_num, (outcome, bet, bankroll) in enumerate(simulation_results, 1):
    print(f"Round {round_num}: Outcome: {outcome}, Bet: ${bet}, Bankroll: ${bankroll}")

