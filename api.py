import flask
import webbrowser
import os
from werkzeug.utils import secure_filename
import app.map as m
from flask import app, jsonify, request, render_template, flash, redirect, url_for

UPLOAD_FOLDER = './data'
ALLOWED_EXTENSIONS = {'csv', 'json'}

app = flask.Flask(__name__)
app.config['DEBUG'] = True

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Home</h1>'''


@app.route('/api/v1/data1', methods=['GET'])
def dataset1():
    return render_template('')


@app.route('/api/v1/data2', methods=['GET', 'POST'])
def dataset2():
    # Upload the dataset and the map files
    # Put them into their respective folders
    # generate map using new values
    json_path = '/Users/jacob/PycharmProjects/geovisualization/data/GeoJSON/us_states.json'
    dataset1_path = '/Users/jacob/PycharmProjects/geovisualization/data/Datasets/us_death_rates.csv'
    dataset2_path = '/Users/jacob/PycharmProjects/geovisualization/data/Datasets/covid-19_cases.json'

    # 'BuGn', 'BuPu', 'GnBu', 'OrRd', 'PuBu', 'PuBuGn', 'PuRd', 'RdPu', 'YlGn', 'YlGnBu', 'YlOrBr', and 'YlOrRd'

    m.generate_map(geo_file=json_path, data_file=dataset1_path, col=['State', 'Deaths'], color='GnBu',
                   legend='Total Count (min - max)', html='US Death Rates.html')
    # set path for html file to be in templates folder

    m.generate_map(geo_file=json_path, data_file=dataset2_path, col=['State', 'Cases'], color='PuRd',
                   legend='Total Count (min - max)', html='US_Covid-19.html')

    return render_template('US_Covid-19.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/v1/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_file',
                                    filename=filename))

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=Dataset>
          <input type=file name=GeoJSON>
          <input type=submit value=Upload>
        </form>
        '''


app.run()
