import random

class RouletteGame:
    def __init__(self):
        self.red_numbers = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}
        self.black_numbers = {2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35}
        self.roulette_wheel = list(range(37))  # 0 to 36

    def spin_wheel(self):
        return random.choice(self.roulette_wheel)

    def run_scenario(self):
        # Initial balances after Player 1 gives $500 to Player 2
        players = {"Player 1": 500, "Player 2": 1500}

        # Single spin of the wheel
        outcome = self.spin_wheel()

        # Player 1 bets $500 on red, Player 2 bets $1500 on black
        if outcome in self.red_numbers:
            players["Player 1"] += 500  # Player 1 wins their bet amount
            players["Player 2"] -= 1500  # Player 2 loses their bet amount
        elif outcome in self.black_numbers:
            players["Player 1"] -= 500  # Player 1 loses their bet amount
            players["Player 2"] += 1500  # Player 2 wins their bet amount

        # Final balances after splitting winnings evenly
        total_balance = players["Player 1"] + players["Player 2"]
        players["Player 1"] = players["Player 2"] = total_balance // 2

        # Determine if the scenario is a win or loss
        if players["Player 1"] == 1500 and players["Player 2"] == 1500:
            return 1  # WIN
        else:
            return 0  # LOSS

    def simulate_scenarios(self, num_trials):
        results = []

        for _ in range(num_trials):
            result = self.run_scenario()
            results.append(result)

        win_percentage = sum(results) / num_trials * 100
        return results, win_percentage

if __name__ == "__main__":
    game = RouletteGame()

    # Input the number of times to run the scenario
    num_trials = int(input("Enter the number of times to test the scenario: "))

    results, win_percentage = game.simulate_scenarios(num_trials)

    print(f"\nResults: {results}")
    print(f"Win Percentage: {win_percentage:.2f}%")
