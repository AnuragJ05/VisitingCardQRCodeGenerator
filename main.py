from flask import Flask, redirect, url_for, request, render_template
from utils.qrcode_utils import text_to_qr_generator

app = Flask(__name__)
form_data = None


@app.route('/qrcode')
def get_qr():
    text_to_qr_generator(form_data)
    return render_template("qr.html")


@app.route('/home', methods=["Post"])
def home():
    if request.method == "POST":
        global form_data
        form_data = request.form
        form_data = dict(form_data)
        return redirect(url_for("get_qr"))


@app.route('/', methods=["Post", "Get"])
def index():
    return render_template("index.html")


if __name__ == '__main__':
    # Default 127.0.0.1:5000
    app.run()
