from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

usuarios = []

with open ('data.json', 'r') as file:
    data = json.load(file)

# HOME
@app.route('/', methods=['GET'])
@app.route('/<mensaje>', methods=['GET'])
def main(mensaje=None):
    if mensaje != None:
        return render_template('index.html', mensaje = mensaje)
    return render_template('index.html', mensaje="")


@app.route('/cuenta', methods=['GET', 'POST'])
@app.route('/cuenta/<cuenta>', methods=['POST'])
def login(cuenta=None):
    if cuenta == None:
        userItem = " "
        cuenta = request.form['Cuenta']
        for user in data:
            if user["Cuenta"] == cuenta:
                userItem = user
        if userItem != " ":
            return render_template('cuenta.html', user = userItem, mensaje="")
        else:
            return redirect(url_for('main', mensaje = "NO EXISTE"))
    
    else:
        # Transferencia
        try:
            cuentaDestino = ""
            destinatario = request.form['CuentaDestino']
            cantidad = request.form.get('Cantidad', type=int)
            for user in data:
                if user["Cuenta"] == destinatario:
                    cuentaDestino = user
                elif user["Cuenta"] == cuenta:
                    userItem = user
            if cuentaDestino == "" or cantidad < 0 or userItem["Saldo"] < cantidad:
                return render_template('cuenta.html', user = userItem, mensaje="INVALIDO")
            userItem["Saldo"] -= cantidad
            cuentaDestino["Saldo"] += cantidad
            return render_template("cuenta.html", user=userItem, mensaje="HECHO")
        except Exception:
            pass

        # Deposito o Retiro
        for user in data:
            if user["Cuenta"] == cuenta:
                userItem = user
        cantidad = request.form.get('Cantidad', type=int)
        if cantidad < 0:
            return render_template('cuenta.html', user = userItem, mensaje="INVALIDO")
        movimiento = request.form.get('Movimiento')
        if movimiento == "D":
            userItem["Saldo"] += cantidad
        elif movimiento == "R":
            if userItem["Saldo"] < cantidad:
                return render_template('cuenta.html', user = userItem, mensaje="INVALIDO")
            userItem["Saldo"] -= cantidad
        return render_template('cuenta.html', user = userItem, mensaje="HECHO")

@app.route('/registrar', methods=['POST'])
def registro():
    nombre = request.form['Nombre']
    cuenta = request.form['Cuenta']
    saldo = int(request.form['Saldo'])
    for user in data:
        if user["Cuenta"] == cuenta:
            return redirect(url_for('main', mensaje = "USUARIO EXISTENTE"))
    user = {
        "Nombre": nombre,
        "Cuenta": cuenta,
        "Saldo": saldo
    }
    data.append(user)
    return redirect(url_for('main', mensaje = "REGISTRADO"))



if __name__ == '__main__':
    app.run(debug=True)