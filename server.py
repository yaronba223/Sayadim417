from flask import Flask, request
import requests

app = Flask(_name_)

# כאן תכניס את הטוקן שקיבלת מ-BotFather
TELEGRAM_TOKEN = "8273469629:AAHE5xlBafWCOHxekUQUa6OxSah6fmfCQvI"

# כאן תכניס את ה-CHAT ID שלך (אפשר להשיג דרך https://api.telegram.org/bot<TOKEN>/getUpdates)
CHAT_ID = "1852389105"

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' in request.files:
        file = request.files['file']

        # שליחת התמונה לטלגרם
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
        response = requests.post(url, data={"chat_id": CHAT_ID}, files={"photo": file})
        return f"Image sent to Telegram. Response: {response.text}", 200
    else:
        return "No file received", 400

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=8080)