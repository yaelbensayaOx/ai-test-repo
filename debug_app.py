"""Flask app — intentionally vulnerable for SAST testing."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello"


if __name__ == "__main__":
    # B201: Flask running with debug=True
    app.run(host="0.0.0.0", debug=True)
