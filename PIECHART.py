# -*- coding: utf-8 -*-
"""
Created on Sun Nov 5 09:17:18 2023
@author: Revathi Nanubala
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Define the URL for the dataset
url = 'https://drive.google.com/file/d/12akRDB02Ph5vAbcKSlJySZqGHl0OdZGM/view?usp=sharing'

# Read the dataset from the given URL
data = pd.read_csv("https://drive.google.com/uc?export=download&id="+url.split('/')[-2])

# Dropping unnecessary columns
data = data.drop(columns=['Image URL'])

# Extract the country data and medal data
country_data = data["Country Name"]
medal_data = data['2000']

# Display the medal data and the first five rows of the dataset
print(medal_data)
print(data.head())

# Define the explode values for the pie chart
explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0.1)

# Create a figure for the pie chart
plt.figure(figsize=(30, 15))

# Define an array of different RGB values for the pie chart colors
colors = [
    (255, 0, 0),     # Red
    (0, 128, 0),     # Green
    (0, 0, 255),     # Blue
    (255, 165, 0),   # Orange
    (128, 0, 128),   # Purple
    (255, 192, 203), # Pink
    (0, 255, 0),     # Lime
    (0, 255, 255),   # Cyan
    (255, 255, 0),   # Yellow
    (0, 0, 128),     # Navy
    (255, 0, 255),   # Magenta
    (192, 192, 192), # Silver
    (128, 128, 128), # Gray
    (128, 0, 0),     # Maroon
    (128, 128, 0),   # Olive
    (0, 128, 128),   # Teal
    (128, 0, 64),    # Burgundy
    (255, 165, 0),   # Coral
    (0, 128, 128),   # Aquamarine
]

# Convert RGB values to normalized floats between 0 and 1
colors = [(r / 255, g / 255, b / 255) for r, g, b in colors]

# Create the pie chart
plt.pie(medal_data, 
        labels=country_data, 
        explode=explode, 
        colors=colors, 
        autopct='%1.1f%%', 
        shadow=True, 
        startangle=180,
        wedgeprops={
            "edgecolor": "white",
            'linewidth': 1,
            'antialiased': True
        })

# Set the title for the pie chart
plt.title('Medal Achievements for different countries in the year 2000')

# Display the pie chart
plt.show()
