# Geovisualization-documentation
Welcome to the introduction of **Asyncing Ship's Geovisualization program**. This documentation will help you get started with the\
set up process in order to use the program and show you how to implement geovisualization tools so that you can plot maps of different geographic regions and areas.


## Description
This program is designed to allow users to develop interactive chloropleth maps that utilize text files like CSV, JSOn, XML, etc in order to plot points and import data sets that will change the visual appearance of the map they are creating. The program allows for users to load in two different files: 1. The data file that is going to be use for the map 2. The data file that is to be plotted. 


## Table of Contents
1. Getting Started
   - Prequisites [Link](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#prerequisites)
   - Installation [Link](https://github.com/Daechathon/EGR400-Geovisualization/blob/Documentation/README.md#installing)
   - ...


## Getting Started


### Prerequisites


### Installing
A step by step series of examples that tell you how to get a Geovisualization program running
> pip install [example]

and then
> [another example]

```
# code block
@as_chan
        def thermo(chan, unit):
            while True:
                yield chan.put(convert(thermo_get(), unit))

        @coroutine
        def main():
            thermo_chan = thermo('C')
            while True:
