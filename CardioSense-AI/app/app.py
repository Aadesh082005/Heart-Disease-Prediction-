
from pathlib import Path

from flask import Flask, render_template, request

from app.predict import predict_heart_risk
from app.utils import validate_inputs, FEATURE_NAMES

ROOT = Path(__file__).resolve().parent.parent
PUBLIC_DIR = ROOT / "public"

app = Flask(
    __name__,
    template_folder=str(ROOT / "templates"),
    static_folder=str(PUBLIC_DIR),
    static_url_path="",
)

app.config["MAX_CONTENT_LENGTH"] = 16 * 1024


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/predict", methods=["GET", "POST"])
def predict():
    error = None

    if request.method == "POST":
        try:
            values = validate_inputs(request.form)
            result = predict_heart_risk(values)

            return render_template(
                "result.html",
                result=result,
                values=dict(zip(FEATURE_NAMES, values)),
            )
        except (ValueError, FileNotFoundError, OSError) as exc:
            error = str(exc)

    return render_template(
        "predict.html",
        error=error,
        form_data=request.form if request.method == "POST" else {},
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
