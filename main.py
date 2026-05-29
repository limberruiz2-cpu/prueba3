from binance.client import Client
import requests
import time

# Binance
API_KEY = "vcAvfzfIGHbBFI0RBIy6IRFoE7nXmV2Wb9TZT4D3FY7VMRjVt9TzSG0fDh5Zz8jS"
API_SECRET = "hEJzqGsu90aKlHwRI4L78uzBTZPDK48ceLBEanu65NUBocXlAPzPEwHVPKx6s09v"

# Telegram
BOT_TOKEN = "8878074016:AAE4VaVQ2D-XzXm3uWU90trey85rt7rEhUU"
CHAT_ID = "5855497862"


client = Client(API_KEY, API_SECRET)
server_time = client.get_server_time()['serverTime']
local_time = int(time.time() * 1000)

client.timestamp_offset = server_time - local_time

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensaje
    })

try:
    cuenta = client.get_account()

    mensaje = "📊 Balance Binance\n\n"

    for activo in cuenta['balances']:
        libre = float(activo['free'])
        bloqueado = float(activo['locked'])

        total = libre + bloqueado

        if total > 0:
            mensaje += f"{activo['asset']}: {total}\n"

    enviar_telegram(mensaje)

    print("Mensaje enviado")

except Exception as e:
    print("Error:", e)
