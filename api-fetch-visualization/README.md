# GitHub Star Tracker and Hacker News Discussion Visualizer

## Overview

This project consists of two Python scripts that fetch data from GitHub and Hacker News. The first script retrieves the most starred projects on GitHub, while the second script fetches the most active discussions on Hacker News. The data is visualized using Pygal.

## Features

- Fetches the most starred repositories from GitHub.
- Retrieves the most active discussions from Hacker News.
- Visualizes the data using Pygal with clickable links to each repository and discussion.

## API Endpoints Used

- GitHub API: 'https://api.github.com/search/repositories?q=language:python&sort=stars'
- Hacker News API: 'https://hacker-news.firebaseio.com/v0/topstories.json'

## Requirements

To run these scripts, you will need:

- Python 3.x
- Requests library for making API calls
- Pygal for data vsualization


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

You can install the required libraries using pip:

```bash
pip install requests pygal
