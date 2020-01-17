from flask import Flask, request, Response

from lib.slack import send_slack
from lib.forecast import forecast

app = Flask(__name__)

# slack outgoing webhook
@app.route("/slack", methods=['POST'])
def slack():
    username = request.form.get('user_name')
    token = request.form.get('token')
    text = request.form.get('text')

    if "weather" in text:
        summary = forecast()
        send_slack(summary)
        
    if "Weather" in text:
        summary = forecast()
        send_slack(summary)
        
    if "Danny" in text:
        send_slack("He is awesome")
        
    if "danny" in text:
        send_slack("He is awesome")
        
    if "chiru" in text:
        send_slack("Me? My biggest attraction is snoring. Haha~")
    
    if "Chiru" in text:
        send_slack("Me? My biggest attraction is snoring. Haha~")

    print(username, token, text)

    return Response(), 200

if __name__ == "__main__":
    app.run()
