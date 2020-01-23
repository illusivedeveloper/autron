from flask import Flask, escape, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shell", methods=['GET', 'POST'])
def shell(ipaddr = None):
    if request.args.get('ipaddr', None):
        ipaddr = shbox(request.args['ipaddr'])
        return redirect( url_for('shbox', ipaddr=ipaddr ))

    return render_template("shell.html", ipaddr=ipaddr)

@app.route("/shbox/<ipaddr>")
def shbox(ipaddr):
    ip = 'http://192.168.43.92:4200'
    #return redirect(ip, 303)
    return redirect(ip)

@app.route("/docker")
def docker():
    return render_template("docker.html")

@app.route("/vnc")
def vnc():
    return render_template("vnc.html")

@app.route("/hadoop")
def hadoop():
    return render_template("hadoop.html")
