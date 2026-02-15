from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return 10/0

if __name__ == "__main__":
    app.run()
