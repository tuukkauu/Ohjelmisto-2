import json

import mysql.connector
from flask import Flask, jsonify, Response

app = Flask(__name__)

# tietokantayhteys
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="tuukka",
    passwd="Muumilaakso",
    autocommit=True,
    collation="utf8mb4_general_ci",
)


def query(ICAO):
    sql = f"SELECT airport.ident AS ICAO, airport.name AS airport, airport.municipality AS municipality FROM airport where airport.ident = %s;"
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (ICAO,))
    result = kursori.fetchone()  # palauttaa tuloksen tai None jos väärä ICAO tunnus

    print(f"Kyselyn tulos: {result}")  # virheenkorjausta varten
    return result


@app.route("/kenttä/<string:ICAO>")
def kentta(ICAO):
    kentta_tiedot = query(ICAO)  # kutsutaan tietokantafunktiota hakemaan käyttäjän ICAO tunnuksella tiedot

    if kentta_tiedot is not None:
        vastaus = {
            "ICAO": kentta_tiedot["ICAO"],
            "Name": kentta_tiedot["airport"],
            "Municipality": kentta_tiedot["municipality"]
        }
    else:
        vastaus = {"error": "Airport not found, check the ICAO code."}

    return jsonify(vastaus)  # json muotoinen vastaus

@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status" : "404",
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

