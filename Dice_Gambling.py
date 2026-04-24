import random

def rollDice() -> bool:
    roll = random.randint(1,100)
    if roll == 100:
        print(roll, "Roll was 100, you lose! Play again")
        return False
    
    elif roll <= 50:
        print(roll, "Roll was in 1-50, you lose! Play again")
        return False

    elif 50 < roll < 100:
        print(roll, "Roll was in 51-99, you win! Play more")
        return True

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager # For simple better, we fix this to initial_wager for all runs.

    currentWagerNum = 0
    while currentWagerNum < wager_count:
        if rollDice():
            value += wager
        else:
            value -= wager
        currentWagerNum += 1

        print(f"Funds: {value}")

simple_bettor(10000, 100, 100)
    

