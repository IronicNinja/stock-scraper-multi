from flask import render_template, url_for, jsonify, flash, redirect, request, send_file, send_from_directory, session
from stocks import app
from stocks.forms import InputForm
import os
from stocks.yahoo import get_stocks
from werkzeug.utils import secure_filename
import random

# pylint: skip-file

@app.route("/", methods=['GET', 'POST'])
def home():
    form = InputForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            session['p_id'] = random.randint(1, 1000000)
            stock_data = form.stocks.data
            first_date = form.date_start.data
            last_date = form.date_end.data
            DNE_list = get_stocks(stock_data, first_date, last_date, session.get('p_id'))
            if not DNE_list:
                flash('All stocks were downloaded! Click Download All to download your stocks.', 'success')
            else:
                s = ', '.join(DNE_list)
                flash('The following stocks were undownloadable: %s' % s, 'danger')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful, please try again.', 'danger')
            return redirect(url_for('home'))
    return render_template('home.html', title='Home', form=form)

@app.route("/downloading", methods=['GET', 'POST'])
def downloading():
    return send_from_directory('../', filename='sampleDir%s.zip' % session.get('p_id'),
                    attachment_filename='stocks.zip',
                    as_attachment=True, cache_timeout=-1)