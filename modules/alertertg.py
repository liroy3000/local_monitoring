#!/usr/bin/env python3

def alerter(tg, message):
    import requests

    format_message = ""
    for i in message:
        format_message = format_message + i + ": " + message[i] + "\n"

    url = 'https://api.telegram.org/bot' + tg["token"] + '/sendMessage'
    params = {'chat_id': tg["chat_id"], 'text': format_message}
    requests.post(url, data=params)
