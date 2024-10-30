import json
import requests
"
k = input("Vastaa k, jos haluat kuulla Chuck Norris vitsin: ")

vastaus = k

# pyyntö:
if vastaus == k:
    pyyntö = "https://api.chucknorris.io/jokes/random/search/shows?q=:query"

