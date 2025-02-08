# Medical Data Visualizer

This project visualizes and analyzes actual medical examination data using `matplotlib`, `seaborn`, and `pandas`. It focuses on visualizing health outcomes for patients based on factors like cholesterol, glucose levels, alcohol use, physical activity, smoking status, and obesity (as a risk factor for cardiovascular disease).

## Description

The dataset, sourced from freeCodeCamp, includes medical data with features such as cholesterol, glucose levels, alcohol consumption, blood pressure, physical activity, smoking status, and cardiovascular disease (`cardio`). The project involves the following:

- **Data Preprocessing & Visualization**:
  - Filter out irrelevant or missing data.
  - Obesity is judged based on a BMI greater than 25.
  - Visualize counts of good and bad outcomes (categorical plots) for **cholesterol**, **gluc**, **alco**, **active**, **smoke**, and **obesity**, split by `cardio=0` (no cardiovascular disease) and `cardio=1` (with cardiovascular disease).
  - Generate a **correlation matrix** to explore relationships between the features.

## Project Structure

- `medical_examination.csv/`: Dataset used for analysis.
- `Examples`: Test your visualization against these figures.  
- `visualizations/`: Generated figures (charts).
- `notebooks/`: Data processing, analysis, and visualization code.
- `README.md`: Project details.

## Requirements

Install the required libraries with:

```bash
pip install matplotlib seaborn pandas jupyter

```

## Contributions

Contributions are welcome! Please submit a pull request or open an issue to suggest improvements.

## Future Improvements

- **Machine Learning**: Implement machine learning models (e.g., logistic regression, random forests, or gradient boosting) to predict cardiovascular risk based on the available features.
- **User Interface**: Create an interactive web application to allow users to upload their own medical data and receive visualizations or predictions.
- **Obesity Calculation**: Include additional obesity metrics like waist-to-hip ratio or body fat percentage for a more comprehensive analysis.
- **Additional Features**: Expand the dataset with more medical or lifestyle features and explore their impact on cardiovascular disease prediction.

## Acknowledgements

- Dataset provided by **freeCodeCamp**.
- Libraries: **matplotlib**, **seaborn**, **pandas**.


