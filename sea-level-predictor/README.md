# Sea Level Predictor

This project analyzes a dataset (epa-sea-level.csv) of global average sea level changes since 1880 and uses linear regression to predict the sea level rise by 2050.

## Project Overview

The goal of this project is to predict future sea level rise based on historical data. The dataset provided contains sea level changes adjusted by the CSIRO (Commonwealth Scientific and Industrial Research Organisation). Using this data, a scatter plot is created, followed by linear regression models to predict future sea levels.

## Technologies Used

- **Pandas**: Used for importing and handling the dataset.
- **Matplotlib**: Used for creating scatter plots and plotting the line of best fit.
- **SciPy**: The `linregress` function was used to calculate the slope and y-intercept of the line of best fit.
- **Google Colab**: Data exploration, manipulation, and visualization codes.

## Results
- Scatter plot showing historical sea level data.
- **Line of Best Fit (1880 - present)**: Predicts the sea level rise until 2050 based on the entire dataset.
- **Line of Best Fit (2000 - present)**: Predicts the sea level rise until 2050 based on data from the year 2000 onward, assuming the current rate of sea level rise continues.

## Requirements

``` bash
!pip install pandas matplotlib scipy
```
## Conclusion

This project demonstrates the use of data visualization and linear regression to predict sea level rise based on historical data. The model provides insights into the potential future rise in sea level and can be adapted for similar predictive analyses using other datasets.

## Acknowledgments
Dataset: The dataset used in this project is sourced from freeCodeCamp for educational purposes.


