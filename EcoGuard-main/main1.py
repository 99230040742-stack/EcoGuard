# --- vercel bootstrap: fallback DB + disable heavy ML (paste at top of main1.py) ---
import os

# If developer hasn't provided a DB URI in Vercel, use a local SQLite file
# so the app runs without an external DB. The SQLite file is ephemeral on Vercel.
if not os.environ.get("SQLALCHEMY_DATABASE_URI"):
    os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vercel.db"

# Prevent heavy ML model imports on cold start when not needed.
# Recommended: set DISABLE_AI=1 in Vercel Environment Variables.
DISABLE_AI = os.environ.get("DISABLE_AI", "0") == "1"
if DISABLE_AI:
    print("DISABLE_AI=1 -> skipping heavy ML imports and model loading")
# --- end bootstrap ---
from main1 import app
app = Flask(__name__)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port) 