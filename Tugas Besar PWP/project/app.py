from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def edit_profil():
    return render_template("edit_profil.html")

@app.route("/mydompet")
def mydompet():
    return render_template("mydompet.html", saldo=0)

@app.route("/galang-dana")
def galang_dana():
    campaigns = ["Bantu Korban Banjir", "Donasi Pendidikan"]
    return render_template("galang_dana.html", campaigns=campaigns)

@app.route("/kategori")
def kategori():
    data = ["Bantuan Pendidikan", "Bencana Alam", "Difabel",
            "Kemanusiaan", "Lingkungan", "Zakat"]
    return render_template("kategori.html", kategori=data)

if __name__ == "__main__":
    app.run(debug=True)

