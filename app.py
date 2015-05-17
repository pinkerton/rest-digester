import json
from multiprocessing import Process
import shlex
import subprocess
import sys
import threading

from flask import Flask, render_template
from flask.ext.socketio import SocketIO, send, emit
from libmproxy import flow
import zmq

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app)

thread_data = threading.local()


cmd = 'mitmdump -s endpoints.py'

@socketio.on('ready2go', namespace='/endpoints')
def handle_json(json):
    print "Browser said okay"
    subprocess.call(shlex.split(cmd))
    print "Called script"
    while True:
        message = thread_data.socket.recv_json()
        obj = json.loads(message)[0]
        thread_data.socket.send_json(obj)

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
    return render_template('requests.html', endpoint=None)

if __name__ == "__main__":
    # mitmproxy -w two.out "~d api\.zondr\.com"    
    #generate_pem()
    #remind_pem()
    thread_data.context = zmq.Context()
    thread_data.socket = thread_data.context.socket(zmq.PULL)
    thread_data.socket.bind('tcp://127.0.0.1:12345')
    socketio.run(app)    
