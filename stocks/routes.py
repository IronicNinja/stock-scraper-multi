from flask import render_template, url_for, jsonify, flash, redirect, request, send_file, send_from_directory, session
from stocks import app
from stocks.forms import InputForm
import os
from stocks.yahoo import get_stocks
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
            DNE_list, before_list = get_stocks(stock_data, first_date, last_date, session.get('p_id'))
            if DNE_list == "Error":
                flash('Your start date was after the end date. Please try again.', 'danger')
            elif not DNE_list and not before_list:
                flash('All stocks were downloaded! Click Download All to download your stocks.', 'success')
            elif DNE_list and not before_list:
                s = ', '.join(DNE_list)
                flash('The following stocks were undownloadable: %s' % s, 'danger')
            elif not DNE_list and before_list:
                s = ', '.join(before_list)
                flash("Your start date was before these companies' IPOs: %s. They are still downloaded but beware of length mismatches." % s, 'danger')
            else:
                s1 = ', '.join(DNE_list)
                s2 = ', '.join(before_list)
                flash("The following stocks were undownloadable: %s; Your start date was before these companies' IPOs: %s. They are still downloaded but beware of length mismatches" % (s1, s2), 'danger')
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