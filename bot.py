from flask import Flask, request
import requests
import os
import logging

TOKEN = '7412819431:AAG65XHpyBq4G8dy0KNrdNHFAVtn53EiW-Y'
WEB_APP_URL = 'https://t.me/facecheckV1_bot/faceCheckID'  # Replace with your actual web app URL

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        update = request.get_json()
        app.logger.info('Received update: %s', update)
        handle_update(update)
        return 'OK'

def handle_update(update):
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        message_text = update['message']['text']
        if message_text == '/start':
            welcome_message = (
                "Welcome to FaceSearchID Bot!\n\n"
                "FaceSearchID allows you to search for faces.\n"
                "Click the link below to access the web app:\n"
                f"{WEB_APP_URL} \n"
                "Use the Launch menu button to start\n"
            )
            send_message(chat_id, welcome_message)
        else:
            send_message(chat_id, "I'm sorry, I didn't understand that command.")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    response = requests.post(url, json=payload)
    app.logger.info('Sent message response: %s', response.json())

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
