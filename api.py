import flask
import os
from werkzeug.utils import secure_filename
import map as m
from flask import app, request, render_template, flash, redirect, url_for
import pathlib as pb
import pandas as pd

MAP_FOLDER = './data/GeoJSON'
DATA_FOLDER = './data/Datasets'
ALLOWED_EXTENSIONS = {'csv', 'json'}

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'I have a dream'
app.config['GeoJSON'] = MAP_FOLDER
app.config['Datasets'] = DATA_FOLDER


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/v1/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file par
        form = request.form
        if 'mapfile' not in request.files:
            flash('No file part')
            return redirect(request.url)

        map_file = request.files['mapfile']
        data_file = request.files['datafile']
        map_name = request.form.get('mapname')
        legend_name = request.form.get('legendname')
        color = request.form.get('color')

        # if user does not select file, browser also
        # submit an empty part without filename
        if map_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if map_file and allowed_file(map_file.filename):
            file_suffix = pb.Path(map_file.filename).suffix
            map_file_name = secure_filename(map_name + 'MAP' + file_suffix)
            map_file.save(os.path.join(app.config['GeoJSON'], map_file_name))

        if data_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if data_file and allowed_file(data_file.filename):
            file_suffix = pb.Path(data_file.filename).suffix
            data_file_name = secure_filename(map_name + 'DATASET' + file_suffix)

            data_file.save(os.path.join(app.config['Datasets'], data_file_name))

        if map_name != '' and legend_name != '' and color != '' and allowed_file(
                map_file.filename) and allowed_file(data_file.filename):

            data_path = os.path.join(app.config['Datasets'], data_file_name)
            map_path = os.path.join(app.config['GeoJSON'], map_file_name)

            suffix = pb.Path(data_path).suffix

            if suffix == ".csv":
                col = pd.read_csv(data_path).count(0).keys()
            else:
                col = pd.read_json(data_path).count(0).keys()
            return render_template(m.generate_map(geo_file=map_path, data_file=data_path, color=color,
                                                  col=col.to_list(), html=map_name + '.html', legend=legend_name))

        return redirect(url_for('home'))

app.run()