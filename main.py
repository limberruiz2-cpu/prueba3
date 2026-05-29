import requests

BOT_TOKEN = "8878074016:AAE4VaVQ2D-XzXm3uWU90trey85rt7rEhUU"
CHAT_ID = "5855497862"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

r = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "Prueba desde Python"
    }
)

print(r.text)