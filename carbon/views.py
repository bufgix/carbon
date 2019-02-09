from flask import render_template, request, jsonify, abort
from flask_cors import cross_origin

from carbon import app
from carbon.forms import MainForm
from carbon.utils import AVAILABLE_LANGS, convert

from pygments.util import ClassNotFound
import json

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MainForm()
    if form.validate_on_submit():
        converted_data = convert(form.content.data, request.form.get('lang'))
        return render_template('home.html', result=converted_data, title='THT code highlighter', form=form, langs = AVAILABLE_LANGS)
    return render_template('home.html', title='THT code highlighter', form=form, langs = AVAILABLE_LANGS)

@app.route('/api', methods=['POST'])
@cross_origin()
def api():
    if not request.form:
        abort(400)
    else:
        try:
            converted_data = convert(request.form.get('data'), request.form.get('lang'))
        except ClassNotFound as err:
            return jsonify({'converted': "Dil Bulunamadı"})
        
        return jsonify({'converted': converted_data})
