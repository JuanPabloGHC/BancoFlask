from flask import Flask, render_template, request, redirect, url_for
import json
from models.Banco import Banco
from models.Account import Account

app = Flask(__name__)
banco = Banco("GM CUBE")

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
        cuenta = request.form['Cuenta']
        userItem = banco.SearchUser(cuenta)
        if userItem != None:
            return render_template('cuenta.html', user = userItem, mensaje="")
        else:
            return redirect(url_for('main', mensaje = "NO EXISTE"))
    
    else:
        # Transferencia
        try:
            destinatario = request.form['CuentaDestino']
            cantidad = request.form.get('Cantidad', type=int)
            userItem = banco.SearchUser(str(cuenta))
            cuentaDestino = banco.SearchUser(destinatario)
            saldoSuficiente = userItem.CheckSufficientBalance(cantidad)
            if cuentaDestino == None or cantidad < 0 or saldoSuficiente == False:
                return render_template('cuenta.html', user = userItem, mensaje="INVALIDO")
            banco.Transfer(userItem, cuentaDestino, cantidad)
            return render_template("cuenta.html", user=userItem, mensaje="HECHO")
        except Exception:
            pass

        # Deposito o Retiro
        userItem = banco.SearchUser(str(cuenta))
        cantidad = request.form.get('Cantidad', type=int)
        if cantidad < 0:
            return render_template('cuenta.html', user = userItem, mensaje="INVALIDO")
        movimiento = request.form.get('Movimiento')
        if movimiento == "D":
            banco.Deposit(userItem, cantidad)
        elif movimiento == "R":
            if userItem.CheckSufficientBalance(cantidad) == False:
                return render_template('cuenta.html', user = userItem, mensaje="INVALIDO")
            banco.Withdrawal(userItem, cantidad)
        return render_template('cuenta.html', user = userItem, mensaje="HECHO")

@app.route('/registrar', methods=['POST'])
def registro():
    nombre = request.form['Nombre']
    cuenta = request.form['Cuenta']
    saldo = int(request.form['Saldo'])
    userItem = banco.SearchUser(cuenta)
    if userItem != None:
        return redirect(url_for('main', mensaje = "USUARIO EXISTENTE"))
    banco.AddUser(nombre, cuenta, saldo)
    return redirect(url_for('main', mensaje = "REGISTRADO"))



if __name__ == '__main__':
    app.run(debug=True)