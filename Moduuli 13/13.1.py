from flask import Flask, jsonify, Response
import json


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

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen paatepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
