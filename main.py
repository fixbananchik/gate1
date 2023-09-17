import requests
from flask import Flask

app = Flask(__name__)

base_url = "http://numbersapi.com/"

url_random_trivia = "random/trivia"
url_random_math = "random/math"

facts =[]


@app.route("/numbers/<count>")
def main(count):
    count = int(count)
    facts = []
    for a in range(count):
        response = requests.get(base_url + url_random_trivia)
        facts.append(response.text)
    return {"count": count, "facts": facts}

@app.route("/number/trivia")
def main1():
    facts = ""
    response = requests.get(base_url + url_random_trivia)
    facts.append(response.text)
    return {"fact": facts}


@app.route("/number/math")
def main2():
    facts = ""
    response = requests.get(base_url + url_random_math)
    facts.append(response.text)
    return {"fact": facts}

app.run(port=3000)