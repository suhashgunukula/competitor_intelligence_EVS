from flask import Flask, render_template, request, url_for, make_response
import subprocess
import pandas as pd
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def run_competitor_list():
    user_input = request.form['input']
    if user_input == "Avira":
        subprocess.run(["python", "Avira_File.py"], shell=True)
        # Accessing subprocess lists or dataframe from other file
        #from Avira_File import current_price, title, ac_renewal_price, devices, years, discount, Location, website
        from Avira_File import data
        '''
        dist_1 = pd.DataFrame()
        dist_1['S.no'] = list(range(0, len(current_price)))
        dist_1['date'] = date.today().strftime("%d/%m/%Y")
        dist_1['Date'] = int(date.today().strftime("%d"))
        dist_1['Month'] = int(date.today().strftime("%m"))
        dist_1['Year'] = int(date.today().strftime("%y"))
        dist_1['title'] = pd.Series(title)
        dist_1['current_price'] = pd.Series(current_price)
        # to replace the unneccesary values in the column of a dataframe
        dist_1['current_price'] = dist_1['current_price'].str.replace("*", "")
        # to replace the unneccesary values in the column of a dataframe
        dist_1['current_price'] = dist_1['current_price'].str.replace("\u200b", "")

        dist_1['Actual_price/Renewal'] = pd.Series(ac_renewal_price)
        # dist_1['years']=pd.Series(years)
        # dist_1['discount']=pd.Series(discount)
        dist_1['Devices'] = pd.Series(devices)
        #for q in range(0, len(dist_1['current_price'])):
           # dist_1['Devices'][q] = str(devices[q]) + " / " + str(years[q])

        dist_1['Location'] = pd.Series(Location)
        dist_1['website'] = pd.Series(website)
        dist_1['Description'] = ""
        # Convert DataFrame to CSV file and provide a download link
        '''
        csv = data.to_csv(index=False)
        response = make_response(csv)
        response.headers.set('Content-Disposition', 'attachment', filename='competitor_list.csv')
        response.headers.set('Content-Type', 'text/csv')
        return response
    elif user_input == "McAfee":
        with subprocess.Popen(["python", "McAfee_file.py"], stdout=subprocess.PIPE, bufsize=1, universal_newlines=True,
                              shell=True) as p:
            output = ''.join([line for line in p.stdout])
    elif user_input == "Bitdefender":
        with subprocess.Popen(["python", "Bitdefender_file.py"], stdout=subprocess.PIPE, bufsize=1, universal_newlines=True,
                              shell=True) as p:
            output = ''.join([line for line in p.stdout])
    else:
        output = "Invalid input!"

    return render_template('index.html', message="The competitor list has been run successfully.")

if __name__ == '__main__':
    app.run(debug=True)


