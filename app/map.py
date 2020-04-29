import pandas as pd
import folium as f
import os
import pathlib


def generate_map(geo_file, data_file, col, color, legend, html):
    geo_path = os.path.join(geo_file)
    data_path = os.path.join(data_file)

    ext = pathlib.Path(data_path).suffix
    if ext == ".csv":
        data_read = pd.read_csv(data_path)
    elif ext == ".json":
        data_read = pd.read_json(data_path)

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

    # Save to html
    m.save(html)
# 2. Set up loading the dataset
# 3. Have user enter the files they want
# 4. Generate Map with values
