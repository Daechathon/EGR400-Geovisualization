# Geovisualization Documentation
Welcome to the introduction of **Asyncing Ship's Geovisualization program**. This documentation will help you get started with the\
set up process in order to use the program and show you how to implement geovisualization tools so that you can plot maps of different geographic regions and areas.


## Description
This program is designed to allow users to develop interactive chloropleth maps that utilize text files like CSV, JSON, XML, etc in order to plot points and import data sets that will change the visual appearance of the map they are creating. The program enables users to load in two different files: 1. The data file that will generate the map & 2. The data file that is to be plotted. Once these files are uploaded within the construct users can initialize their maps with a starting location, zoom values, as well as parameters that entail what geographic data is going to be used, the name of the map, legends, etc.


## Table of Contents
1. [Getting Started](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#getting-started)
   - [*Prerequistite Installation*](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#prerequisite-installation)
   - [*Coding*](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#coding)
   - ...


## Getting Started
These instructions will show you how to produce a copy of the project while also getting it up and running on your local machine for development and testing purposes. See [**deployment**] for notes on how to deploy the project on a live system.

### Prerequisite Installation
1. Download and Install the latest version of [Anaconda](https://www.anaconda.com/distribution/) with Python\
   or


2. Pip install and run Pandas in Python
   > $ pip install pandas
3. Pip Install [Folium](https://pypi.org/project/folium/)
   > $ pip install folium
   
   or
   
   > $ conda install -c conda-forge folium


### Coding
A step by step series of examples that tell you how to get a Geovisualization program running
> pip install [example]

and then
> [another example]

### Example Code: Import
To begin writing your file...
```
# code block
import pandas as pd
import folium as f
import os
```
### Example Code: Map Generation
This function takes in data sets of various file formats to generate a chloropleth map and plot the given data
```
# code block
def generate_map():
    
    # joining paths to begin loading dataframe and datasets
    state_geo = os.path.join('/Users/jacob/PycharmProjects/geovisualization/data/us_states.json')

    state_unemployment = os.path.join(
        '/Users/jacob/Desktop/Spring 2020/Full-Stack Development in '
        'Python/Geovisualization/datasets/US_Unemployment_Oct2012.csv')
```
