import random

# Define the Roulette wheel
roulette_wheel = {
    "0": "Green",
    "1": "Red", "2": "Black", "3": "Red", "4": "Black", "5": "Red", "6": "Black",
    "7": "Red", "8": "Black", "9": "Red", "10": "Black", "11": "Black", "12": "Red",
    "13": "Black", "14": "Red", "15": "Black", "16": "Red", "17": "Black", "18": "Red",
    "19": "Red", "20": "Black", "21": "Red", "22": "Black", "23": "Red", "24": "Black",
    "25": "Red", "26": "Black", "27": "Red", "28": "Black", "29": "Black", "30": "Red",
    "31": "Black", "32": "Red", "33": "Black", "34": "Red", "35": "Black", "36": "Red"
}

# Payout rates for different bets
payouts = {
    "straight": 35,  # 35:1
    "color": 1,      # 1:1
    "odd_even": 1,   # 1:1
    "high_low": 1,   # 1:1
    "dozens": 2,     # 2:1
    "columns": 2     # 2:1
}

# Function to spin the wheel
def spin_wheel():
    number = random.choice(list(roulette_wheel.keys()))
    color = roulette_wheel[number]
    return int(number), color

# Function to determine the outcome of a bet
def evaluate_bet(bet_type, bet_choice, spin_result):
    number, color = spin_result
    winnings = 0

    if bet_type == "straight":
        if int(bet_choice) == number:
            winnings = payouts["straight"]
    elif bet_type == "color":
        if bet_choice.lower() == color.lower():
            winnings = payouts["color"]
    elif bet_type == "odd_even":
        if bet_choice.lower() == "odd" and number % 2 != 0:
            winnings = payouts["odd_even"]
        elif bet_choice.lower() == "even" and number % 2 == 0:
            winnings = payouts["odd_even"]
    elif bet_type == "high_low":
        if bet_choice.lower() == "low" and 1 <= number <= 18:
            winnings = payouts["high_low"]
        elif bet_choice.lower() == "high" and 19 <= number <= 36:
            winnings = payouts["high_low"]
    elif bet_type == "dozens":
        if bet_choice == "1" and 1 <= number <= 12:
            winnings = payouts["dozens"]
        elif bet_choice == "2" and 13 <= number <= 24:
            winnings = payouts["dozens"]
        elif bet_choice == "3" and 25 <= number <= 36:
            winnings = payouts["dozens"]
    elif bet_type == "columns":
        if bet_choice == "1" and number % 3 == 1:
            winnings = payouts["columns"]
        elif bet_choice == "2" and number % 3 == 2:
            winnings = payouts["columns"]
        elif bet_choice == "3" and number % 3 == 0:
            winnings = payouts["columns"]

    return winnings

# Function for user input and simulation
def play_roulette():
    print("Welcome to the Roulette Table!")
    print("Available bets: straight, color, odd_even, high_low, dozens, columns")
    
    # Get user bet input
    bet_type = input("Enter the type of bet: ")
    bet_choice = input("Enter your choice (e.g., 17, Red, Odd, Low, 1 for dozens): ")
    bet_amount = float(input("Enter the amount you want to bet: "))
    
    # Spin the wheel
    spin_result = spin_wheel()
    print(f"\nThe wheel spins... Result: Number {spin_result[0]}, Color {spin_result[1]}")
    
    # Evaluate the bet
    winnings = evaluate_bet(bet_type, bet_choice, spin_result)
    if winnings > 0:
        print(f"Congratulations! You win ${bet_amount * winnings:.2f}!")
    else:
        print(f"Sorry, you lost ${bet_amount:.2f}. Better luck next time!")

# Run the game
if __name__ == "__main__":
    play_roulette()
