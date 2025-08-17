from flask import Flask, render_template, request

uygulama = Flask(__name__)

isimler = []  # Kullanıcıların girdiği isimleri saklayacak liste

@uygulama.route("/", methods=["GET", "POST"])
def anasayfa():
    if request.method == "POST":
        yeni_isim = request.form.get("isim")
        if yeni_isim:
            isimler.append(yeni_isim)  # Listeye ekle
    return render_template("index.html", isimler=isimler)

if __name__ == "__main__":
    uygulama.run()