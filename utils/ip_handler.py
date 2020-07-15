import os
from urllib import request, urlopen

def handle_ip(remote_ip):
    print("===========")
    print("Visitor: ", remote_ip)
    print("===========")
    api_key = os.environ.get('IPTOEARTH_API_KEY')
    client_id = os.environ.get('IPTOEARTH_CLIENT_ID')
    request = request('https://iptoearth.expeditedaddons.com/?api_key=' + api_key + '&ip=' + remote_ip)
    result = urlopen(request).read()
    print("RESULT: ", result)
    return

