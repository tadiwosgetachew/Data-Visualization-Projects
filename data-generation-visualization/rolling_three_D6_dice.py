import pygal

from die import Die


# Create three D6 dice.
die1= Die()
die2 = Die()
die3 = Die()

# make rolls and store results in a list
results = []
for rolls in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)
# Analyze the results
frequencies = []
max_result = die1.num_sides + die2.num_sides + die3.num_sides
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Simulated results of rolling three D6 1000 times."
hist.x_labels = [x for x in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file("three_dice_visual.svg")