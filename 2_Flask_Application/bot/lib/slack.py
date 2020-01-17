import requests, json

WEBHOOK_URL = "https://hooks.slack.com/services/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"

def send_slack(msg):
    data = {"channel": "#webhook","emoji": ":angry:","msg": msg,"username": "Chiru"}
    payload = {"channel": data["channel"],"username": data["username"],"icon_emoji": data["emoji"],"text": data["msg"]}
    response = requests.post(WEBHOOK_URL, data = json.dumps(payload))
