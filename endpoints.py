from libmproxy import flow
from libmproxy.protocol.http import decoded
import zmq

endpoints = {}
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.connect('tcp://127.0.0.1:5556')

def start(context, argv):
    print "starting"

def done(context):
    print endpoints
    socket.close()

def request(contet, flow):
    endpoint = {
        'host': flow.request.host,
        'path': flow.request.path
    }
    endpoints[flow.request.host] = flow.request.path
    # send the endpoints over the wire
    socket.send_json(endpoint)

def response(contet, flow):
    with decoded(flow.response):
        pass
        #print flow.response.host, flow.response.path

def responseheaders(context, flow):
    flow.response.stream = True
    print flow.request.host, flow.request.path

