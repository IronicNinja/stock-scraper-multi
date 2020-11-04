from flask import render_template, url_for, jsonify, flash, redirect, request, send_file
from stocks import app
from stocks.forms import InputForm
import os
from stocks.yahoo import get_stocks
from zipfile import ZipFile
from os.path import basename

# pylint: skip-file

@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = InputForm()
    if form.validate_on_submit():
        stock_data = form.stocks.data
        first_date = form.date_start.data
        last_date = form.date_end.data
        get_stocks(stock_data, first_date, last_date)
        flash('Successful!', 'success')

        dirName = r"C:\Users\evanz\Desktop\stock_scraper\stocks\downloads"
        with ZipFile('sampleDir.zip', 'w') as zipObj:
        # Iterate over all the files in directory
            for folderName, subfolders, filenames in os.walk(dirName):
                for filename in filenames:
                    #create complete filepath of file in directory
                    filePath = os.path.join(folderName, filename)
                    # Add file to zip
                    zipObj.write(filePath, basename(filePath))
                    os.remove(filename)

        path = r"C:\Users\evanz\Desktop\stock_scraper\sampleDir.zip"
        return send_file(path,
                attachment_filename= 'downloads.zip',
                as_attachment = True, cache_timeout=-1)
    else:
        flash('Unsuccessful please try again', 'danger')
        redirect(url_for('home'))
    return render_template('home.html', title='Home', form=form)