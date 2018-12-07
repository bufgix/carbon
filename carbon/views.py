from flask import render_template, request

from carbon import app
from carbon.forms import MainForm
from carbon.utils import AVAILABLE_LANGS, convert

@app.route('/', methods=['GET', 'POST'])
def home():
    form = MainForm()
    if form.validate_on_submit():
        converted_data = convert(form.content.data, request.form.get('lang'))
        return render_template('home.html', result=converted_data, title='THT code highlighter', form=form, langs = AVAILABLE_LANGS)
    return render_template('home.html', title='THT code highlighter', form=form, langs = AVAILABLE_LANGS)
