import os
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "this is a test!"
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port)
