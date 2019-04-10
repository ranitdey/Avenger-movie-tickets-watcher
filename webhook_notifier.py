import requests

def notify_webook(webhook_url, message):
    payload = "{\n\t \"message\" : \""+message+"\"\n}"
    response = requests.request("POST", webhook_url, data=payload)