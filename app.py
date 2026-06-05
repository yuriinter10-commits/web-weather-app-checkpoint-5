from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = "93339e8b1ff5c97ccf13b536cab33117"

@app.route("/", methods=["GET", "POST"])
def index():
    clima = None
    erro = None

    if request.method == "POST":
        cidade = request.form.get("cidade")
        if cidade:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"

            try:
                resposta = requests.get(url)

                if resposta.status_code == 200:
                    clima = resposta.json()
                else:
                    erro = "Cidade não encontrada! Tente novamente."

            except requests.exceptions.RequestException:
                erro = "Não foi possivel conectar ao servidor de clima."
                 
        print(clima)

    return render_template("index.html", clima=clima, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)