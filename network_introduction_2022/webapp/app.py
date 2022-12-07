from flask import Flask, render_template, request, url_for, flash, redirect
from os import stat, urandom
from subprocess import run
from pathlib2 import Path

app = Flask(__name__)

# Secret key generated with the following python code
# import os
# os.urandom(24).hex()
# it is necessary for flask.flash()
app.secret_key = urandom(24).hex()
#app.secret_key = 'e371ea2ad1633a5526b756c303695606927c5b0570f34e50'

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        ssid = request.form['ssid']
        pwd = request.form['pwd']

        if not ssid or not pwd:
            flash('SSID and password are required!')
        else:
            wifi_string = 'network={\n' + '\tssid="{}"\n'.format(ssid) + '\tpsk="{}"\n'.format(pwd) + '\tkey_mgmt=WPA-PSK\n' + '}\n\n'
            
            # check if wpa_supplicant is empty
            if stat('/etc/wpa_supplicant/wpa_supplicant.conf').st_size == 0:
                f = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'w')
                f.write(
                    'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n' +
                    'update_config=1\n' +
                    'country=IT\n\n' +
                    wifi_string
                )
            else:
                f = open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a')
                f.write(wifi_string)
            f.close()
            # reload wifi settings TODO
            
            # check for internet connection
            ip = run(['hostname', '-I'], capture_output=True)
            if ip.stdout.decode("utf-8") != '\n':
                return redirect(url_for('ok'))
            else:
                # Note: give read permission to wpa_supplicant.conf
                # delete wifi wrong credentials from wpa_supplicant.conf
                file = Path(r'/etc/wpa_supplicant/wpa_supplicant.conf')
                data = file.read_text()
                data = data.replace(wifi_string, '')
                file.write_text(data)
                # Note: remove read permission to wpa_supplicant.conf
                return redirect(url_for('error'))
    
    return render_template('index.html')

@app.route('/ok')
def ok():
    return render_template('ok.html')

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    # COMMENT DEBUG=TRUE LINE AND ADD VALIDE CERTIFICATES BEFORE RELEASE!!!
    app.run(debug=True, host='0.0.0.0', ssl_context='adhoc', port=80) # COMMENT BEFORE RELEASE (PORT 443?)
    #app.run(host='0.0.0.0', ssl_context=('cert.pem', 'key.pem'), port=443) # UNCOMMENT BEFORE RELEASE
