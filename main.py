from flask import Flask, escape, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shell", methods=['GET', 'POST'])
def shell(ipaddr = None):
    if request.args.get('ipaddr', None):
        ipaddr = shbox(request.args['ipaddr'])
        ip = ipaddr
        return redirect( url_for('shbox', ipaddr=ipaddr ))
        #return redirect('''<a href='http://{}:4200' target='myredhat'>Click here to show OS</a><iframe width='100%' height='100%' name='myredhat' />'''.format(ip))
    return render_template("shell.html", ipaddr=ipaddr)

@app.route("/shbox/<ipaddr>")
def shbox(ipaddr):
    
    #ip = 'http://192.168.43.92:4200'
    ip = ipaddr
    if ip == 'http://192.168.43.92:4200':
        return redirect('http://192.168.43.92:4200')
    else:
        return redirect('http://192.168.43.239:4200')
    '''
    elif ip == 'http://192.168.43.239:4200/':
        return redirect('http://192.168.43.239:4200/')

    elif ip == 'http://192.168.43.142:4200/':
        return redirect('http://192.168.43.142:4200/')

    else:
        return redirect('http://192.168.43.143:4200/')
    '''
    #return redirect(ip, 303)
    #return redirect(url_for('shbox', ipaddr=ipaddr))
    #return redirect('http://www.google.com')

@app.route("/docker", methods=['GET', 'POST'])
def docker():
    return redirect('https://nitish-iygl.localhost.run')
    #return render_template("docker.html")

@app.route("/vnc")
def vnc():
    return render_template("vnc.html")

@app.route("/hadoop")
def hadoop():
    return render_template("hadoop.html")

@app.route("/new")
def new():
    return render_template("new.html")

'''
@app.route("/aut")
def aut():
    return render_template("aut.php")
'''