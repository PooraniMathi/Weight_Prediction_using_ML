from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# ---- Load trained model ----
MODEL_PATH = os.path.join(os.path.dirname(__file__), "models", "linregpredict.pkl")
model = None

def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        try:
            model = joblib.load(MODEL_PATH)
            print("✅ Model loaded from", MODEL_PATH)
        except Exception as e:
            print("⚠️ Could not load model:", e)

load_model()

# Fallback if no model file is found
def fallback_predict(height_cm: float) -> float:
    return 0.9 * (height_cm - 100)

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/api/predict")
def api_predict():
    try:
        data = request.get_json(force=True)
        height = float(data.get("height_cm", None))
    except Exception:
        return jsonify({"ok": False, "error": "Invalid JSON or 'height_cm' missing."}), 400

    if not (50 <= height <= 300):
        return jsonify({"ok": False, "error": "height_cm must be between 50 and 300."}), 422

    try:
        if model is not None:
            pred = float(model.predict(np.array([[height]]))[0])
        else:
            pred = float(fallback_predict(height))
    except Exception as e:
        return jsonify({"ok": False, "error": f"Prediction failed: {e}"}), 500

    return jsonify({"ok": True, "height_cm": height, "predicted_weight_kg": round(pred, 2)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
