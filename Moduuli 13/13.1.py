from flask import Flask, jsonify
import json
#luku = int(input("Syötä tähän luku tarkistaaksesti, onko se alkuluku: "))

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    luku = int(luku)
    isPrime = True

    if luku <= 1:
        isPrime = False

    else:
        for i in range(2, int(luku ** 0.5) + 1):
            if luku % i == 0:
                isPrime = False
                break

    vastaus = {
        "Number": luku,
        "isPrime": isPrime
    }

    return jsonify(vastaus)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
