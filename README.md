```diff
+ April 30: Released v1.0.0 with
+   functionality for image geovisualization, data plotting   
```

# Geovisualization Documentation
Welcome to the introduction guide to **Asyncing Ship's Geovisualization program**. This documentation will help you get started with the set up process in order to use the program and show you how to implement geovisualization tools so that you can plot maps of different geographic regions and areas.


## Description
This program was designed to allow users to develop interactive chloropleth maps that utilize text files like CSV, JSON, XML, etc in order to plot points and import data sets that will change the visual appearance of the map they are creating. The program enables users to load in two different files: 1. The data file that will generate the map's location & 2. The data file that holds the data that is to be plotted. Once these files are uploaded within the construct users can initialize their maps with a starting location, zoom values, as well as parameters that entail what geographic data is going to be used, the name of the map, legends, etc.


## Table of Contents
1. [Getting Started](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#getting-started)
   - [*Prerequistite Installation*](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#prerequisite-installation)
   - [*Coding*](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#coding)
2. [Input/Output Verification](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#inputoutput-verification)
   - [*Examples*](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#examples)
   - [*Build Status*](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#build-status)
3. [UI Support](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#ui-support)
4. [Contributors](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#contributors)


## Getting Started
These instructions will show you how to produce a copy of the project while also getting it up and running on your local machine for development and testing purposes.

### System Requirements 

__Requirements__

* A machine running Linux or Windows
* Anaconda with Python version >= 3.8.2

### Prerequisite Installation
1. Download and Install the latest version of [Anaconda](https://www.anaconda.com/distribution/) with Python >= 3.8.2

   or

   Pip install and run Pandas in Python
```
   $ pip install pandas
```
2. Pip Install [Folium](https://pypi.org/project/folium/)
> NOTE:
```
   $ pip install folium
```   
   or
```   
   $ conda install -c conda-forge folium
```
> NOTE: For Windows users it is suggested that you use Anaconda

> NOTE: For non-Windows you can easily install a python package manager, like pip, through Homebrew or use the apt-get command if you are using Linux

### Coding

__Coding Your Project__

A step by step series of examples that tell you how to get a Geovisualization program running

1. Upload your map using a GeoJSON format

```
# provide absolute paths for GeoJSON from local machine
json_path = '/Users/jacob/PycharmProjects/geovisualization/data/GeoJSON/us_states.json'
```
2. Upload the datasets you want to map from various file types

```
# provide absolute paths for dataset from local machine
dataset1_path = '/Users/jacob/PycharmProjects/geovisualization/data/Datasets/us_death_rates.csv'
dataset2_path = '/Users/jacob/PycharmProjects/geovisualization/data/Datasets/covid-19_cases.json'
```
> NOTE: The application currently takes in .csv and .json files
> NOTE: Only takes two columns or keys with data

3. Upon running the application it will then generate your desired map with plotted data for spatial vectors and statistical data
**See "Example Code 'Map Generation' "**
> NOTE: Generates an html which displays the user's map of choice

4. Map is saved to HTML
> NOTE: Could also generate in browser with localhost

__Example Code: Files to Import__

To begin writing your file first import Pandas and Folium

```
# code block
import pandas as pd
import folium as f
import os
import pathlib
```
__Example Code: Map Generation__


This function takes in the data sets of various file formats (in this case .CSV & .JSON) to generate a chloropleth map and plot the given data
```
# code block
def generate_map(geo_file, data_file, col, color, legend, html):
    geo_path = os.path.join(geo_file)
    data_path = os.path.join(data_file)
```
> NOTE: "geo_file" & "data_file" are the spaces where your .csv and .json files are placed

This reads in the file type 
```
# code block
    ext = pathlib.Path(data_path).suffix
    if ext == ".csv":
        data_read = pd.read_csv(data_path)
    elif ext == ".json":
        data_read = pd.read_json(data_path)
```

Here lies the visual aspect of you generate map, which gives it showcases you data through color and layout plotting
```
# code block
    m = f.Map(location=[37, -102], zoom_start=5)

    # Add the color for the chloropleth:
    m.choropleth(
        geo_data=geo_path,
        name='choropleth',
        data=data_read,
        columns=col,
        key_on='feature.id',
        fill_color=color,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=legend
    )
    f.LayerControl().add_to(m)
```

## Input/Output Verification

### Examples
<p align="center">
  <img src="" height="350"/>
</p>

### Build Status

__Testing__



## UI Support



## Contributors
* Brandon-*Testing/Deployment*
* Cameron-*Design*
* Chase-*Deployment/Development*
* Jacob-*Deployment/Development*
* Micah-*Documentation*
