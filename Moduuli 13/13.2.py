import  mysql.connector

def query(code):
    sql = f"SELECT airport.ident, airport.name, airport.municipality FROM airport where airport.ident = 'EFHK';"
    kursori = yhteys.cursor()
    kursori.execute(sql, (code))
    tulos = kursori.fetchall()

    vastaus = {
        "ICAO": code,
        "Name": code,
        "Municipality": code
    }

#pääohjelma
yhteys = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="flight_game",
    user="tuukka",
    passwd="Muumilaakso",
    autocommit=True,
    collation = "utf8mb4_general_ci",
)