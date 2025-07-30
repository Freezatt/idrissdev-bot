from flask import Flask, render_template_string, request  
import requests  
import random  
  
app = Flask(__name__)  
account = {"login": None, "domain": None}  
  
HTML = '''  
<!doctype html>  
<html lang="ar">  
<head>  
  <meta charset="UTF-8">  
  <title>📧 بريد إدريس المؤقت</title>  
  <style>  
    body {  
      background: linear-gradient(130deg, #0d1117 0%, #1f1f1f 100%);  
      color: #c9d1d9;  
      font-family: sans-serif;  
      text-align: center;  
      padding: 40px;  
}  
.email-box {  
      background: #1e1e2e;  
      padding: 15px;  
      border-radius: 12px;  
      font-size: 20px;  
      margin-bottom: 20px;  
      display: inline-block;  
      box-shadow: 0 0 10px #58a6ff;  
}  
    button {  
      padding: 10px 20px;  
      background: #21262d;  
      color: #58a6ff;  
      border: none;  
      border-radius: 12px;  
      cursor: pointer;  
      margin: 5px;  
}  
.message {  
      background: #2c313a;  
      margin: 10px auto;  
      padding: 12px;  
      border-radius: 10px;  
      max-width: 500px;  
}  
.footer {  
      margin-top: 30px;  
      font-size: 13px;  
      color: #999;  
}  
  </style>  
</head>  
<body>  
  <h2>📮 بريدك المؤقت:</h2>  
  <div class="email-box"><b>{{ email}}</b></div>  
  <form method="post">  
      <button name="action" value="refresh_email">🔁 بريد جديد</button>  
      <button name="action" value="refresh_messages">📨 تحديث الرسائل</button>  
  </form>  
  <h3>📬 الرسائل:</h3>  
  {% if messages %}  
    {% for msg in messages %}  
      <div class="message"><b>{{ msg['from']}}</b> - {{ msg['subject']}}</div>  
    {% endfor %}  
  {% else %}  
    <p>لا توجد رسائل بعد.</p>  
  {% endif %}  
  <div class="footer">صُنع بحب ❤️ من طرف إدريس</div>  
</body>  
</html>  
'''  
  
def generate_email():  
    login = f"idris{random.randint(1000,9999)}"  
    domain = random.choice(["1secmail.com", "1secmail.net", "1secmail.org"])  
    return {"login": login, "domain": domain}  
  
def get_messages(login, domain):  
    try:  
        url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"  
        return requests.get(url).json()  
    except:  
        return []  
  
@app.route("/", methods=["GET", "POST"])  
def index():  
    global account  
    if request.method == "POST":  
        action = request.form.get("action")  
        if action == "refresh_email" or account["login"] is None:  
            account = generate_email()  
  
    messages = get_messages(account["login"], account["domain"])  
    email = f"{account['login']}@{account['domain']}"  
    return render_template_string(HTML, email=email, messages=messages)  
  
app.run(host="0.0.0.0", port=3000)