# Stock Scraping Tool

https://stock-scraper-multi.herokuapp.com/

**Instructions for Use**
1. Input a list of stocks (abbreviated form) that you want downloaded, e.g. GOOG, FB, AAPL. You MUST use the correctly spelled abbreviation. The more stocks you have and the larger the time range, the longer it will take for the program to compile the files.

2. Add the start date and end date in the format year-month-date, e.g. 2015-01-13 or 2018-11-02.

3. Click Submit. If you inputted the date in an incorrect format or the start date after the end date, you will get an error message. If you input incorrectly spelled stocks, there will be an error message telling you which stocks were not found. You may still download the zip folder as it will consist of all of the correctly spelled stocks. If everything is inputted correctly, you should receive a confirmation message.

4. Click Download All. This should create a zipped folder called "stocks.zip" which contains all your stocks in csv format!

Please note: If your start date is before a company's initial public offering, you will receive data that starts from the company's IPO. Be careful because this can cause mismatches in the lengths of your csv files. The program should be able to catch if your state date is before the company's IPO; however, in rare circumstances (where your start date is within a week of the IPO), it may not be able to do so. I would suggest checking the length of each csv with a program before using them.
