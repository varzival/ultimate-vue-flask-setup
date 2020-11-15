from flask import Flask, render_template
#from flask_cors import CORS
from backend.api import api_bp
import os

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")
#CORS(app) - not needed as flask only serves static files

app.secret_key = os.urandom(16)

@app.route('/')
def index():
    return render_template("index.html")

app.register_blueprint(api_bp, url_prefix="/api")
            
if __name__ == "__main__":
    app.run(debug=True)

