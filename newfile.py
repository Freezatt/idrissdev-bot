import requests

URL = "https://رابط_موقعك.replit.dev/"

try:
    response = requests.get(URL)
    print("✅ الموقع تم زيارته بنجاح!")
except Exception as e:
    print(f"❌ فشل في الاتصال: {e}")
