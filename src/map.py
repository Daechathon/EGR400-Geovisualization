"""File that generates a chloropleth map based on the data sets provided """
import pandas as pd
import folium as f
import os


def generate_map():
    """Function that takes in data sets of various file formats to generate a chloropleth map and plot the given data"""

    # joining paths to begin loading dataframe and datasets
    state_geo = os.path.join('/Users/jacob/PycharmProjects/geovisualization/data/us_states.json')

    state_unemployment = os.path.join(
        '/Users/jacob/Desktop/Spring 2020/Full-Stack Development in '
        'Python/Geovisualization/datasets/US_Unemployment_Oct2012.csv')

    # load csv file for unemployment data
    state_data = pd.read_csv(state_unemployment)

    # initialize map with beginning coordinates and starting position
    m = f.Map(location=[37, -102], zoom_start=5)

    # initialize all the parameters of the chloropleth map
    m.choropleth(
        geo_data=state_geo,
        name='choropleth',
        data=state_data,
        columns=['State', 'Unemployment'],
        key_on='feature.id',
        fill_color='YlGn',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Unemployment Rate (%)'
    )
    # folium handles layer controlling
    f.LayerControl().add_to(m)

    # Save to html
    m.save('folium_chloropleth_USA1.html')
