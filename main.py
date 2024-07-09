import requests
from send_mail import send_email

api_key = "2da943153efe4d27aac099f5403d1417"

topic = "telsa"

url = (f"https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&apiKey="
       "890603a55bfa47048e4490069ebee18c&"
       "language=en")

request = requests.get(url)

content = request.json()

message = "Subject:Today's news" + "\n"

for article in content["articles"][:20]:
    try:
        message = ( message + article["title"] + "\n" +
                   article["description"] + "\n" +
                   article["url"] + 2*"\n")
    except TypeError:
        continue


message = message.encode("utf-8")
send_email(message)
