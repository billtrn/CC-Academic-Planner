import json

from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "9ea87e4f94007164efd29eab1793d57f"


@app.route("/courses")
def get_courses():
    with open('classes.json', 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    app.run(debug=True)
