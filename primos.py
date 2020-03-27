import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():

    cont2 = 0
    for div in range(0,1000+1):
        cont = 0
        if cont2 == 100:
            break

        for x in range(1,div+1):
            if div % x == 0:
                cont += 1

        if cont == 2:
            cont2 += 1         

    return x + ','



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

