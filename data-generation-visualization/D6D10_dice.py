import pygal

from die import Die


# Create a D6 and a D10.
die1= Die()
die2 = Die(10)

# make rolls and store results in a list
results = []
for rolls in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)
# Analyze the results
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = "Simulated results of rolling a D6 and a D10 50,000 times."
hist.x_labels = [x for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file("dice_D6D10_visual.svg")