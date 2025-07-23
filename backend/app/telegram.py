import requests
import os
from dotenv import load_dotenv

load_dotenv()

def send_telegram_notify(user_id: str):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    text = f"User {user_id} requested human chat. Check admin panel."
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(url)