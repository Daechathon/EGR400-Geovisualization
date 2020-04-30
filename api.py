import flask
import os
from werkzeug.utils import secure_filename
import map as m
from flask import app, request, render_template, flash, redirect, url_for

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
    return '''<h1>Home</h1>'''


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

        dataset1 = request.files['file']
        dataset2 = request.files['file2']
        # if user does not select file, browser also
        # submit an empty part without filename
        if dataset1.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if dataset1 and allowed_file(dataset1.filename):
            filename = secure_filename(dataset1.filename)
            dataset1.save(os.path.join(app.config['GeoJSON'], filename))

        if dataset2.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if dataset2 and allowed_file(dataset2.filename):
            filename = secure_filename(dataset2.filename)
            dataset2.save(os.path.join(app.config['Datasets'], filename))

        if dataset1.filename == '' and dataset1 and allowed_file(
                dataset1.filename) and dataset2.filename == '' and dataset2 and allowed_file(dataset2.filename):
            filename = secure_filename(dataset2.filename)
            return redirect(url_for('upload_file',
                                    filename=filename))

    return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
          <input type=file name=file>
          <input type=file name=file2>
          <input type=submit value=Upload>
        </form>
        '''


# We have uploaded the files, now we need to plug those files in to generate the maps.......

# TODO: Figure out how to read the files when they are passed in from the user so that the maps can be generated
#  dynamically and with invariant results

@app.route('/api/v1/map', methods=['GET', 'POST'])
def generate_map():
    json_path = 'data/GeoJSON/us_states.json'
    dataset1_path = 'data/Datasets/covid-19_cases.csv'

    m.generate_map(geo_file=json_path, data_file=dataset1_path, col=['State', 'Cases'], color='GnBu',
                   legend='Total Count (min - max)', html='US-COVID-19.html')
    # set path for html file to be in templates folder

    return render_template("US-COVID-19.html")


app.run()
