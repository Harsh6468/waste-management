from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib
import os
from data.preprocess import preprocess_data

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
    )

MODEL_PATH = os.path.join("models", "final_model.pkl")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        df_processed = preprocess_data(df, is_train=False)

        model = joblib.load(MODEL_PATH)
        prediction = model.predict(df_processed)[0]
        return jsonify({"Recycling Rate (%)": prediction})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
