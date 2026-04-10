# api/index.py
# Vercel will use this file to start your Flask app
from main1 import app
app = Flask(__name__)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)  # make sure your main file is main1.py and defines app = Flask(__name__)
