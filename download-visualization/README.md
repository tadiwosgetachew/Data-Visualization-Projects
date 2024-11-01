# Download and Visualize Project

This project contains Python scripts that download and visualize differrent datasets, including world population data and weather data. The visualizations are created using Pygal and Matplotlib.

## Project Overview

This project aims to provide insights into world demographics and weather patterns. It includes:

- Visualization of world population data for the year 2010 using an interactive map.
- Visualization of weather data for Death Valley, CA, and Sitka, AL, for the year 2014.

### Features

- Uses world population data downloaded in JSON format.
- Plots an interactive world population map that is an SVG, color-coded based on population density, and scales beautifully from smartwatches to large screens. The `get_country_code` class from the `country_code` module is used to handle country codes.
- Handles CSV data for weather without using additional libraries like pandas.

## Requirements

To run these scripts, you will need:

- Python 3.x
- Matplotlib
- Pygal
- CSV module (built-in)

## Usage 

### World population Visulization

- Download the world population data in JSON format(also provided) & use the script to visualize the data for the year 2010. 

### Weather data visualization 

- Ensure you have the CSV files for Death Valley and Sitka (also provided) and use the scripts to visualize the data for the year 2014. 

## Contributing 

Contributions are welcome! If you have suggestions for improvements or additional features, feel free to fork the repository and submit a pull request.

You can install the required libraries using pip:

```bash
pip install matplotlib pygal