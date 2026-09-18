from flask import Flask, render_template, request
import pickle
import pandas as pd


# ==========================================
# CREATE FLASK APPLICATION
# ==========================================

app = Flask(
    __name__,
    template_folder="web_pages",
    static_folder="assets"
)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

try:

    with open("model/crop_model.pkl", "rb") as file:
        model = pickle.load(file)

    print("Model loaded successfully!")

except FileNotFoundError:

    print("ERROR: Model file not found!")
    print("Please run train_model.py first.")

    model = None


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template("home.html")


# ==========================================
# PREDICTION
# ==========================================

@app.route("/predict", methods=["POST"])
def predict():

    if model is None:

        return render_template(
            "home.html",
            error="Model not found. Please train the model first."
        )


    try:

        # ----------------------------------
        # GET USER INPUT
        # ----------------------------------

        N = float(request.form["N"])

        P = float(request.form["P"])

        K = float(request.form["K"])

        temperature = float(
            request.form["temperature"]
        )

        humidity = float(
            request.form["humidity"]
        )

        ph = float(
            request.form["ph"]
        )

        rainfall = float(
            request.form["rainfall"]
        )


        # ----------------------------------
        # VALIDATE INPUT
        # ----------------------------------

        if N < 0 or P < 0 or K < 0:

            return render_template(
                "home.html",
                error="N, P and K values cannot be negative."
            )


        if humidity < 0 or humidity > 100:

            return render_template(
                "home.html",
                error="Humidity must be between 0 and 100."
            )


        if ph < 0 or ph > 14:

            return render_template(
                "home.html",
                error="Soil pH must be between 0 and 14."
            )


        # ----------------------------------
        # CREATE INPUT DATAFRAME
        # ----------------------------------

        input_data = pd.DataFrame(
            [[
                N,
                P,
                K,
                temperature,
                humidity,
                ph,
                rainfall
            ]],

            columns=[
                "N",
                "P",
                "K",
                "temperature",
                "humidity",
                "ph",
                "rainfall"
            ]
        )


        # ----------------------------------
        # PREDICT CROP
        # ----------------------------------

        prediction = model.predict(input_data)


        crop = prediction[0]


        # ----------------------------------
        # RETURN RESULT
        # ----------------------------------

        return render_template(
            "home.html",
            prediction=crop
        )


    except ValueError:

        return render_template(
            "home.html",
            error="Please enter valid numeric values."
        )


    except Exception as e:

        return render_template(
            "home.html",
            error="Something went wrong: " + str(e)
        )


# ==========================================
# RUN APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )