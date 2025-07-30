import requests

URL = "https://1b5a6a61-5ca8-48cc-b9e0-fe2887f73697-00-16k0sfg61afq7.janeway.replit.dev/"

try:
    response = requests.get(URL)
    print("✅ الموقع تم زيارته بنجاح!")
except Exception as e:
    print(f"❌ فشل في الاتصال: {e}")
