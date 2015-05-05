import json
import shlex
import subprocess
import sys

from flask import Flask
from flask import render_template
from libmproxy import flow

app = Flask(__name__)

def url_to_filter(url):
    pass

def generate_pem():
    subprocess.call(['mitmproxy'])

def remind_pem():
    print "Cert generated: ~/.mitmproxy/mitmproxy-ca-cert.pem"
    print "Email this to yourself and open it with Mail"

def parse_dump(dumpfile):
    with open(dumpfile, "rb") as logfile:
        freader = flow.FlowReader(logfile)
        try:
            for f in freader.stream():
                print(f)
                print(f.request.host)
                json.dump(f.get_state(), sys.stdout, indent=4)
                print ""
        except flow.FlowReadError, v:
            print "Flow file corrupted. Stopped loading."

@app.route('/')
@app.route('/setup')
def setup():
    return render_template('setup.html')

@app.route('/endpoints')
def endpoints():
    return render_template('endpoints.html')

@app.route('/requests')
def live_requests():
    return render_template('requests.html')

if __name__ == "__main__":
    # mitmproxy -w two.out "~d api\.zondr\.com"    
    #generate_pem()
    #remind_pem()
    app.run(debug=True)
