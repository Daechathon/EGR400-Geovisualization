import app.map as m


# provide absolute paths for GeoJSON and dataset from local machine
json_path = '/Users/jacob/PycharmProjects/geovisualization/data/GeoJSON/us_states.json'
dataset1_path = '/Users/jacob/PycharmProjects/geovisualization/data/Datasets/us_death_rates.csv'
dataset2_path = '/Users/jacob/PycharmProjects/geovisualization/data/Datasets/covid-19_cases.json'


# 'BuGn', 'BuPu', 'GnBu', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'RdPu', 'YlGn', 'YlGnBu', 'YlOrBr', and 'YlOrRd'

if __name__ == "__main__":
    m.generate_map(geo_file=json_path, data_file=dataset1_path, col=['State', 'Deaths'], color='GnBu',
                   legend='Total Count (min - max)', html='US Death Rates.html')

    m.generate_map(geo_file=json_path, data_file=dataset2_path, col=['State', 'Cases'], color='PuRd',
                   legend='Total Count (min - max)', html='US_Covid-19.html')

