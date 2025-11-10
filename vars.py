import os

API_ID    = os.environ.get("API_ID", "22114233")
API_HASH  = os.environ.get("API_HASH", "d7abcec5c967414fadb1d438fa05ebea")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8178281406:AAHQ56s8EcnYnE8Yda0CmETT-Mo48OKADlQ") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8870))  # Default to 8000 if not set
