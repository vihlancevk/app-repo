from flask import Flask

# sonar-python:S5527
app = Flask(__name__)


@app.route("/")
def start():
    return "Stop the world!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
