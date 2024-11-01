# Data Generation and Visualization

This repository contains Python scripts for generating and visualizing data using Matplotlib and Pygal. The scripts cover a variety of topics including mathematical functions, random walks, and dice simulations.

## Visualizations

The visualizations produced by these scripts are designed to be responsive. For example, the Pygal library generates SVG outputs that can scale beautifully from smartwatch to larger displays.


### 1. Scatter Plots

- **Square Values Scatter Plot**: Visualizes the square of values in a specified range using a colormap.
- **Cubes Values Scatter Plot**: Visualizes the cube of values in a specified range with a colormap.

### 2. Random Walks

- **Brownian Motion Simulation**: Implements a random walk to simulate Brownian motion. This script imports the `RandomWalk` class from the `random_walk` module.
- **General Random Walk**: A more generic random walk visualization with colormap integration. This also requires importing the `RandomWalk` class.

### 3. Dice Simulations

- **Simultaneous D6 and D10 Rolls**: Simulates rolling a six-sided die (D6) and a ten-sided die (D10) at the same time. The script visualizes the probability of occurrence for each number.
- **Rolling a D6 Three Times**: Simulates rolling a six-sided die three times and visualizes the results.

## Usage 

Each script can be executed independently. Make sure to have the necessary libraries installed, and import the RandomWalk class in scripts that require it.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or additional features!


## Requirements

To run these scripts, you will need:

- Python 3.x
- Matplotlib
- Pygal

You can install the required libraries using pip:

```bash
pip install matplotlib pygal

