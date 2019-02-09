from flask import render_template, request, jsonify, abort

from carbon import app
from carbon.forms import MainForm
from carbon.utils import AVAILABLE_LANGS, convert

import json

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MainForm()
    if form.validate_on_submit():
        converted_data = convert(form.content.data, request.form.get('lang'))
        return render_template('home.html', result=converted_data, title='THT code highlighter', form=form, langs = AVAILABLE_LANGS)
    return render_template('home.html', title='THT code highlighter', form=form, langs = AVAILABLE_LANGS)

@app.route('/api', methods=['POST'])
def api():
    if not request.form:
        abort(400)
    else:
        data = json.loads(next(request.form.keys()))
        converted_data = convert(data.get('data'), data.get('lang'))
        return jsonify({'converted': converted_data})
