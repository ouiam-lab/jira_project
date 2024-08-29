import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a route that handles POST requests
@app.route('/createJira', methods=['POST'])
def createJira():
    url = "https://datlassian.net/rest/api/3/issue"
    
    # Replace with your Jira email and API token
    EMAIL = "your_email@example.com"
    API_TOKEN = "your_api_token_here"

    auth = HTTPBasicAuth(EMAIL, API_TOKEN)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "description": {
                "content": [
                    {
                        "content": [
                            {
                                "text": "Order entry fails when selecting supplier.",
                                "type": "text"
                            }
                        ],
                        "type": "paragraph"
                    }
                ],
                "type": "doc",
                "version": 1
            },
            "project": {
                "key": "AB"
            },
            "issuetype": {
                "id": "10007"
            },
            "summary": "Main order flow broken"
        }
    })

    response = requests.post(url, data=payload, headers=headers, auth=auth)

    if response.status_code == 201:
        return jsonify({"message": "Issue created successfully", "issue": response.json()}), 201
    else:
        return jsonify({"message": "Failed to create issue", "error": response.json()}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
