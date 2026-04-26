import random
import matplotlib.pyplot as plt

def rollDice() -> bool:
    roll = random.randint(1,100)
    if roll == 100:
        #print(roll, "Roll was 100, you lose! Play again")
        return False
    
    elif roll <= 50:
        #print(roll, "Roll was in 1-50, you lose! Play again")
        return False

    elif 50 < roll < 100:
        #print(roll, "Roll was in 51-99, you win! Play more")
        return True

def simple_bettor(funds, initial_wager, wager_count):
    value = funds
    wager = initial_wager # For simple better, we fix this to initial_wager for all runs.

    # Current Wager Count V/S Current Value for MC Simulation
    wX = []
    vY = []

    currentWagerNum = 1
    while currentWagerNum <= wager_count:
        wX.append(currentWagerNum)
        if rollDice():
            value += wager
        else:
            value -= wager
        vY.append(value)
        currentWagerNum += 1

    plt.plot(wX, vY)

x = 0 # Number of gamblers/bettors
while x < 1000:
    simple_bettor(10000, 100, 10000)
    x += 1

plt.xlabel('Wager Count')
plt.ylabel('Account Value')
plt.show()