import os
from flask import Flask, render_template, request

uygulama = Flask(__name__)

isimler = []

@uygulama.route("/", methods=["GET", "POST"])
def anasayfa():
    if request.method == "POST":
        yeni_isim = request.form.get("isim")
        if yeni_isim:
            isimler.append(yeni_isim)
    return render_template("index.html", isimler=isimler)

if __name__ == "__main__":
    uygulama.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
