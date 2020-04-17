# Python program to plot  
# geographical data using plotly 

# importing all necessary libraries 
import plotly.matplotlylib as py
import plotly.graph_objs as go
import pandas as pd

# some more libraries to plot graph 
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot, plot

# # To establish connection
# init_notebook_mode(connected=True)
#
# # type defined is choropleth to
# # plot geographical plots
# data = dict(type='choropleth',
#
#             # location: Arizoana, California, Newyork
#             locations=['AZ', 'CA', 'NY'],
#
#             # States of USA
#             locationmode='USA-states',
#
#             # colorscale can be added as per requirement
#             colorscale='Portland',
#
#             # text can be given anything you like
#
#             text=['infected', 'infected', 'infected'],
#             infected_num=[1.0, 2.0, 3.0],
#             colorbar={'title': 'Degree of Infected'})
#
# layout = dict(geo={'scope': 'usa'})
#
# # passing data dictionary as a list
# choromap = go.Figure(data=[data], layout=layout)
#
# # plotting graph
# plot(choromap)
#





###################################################################################### Using leaflet

# import folium
#
# m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
#
#
# #Create Markers
#
# tooltip = 'Click here for more info'
#
# folium.Marker([42.363600, - 71.099500],
#               popup='<strong>Location One</strong>',
#               tooltip=tooltip).add_to(m),
# folium.Marker([42.333600, -71.109500],
#               popup='<strong>Location One</strong>',
#               tooltip=tooltip.__add__('m'),
#               icon=folium.Icon(icon='cloud').add_to(m))
# m.save('map.html')








#########################################################################################
import pandas as pd
import folium as f
import os # use better module: path

state_geo = os.path.join('/Users/jacob/Desktop/Spring 2020/Full-Stack Development in Python/Geovisualization/datasets'
                         , 'us_states.json')

state_unemployment = os.path.join('/Users/jacob/Desktop/Spring 2020/Full-Stack Development in Python/Geovisualization/'
                                  'datasets',
                                  'us-counties.csv')

state_data = pd.read_csv(state_unemployment)

m = f.Map(location=[37, -102], zoom_start=5)

# Add the color for the chloropleth:
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
f.LayerControl().add_to(m)

# Save to html
m.save('#292_folium_chloropleth_USA1.html')





