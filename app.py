from flask import Flask, jsonify, request, render_template

import requests

app = Flask(__name__)

@app.route('/link', methods=['GET'])
def post_data_and_redirect():
    url = "https://dashboard.paytm.com/api/v1/payment/link"
    headers = {
        "Appversion": "6.6.2",
        "Deviceidentifier": "OnePlus-AC2001-c5f52436f1f6cad1",
        # ...  headers 
    }
    data = {
        "mid": "PKxDhR19072489458238",
        "amount": "500",
        # ...  data 
    }
    
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
    app.run(host="0.0.0.0",debug=True)