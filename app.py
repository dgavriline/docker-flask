from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Alex"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
#print("What's poppin")
