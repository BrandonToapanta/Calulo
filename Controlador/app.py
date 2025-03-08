from flask import Flask, request, jsonify
import sympy as sp

app = Flask(__name__)

@app.route("/integrar", methods=["POST"])
def calcular_area():
    datos = request.json
    expresion = datos.get("funcion")
    a = float(datos.get("a"))
    b = float(datos.get("b"))
    
    x = sp.symbols('x')
    funcion = sp.sympify(expresion)
    area = sp.integrate(funcion, (x, a, b))
    
    return jsonify({"resultado": float(area)})

if __name__ == "__main__":
    app.run(debug=True)